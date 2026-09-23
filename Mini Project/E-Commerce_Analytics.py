"""Complete E-Commerce Analytics project with a Gradio interface.

The algorithms in this file use only NumPy and pandas. No project-local
modules or machine-learning framework are required.
"""

from itertools import combinations

import gradio as gr
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
        "Monitor", "Shampoo", "Table Organizer", "Jacket", "Webcam", "Perfume",
        "Vacuum Cleaner", "Dress", "Tablet",
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


def analyze_ecommerce(file_path=None, cluster_count=3, minimum_support=0.10, minimum_confidence=0.30):
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

    summary = "\n".join([
        "# E-Commerce Analytics",
        "",
        "| Metric | Result |",
        "|---|---:|",
        "| Revenue | ${:,.2f} |".format(data["Revenue"].sum()),
        "| Orders | {:,} |".format(data["Order_ID"].nunique()),
        "| Products | {:,} |".format(data["Product"].nunique()),
        "| PCA variance explained | {:.1f}% + {:.1f}% |".format(explained[0], explained[1] if len(explained) > 1 else 0),
        "| Anomalies detected | {:,} |".format(int(anomaly_flags.sum())),
        "| Association rules | {:,} |".format(len(rules)),
    ])
    return summary, cluster_results, pca_results, category_results, rules


with gr.Blocks(title="E-Commerce Analytics") as app:
    gr.Markdown("# E-Commerce Analytics\nUpload a CSV or use the included sample data.")
    with gr.Row():
        file_input = gr.File(label="Transaction CSV", file_types=[".csv"], type="filepath")
        cluster_input = gr.Slider(2, 6, value=3, step=1, label="Number of clusters")
        support_input = gr.Slider(0.05, 0.50, value=0.10, step=0.05, label="Minimum support")
        confidence_input = gr.Slider(0.10, 1.00, value=0.30, step=0.05, label="Minimum confidence")
    analyze_button = gr.Button("Run Complete Analysis", variant="primary")
    summary_output = gr.Markdown()
    with gr.Tab("Clustering and anomalies"):
        cluster_output = gr.Dataframe(label="K-Means clusters and anomaly scores", interactive=False)
    with gr.Tab("Dimensionality reduction"):
        pca_output = gr.Dataframe(label="PCA two-dimensional projection", interactive=False)
    with gr.Tab("Category summary"):
        category_output = gr.Dataframe(label="Category performance", interactive=False)
    with gr.Tab("Association rules"):
        rules_output = gr.Dataframe(label="Apriori product association rules", interactive=False)

    outputs = [summary_output, cluster_output, pca_output, category_output, rules_output]
    inputs = [file_input, cluster_input, support_input, confidence_input]
    analyze_button.click(fn=analyze_ecommerce, inputs=inputs, outputs=outputs)
    app.load(fn=analyze_ecommerce, inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    app.launch()
