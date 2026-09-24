from itertools import combinations

import gradio as gr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {
    "Order_ID", "Order_Date", "Customer_ID", "Category", "Product",
    "Quantity", "Unit_Price", "Discount", "Region",
}
NUMERIC_FEATURES = ["Quantity", "Unit_Price", "Discount", "Revenue"]


SAMPLE_DATA = pd.DataFrame({
    "Order_ID": range(1001, 1021),
    "Order_Date": [
        "2025-01-05", "2025-01-12", "2025-01-18", "2025-02-03", "2025-02-11",
        "2025-02-20", "2025-03-02", "2025-03-15", "2025-03-22", "2025-04-04",
        "2025-04-12", "2025-04-25", "2025-05-06", "2025-05-14", "2025-05-28",
        "2025-06-07", "2025-06-16", "2025-06-23", "2025-07-03", "2025-07-18",
    ],
    "Customer_ID": [
        "C001", "C002", "C003", "C001", "C004", "C005", "C006", "C002",
        "C007", "C008", "C009", "C003", "C010", "C011", "C012", "C004",
        "C013", "C014", "C015", "C005",
    ],
    "Category": [
        "Electronics", "Home", "Fashion", "Electronics", "Beauty", "Home",
        "Fashion", "Electronics", "Beauty", "Home", "Fashion", "Electronics",
        "Beauty", "Home", "Fashion", "Electronics", "Beauty", "Home", "Fashion",
        "Electronics",
    ],
    "Product": [
        "Headphones", "Desk Lamp", "T-Shirt", "Keyboard", "Skincare Set",
        "Coffee Maker", "Jeans", "Mouse", "Face Cream", "Cushion", "Sneakers",
        "T-Shirt", "Shampoo", "Table Organizer", "Jacket", "Webcam", "Perfume",
        "Vacuum Cleaner", "Dress", "Headphones",
    ],
    "Quantity": [2, 1, 3, 1, 2, 1, 2, 3, 1, 2, 1, 1, 3, 2, 1, 2, 1, 1, 2, 1],
    "Unit_Price": [45, 35, 22, 70, 30, 85, 55, 25, 28, 18, 75, 240, 20, 32, 90, 65, 60, 150, 80, 320],
    "Discount": [0.10, 0.00, 0.05, 0.15, 0.10, 0.00, 0.05, 0.00, 0.10, 0.05, 0.15, 0.10, 0.00, 0.05, 0.10, 0.00, 0.15, 0.05, 0.10, 0.20],
    "Region": [
        "North", "South", "East", "North", "West", "South", "East", "North",
        "West", "South", "East", "North", "West", "South", "East", "North",
        "West", "South", "East", "North",
    ],
})


def load_data(file_path=None):
    """Load a CSV and preprocess the fields needed by every algorithm."""
    data = SAMPLE_DATA.copy() if file_path is None else pd.read_csv(file_path)
    missing = sorted(REQUIRED_COLUMNS - set(data.columns))
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))

    data = data.copy()
    data["Order_Date"] = pd.to_datetime(data["Order_Date"], errors="coerce")
    for column in ("Quantity", "Unit_Price", "Discount"):
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data["Discount"] = data["Discount"].fillna(0).clip(0, 1)
    if data[["Order_Date", "Quantity", "Unit_Price"]].isna().any().any():
        raise ValueError("Order_Date, Quantity, and Unit_Price must contain valid values.")
    data["Revenue"] = data["Quantity"] * data["Unit_Price"] * (1 - data["Discount"])
    return data


def standardize(values):
    values = np.asarray(values, dtype=float)
    scale = values.std(axis=0)
    scale[scale == 0] = 1
    return (values - values.mean(axis=0)) / scale


def kmeans(values, cluster_count, max_iterations=100):
    """Run K-Means using deterministic, evenly spaced initial centroids."""
    values = np.asarray(values, dtype=float)
    cluster_count = min(max(1, int(cluster_count)), len(values))
    indices = np.linspace(0, len(values) - 1, cluster_count, dtype=int)
    centroids = values[indices].copy()
    labels = np.zeros(len(values), dtype=int)
    for _ in range(max_iterations):
        distances = ((values[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2)
        new_labels = distances.argmin(axis=1)
        new_centroids = centroids.copy()
        for cluster_id in range(cluster_count):
            members = values[new_labels == cluster_id]
            if len(members):
                new_centroids[cluster_id] = members.mean(axis=0)
        if np.array_equal(labels, new_labels):
            break
        labels, centroids = new_labels, new_centroids
    return labels, centroids


def pca(values, components=2):
    """Reduce standardized values with an eigenvector-based PCA."""
    scaled = standardize(values)
    covariance = np.cov(scaled, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    order = np.argsort(eigenvalues)[::-1][: min(components, scaled.shape[1])]
    reduced = scaled @ eigenvectors[:, order]
    explained = eigenvalues[order] / eigenvalues.sum() * 100
    return reduced, explained


def detect_anomalies(values, percentile=95):
    """Flag rows whose standardized Euclidean distance is unusually large."""
    scores = np.sqrt((standardize(values) ** 2).sum(axis=1))
    threshold = np.percentile(scores, percentile) if len(scores) else 0
    return scores, scores >= threshold


def plot_clustering(pca_results):
    """Return a matplotlib scatter plot showing transaction clusters in PCA space."""
    fig, ax = plt.subplots(figsize=(7, 5))
    if pca_results.empty:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")
        ax.set_axis_off()
        return fig

    for cluster_id in sorted(pca_results["Cluster"].unique()):
        cluster_points = pca_results[pca_results["Cluster"] == cluster_id]
        ax.scatter(
            cluster_points["PC1"],
            cluster_points["PC2"],
            s=80,
            alpha=0.75,
            label=f"Cluster {cluster_id}",
        )

    ax.set_title("K-Means Clustering in PCA Space")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.legend(title="Clusters")
    fig.tight_layout()
    return fig


def association_rules(data, minimum_support=0.10, minimum_confidence=0.30):
    """Mine frequent product sets and rules with a small Apriori implementation."""
    baskets = data.groupby("Customer_ID")["Product"].apply(lambda products: set(products)).tolist()
    basket_count = len(baskets)
    if not basket_count:
        return pd.DataFrame(columns=["Rule", "Support", "Confidence", "Lift"])

    def support(itemset):
        return sum(itemset.issubset(basket) for basket in baskets) / basket_count

    frequent = {}
    single_items = sorted({item for basket in baskets for item in basket})
    current = {frozenset([item]): support({item}) for item in single_items}
    current = {items: value for items, value in current.items() if value >= minimum_support}
    size = 1
    while current:
        frequent.update(current)
        size += 1
        previous = list(current)
        candidates = {
            frozenset(set(left) | set(right))
            for left, right in combinations(previous, 2)
            if len(set(left) | set(right)) == size
        }
        current = {
            itemset: support(itemset)
            for itemset in candidates
            if support(itemset) >= minimum_support
        }

    rules = []
    for itemset, itemset_support in frequent.items():
        if len(itemset) < 2:
            continue
        for item_count in range(1, len(itemset)):
            for left_tuple in combinations(sorted(itemset), item_count):
                left = frozenset(left_tuple)
                right = itemset - left
                left_support = frequent.get(left, support(left))
                right_support = frequent.get(right, support(right))
                confidence = itemset_support / left_support if left_support else 0
                lift = confidence / right_support if right_support else 0
                if confidence >= minimum_confidence:
                    rules.append({
                        "Rule": ", ".join(sorted(left)) + " -> " + ", ".join(sorted(right)),
                        "Support": round(itemset_support, 3),
                        "Confidence": round(confidence, 3),
                        "Lift": round(lift, 3),
                    })
    if not rules:
        return pd.DataFrame(columns=["Rule", "Support", "Confidence", "Lift"])
    return pd.DataFrame(rules).sort_values("Lift", ascending=False)


def analyze_ecommerce(file_path=None, cluster_count=3, minimum_support=0.05, minimum_confidence=0.30):
    """Run preprocessing, clustering, PCA, anomaly detection, and Apriori."""
    data = load_data(file_path)
    features = data[NUMERIC_FEATURES].to_numpy(dtype=float)
    scaled_features = standardize(features)

    labels, _ = kmeans(scaled_features, cluster_count)
    reduced, explained = pca(features)
    scores, anomaly_flags = detect_anomalies(features)

    cluster_results = data[["Order_ID", "Customer_ID", "Product", "Revenue"]].copy()
    cluster_results["Cluster"] = labels + 1
    cluster_results["Anomaly_Score"] = scores.round(3)
    cluster_results["Anomaly"] = np.where(anomaly_flags, "Yes", "No")

    pca_results = data[["Order_ID", "Product"]].copy()
    pca_results["PC1"] = reduced[:, 0].round(3)
    pca_results["PC2"] = reduced[:, 1].round(3) if reduced.shape[1] > 1 else 0
    pca_results["Cluster"] = labels + 1

    category_results = data.groupby("Category", as_index=False).agg(
        Orders=("Order_ID", "nunique"), Units_Sold=("Quantity", "sum"), Revenue=("Revenue", "sum")
    ).sort_values("Revenue", ascending=False)
    category_results["Revenue"] = category_results["Revenue"].round(2)
    rules = association_rules(data, minimum_support, minimum_confidence)

    total_revenue = data["Revenue"].sum()
    total_orders = data["Order_ID"].nunique()
    total_items = data["Quantity"].sum()
    explained_total = explained[:2].sum()
    max_category_revenue = category_results["Revenue"].max() or 1
    category_cards = "".join(
        "<div class='category-row'><span>{}</span><div class='category-track'><i style='width: {}%'></i></div><strong>${:,.2f}</strong></div>".format(
            row.Category, row.Revenue / max_category_revenue * 100, row.Revenue
        )
        for row in category_results.itertuples()
    )
    dashboard = """
    <section class='dashboard'>
      <div class='dashboard-heading'>
        <div><span class='eyebrow'>PERFORMANCE SNAPSHOT</span><h2>Commerce command center</h2></div>
        <span class='status-pill'>Analysis complete</span>
      </div>
      <div class='kpi-grid'>
        <div class='kpi-card accent'><span>NET REVENUE</span><b>${:,.2f}</b><small>after discounts</small></div>
        <div class='kpi-card'><span>ORDERS</span><b>{:,}</b><small>{:,} items sold</small></div>
        <div class='kpi-card'><span>AVG. ORDER VALUE</span><b>${:,.2f}</b><small>revenue per order</small></div>
        <div class='kpi-card'><span>ANOMALIES</span><b>{:,}</b><small>95th percentile threshold</small></div>
      </div>
      <div class='insight-grid'>
        <div class='insight-panel'><span class='panel-label'>TOP CATEGORIES BY REVENUE</span>{}</div>
        <div class='insight-panel compact'><span class='panel-label'>MODEL SIGNALS</span><p><b>{:.1f}%</b> variance captured by the first two PCA components.</p><p><b>{:,}</b> association rules meet your selected thresholds.</p><p><b>{}</b> clusters assigned with K-Means.</p></div>
      </div>
    </section>
    """.format(
        total_revenue,
        total_orders,
        total_items,
        total_revenue / total_orders if total_orders else 0,
        int(anomaly_flags.sum()),
        category_cards,
        explained_total,
        len(rules),
        int(cluster_count),
    )
    cluster_plot = plot_clustering(pca_results)
    return dashboard, cluster_results, cluster_plot, pca_results, category_results, rules


APP_CSS = """
.gradio-container { max-width: 1240px !important; background: #f4f7f6 !important; color: #123b3a !important; color-scheme: light; }
.gradio-container label, .gradio-container .tabitem, .gradio-container .block label span { color: #244d49 !important; }
.gradio-container input, .gradio-container textarea, .gradio-container button { color: #123b3a !important; }
.gradio-container input[type="number"], .gradio-container input[type="text"] { background: #ffffff !important; border: 1px solid #c7d8d4 !important; color: #123b3a !important; }
.gradio-container [data-testid="block-info"], .gradio-container .info-text { background: transparent !important; color: #244d49 !important; }
.gradio-container [data-testid="block-info"] { border-radius: 0 !important; padding: 0 !important; }
.gradio-container .gr-accordion, .gradio-container [data-testid="accordion"] { background: #ffffff !important; border: 1px solid #dbe7e4 !important; }
.gradio-container .gr-accordion > button, .gradio-container [data-testid="accordion"] > button { background: #ffffff !important; color: #123b3a !important; }
.gradio-container .gr-accordion > button span, .gradio-container [data-testid="accordion"] > button span { color: #123b3a !important; opacity: 1 !important; }
.gradio-container .gr-accordion > button svg, .gradio-container [data-testid="accordion"] > button svg { color: #2f7770 !important; stroke: #2f7770 !important; }
.gradio-container .gr-accordion *, .gradio-container [data-testid="accordion"] * { color: #244d49 !important; }
.gradio-container .gr-accordion > button *, .gradio-container [data-testid="accordion"] > button * { color: #123b3a !important; }
.gradio-container .gr-accordion > div, .gradio-container [data-testid="accordion"] > div { background: #ffffff !important; }
.gradio-container .gr-accordion .label-wrap, .gradio-container .gr-accordion .info, .gradio-container [data-testid="accordion"] .label-wrap, .gradio-container [data-testid="accordion"] .info { color: #244d49 !important; opacity: 1 !important; visibility: visible !important; }
.gradio-container .gr-accordion .label-wrap span, .gradio-container .gr-accordion .info span, .gradio-container [data-testid="accordion"] .label-wrap span, .gradio-container [data-testid="accordion"] .info span { color: #244d49 !important; opacity: 1 !important; }
.gradio-container .gr-accordion input[type="range"] + *, .gradio-container [data-testid="accordion"] input[type="range"] + * { color: #244d49 !important; }
.gradio-container .gr-accordion input[type="range"], .gradio-container [data-testid="accordion"] input[type="range"] { accent-color: #2f7770 !important; }
.gradio-container [data-testid="accordion-content"], .gradio-container [data-testid="accordion-content"] .form, .gradio-container [data-testid="accordion-content"] .block { background: #ffffff !important; }
.gradio-container [data-testid="accordion-content"] .block label, .gradio-container [data-testid="accordion-content"] .block .info-text, .gradio-container [data-testid="accordion-content"] .block span { color: #244d49 !important; }
.app-header { padding: 18px 2px 10px; }
.app-header h1 { color: #123b3a; font-size: 36px; letter-spacing: -1px; margin: 5px 0; }
.app-header p { color: #55706e; font-size: 15px; margin: 0; }
.eyebrow, .panel-label { color: #2f7770; font-size: 11px; font-weight: 700; letter-spacing: 1.4px; }
.dashboard { background: #ffffff !important; color: #244d49 !important; border: 1px solid #dbe7e4; border-radius: 14px; padding: 24px; margin: 18px 0; box-shadow: 0 8px 24px rgba(18, 59, 58, .06); }
.dashboard h2, .dashboard p, .dashboard span, .dashboard strong, .dashboard small, .dashboard b { color: #244d49; }
.dashboard .kpi-card.accent, .dashboard .kpi-card.accent b, .dashboard .kpi-card.accent small, .dashboard .kpi-card.accent span { color: #ffffff; }
.dashboard .kpi-card.accent span, .dashboard .kpi-card.accent small { color: #b9d9ce; }
.dashboard-heading { display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-bottom: 22px; }
.dashboard-heading h2 { color: #123b3a; font-size: 25px; margin: 5px 0 0; }
.status-pill { background: #e5f4ed; color: #247052; border-radius: 999px; padding: 8px 12px; font-size: 12px; font-weight: 700; }
.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.kpi-card { background: #f5f8f7; border: 1px solid #e3ece9; border-radius: 10px; padding: 17px; min-height: 90px; }
.kpi-card.accent { background: #123b3a; border-color: #123b3a; color: white; }
.kpi-card span { display: block; color: #71908b; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; }
.kpi-card.accent span { color: #9fd0bd; }
.kpi-card b { display: block; font-size: 25px; margin: 8px 0 4px; }
.kpi-card small { color: #71908b; font-size: 12px; }
.kpi-card.accent small { color: #b9d9ce; }
.insight-grid { display: grid; grid-template-columns: 1.2fr .8fr; gap: 12px; margin-top: 12px; }
.insight-panel { background: #fbfcfc; border: 1px solid #e3ece9; border-radius: 10px; padding: 17px; }
.category-row { display: grid; grid-template-columns: 115px 1fr 80px; gap: 10px; align-items: center; color: #355451; font-size: 13px; margin-top: 14px; }
.category-row strong { color: #123b3a; text-align: right; font-size: 12px; }
.category-track { background: #e6efec; height: 8px; border-radius: 4px; overflow: hidden; }
.category-track i { display: block; height: 100%; background: #2f7770; border-radius: 4px; }
.compact p { color: #55706e; font-size: 13px; line-height: 1.5; margin: 14px 0 0; }
.compact p b { color: #123b3a; font-size: 18px; }
@media (max-width: 760px) { .kpi-grid, .insight-grid { grid-template-columns: 1fr 1fr; } .dashboard-heading { align-items: flex-start; flex-direction: column; } }
@media (max-width: 480px) { .kpi-grid, .insight-grid { grid-template-columns: 1fr; } .category-row { grid-template-columns: 95px 1fr 70px; } }
"""


with gr.Blocks(title="E-Commerce Analytics") as app:
    gr.HTML("""
    <header class='app-header'>
      <span class='eyebrow'>E-COMMERCE INTELLIGENCE</span>
      <h1>Understand every order.</h1>
      <p>Upload your transaction data and turn raw sales into decisions.</p>
    </header>
    """)
    with gr.Row(equal_height=True):
        with gr.Column(scale=3):
            file_input = gr.File(label="Transaction CSV", file_types=[".csv"], type="filepath")
        with gr.Column(scale=1, min_width=180):
            analyze_button = gr.Button("Run analysis", variant="primary", size="lg")
    with gr.Accordion("Tune analysis", open=False):
        with gr.Row():
            cluster_input = gr.Slider(2, 6, value=3, step=1, label="Clusters", info="K-Means groups")
            support_input = gr.Slider(0.05, 0.50, value=0.05, step=0.05, label="Support", info="Apriori minimum")
            confidence_input = gr.Slider(0.10, 1.00, value=0.30, step=0.05, label="Confidence", info="Apriori minimum")

    summary_output = gr.HTML()
    with gr.Tab("Clustering and anomalies"):
        cluster_output = gr.Dataframe(label="K-Means clusters and anomaly scores", interactive=False)
        cluster_plot = gr.Plot(label="Cluster scatter plot")
    with gr.Tab("Dimensionality reduction"):
        pca_output = gr.Dataframe(label="PCA two-dimensional projection", interactive=False)
    with gr.Tab("Category summary"):
        category_output = gr.Dataframe(label="Category performance", interactive=False)
    with gr.Tab("Association rules"):
        rules_output = gr.Dataframe(label="Apriori product association rules", interactive=False)

    outputs = [summary_output, cluster_output, cluster_plot, pca_output, category_output, rules_output]
    inputs = [file_input, cluster_input, support_input, confidence_input]
    analyze_button.click(fn=analyze_ecommerce, inputs=inputs, outputs=outputs)
    app.load(fn=analyze_ecommerce, inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    app.launch(css=APP_CSS, theme=gr.themes.Soft(primary_hue="teal", neutral_hue="slate"))
