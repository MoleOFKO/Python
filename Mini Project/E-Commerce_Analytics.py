from itertools import combinations

import gradio as gr
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {
    "Order_ID", "Order_Date", "Customer_ID", "Category", "Product",
    "Quantity", "Unit_Price", "Discount", "Region",
}
NUMERIC_FEATURES = ["Quantity", "Unit_Price", "Discount", "Revenue"]


SAMPLE_DATA = pd.DataFrame([
    {"Order_ID": 1001, "Order_Date": "2025-01-05", "Customer_ID": "C001", "Category": "Electronics", "Product": "Headphones", "Quantity": 2, "Unit_Price": 45, "Discount": 0.10, "Region": "North"},
    {"Order_ID": 1002, "Order_Date": "2025-01-12", "Customer_ID": "C002", "Category": "Home", "Product": "Desk Lamp", "Quantity": 1, "Unit_Price": 35, "Discount": 0.00, "Region": "South"},
    {"Order_ID": 1003, "Order_Date": "2025-01-18", "Customer_ID": "C003", "Category": "Fashion", "Product": "T-Shirt", "Quantity": 3, "Unit_Price": 22, "Discount": 0.05, "Region": "East"},
    {"Order_ID": 1004, "Order_Date": "2025-02-03", "Customer_ID": "C001", "Category": "Electronics", "Product": "Keyboard", "Quantity": 1, "Unit_Price": 70, "Discount": 0.15, "Region": "North"},
    {"Order_ID": 1005, "Order_Date": "2025-02-11", "Customer_ID": "C004", "Category": "Beauty", "Product": "Skincare Set", "Quantity": 2, "Unit_Price": 30, "Discount": 0.10, "Region": "West"},
    {"Order_ID": 1006, "Order_Date": "2025-02-20", "Customer_ID": "C005", "Category": "Home", "Product": "Coffee Maker", "Quantity": 1, "Unit_Price": 85, "Discount": 0.00, "Region": "South"},
    {"Order_ID": 1007, "Order_Date": "2025-03-02", "Customer_ID": "C006", "Category": "Fashion", "Product": "Jeans", "Quantity": 2, "Unit_Price": 55, "Discount": 0.05, "Region": "East"},
    {"Order_ID": 1008, "Order_Date": "2025-03-15", "Customer_ID": "C002", "Category": "Electronics", "Product": "Mouse", "Quantity": 3, "Unit_Price": 25, "Discount": 0.00, "Region": "North"},
    {"Order_ID": 1009, "Order_Date": "2025-03-22", "Customer_ID": "C007", "Category": "Beauty", "Product": "Face Cream", "Quantity": 1, "Unit_Price": 28, "Discount": 0.10, "Region": "West"},
    {"Order_ID": 1010, "Order_Date": "2025-04-04", "Customer_ID": "C008", "Category": "Home", "Product": "Cushion", "Quantity": 2, "Unit_Price": 18, "Discount": 0.05, "Region": "South"},
    {"Order_ID": 1011, "Order_Date": "2025-04-12", "Customer_ID": "C009", "Category": "Fashion", "Product": "Sneakers", "Quantity": 1, "Unit_Price": 75, "Discount": 0.15, "Region": "East"},
    {"Order_ID": 1012, "Order_Date": "2025-04-25", "Customer_ID": "C003", "Category": "Electronics", "Product": "Monitor", "Quantity": 1, "Unit_Price": 240, "Discount": 0.10, "Region": "North"},
    {"Order_ID": 1013, "Order_Date": "2025-05-06", "Customer_ID": "C010", "Category": "Beauty", "Product": "Shampoo", "Quantity": 3, "Unit_Price": 20, "Discount": 0.00, "Region": "West"},
    {"Order_ID": 1014, "Order_Date": "2025-05-14", "Customer_ID": "C011", "Category": "Home", "Product": "Table Organizer", "Quantity": 2, "Unit_Price": 32, "Discount": 0.05, "Region": "South"},
    {"Order_ID": 1015, "Order_Date": "2025-05-28", "Customer_ID": "C012", "Category": "Fashion", "Product": "Jacket", "Quantity": 1, "Unit_Price": 90, "Discount": 0.10, "Region": "East"},
    {"Order_ID": 1016, "Order_Date": "2025-06-07", "Customer_ID": "C004", "Category": "Electronics", "Product": "Webcam", "Quantity": 2, "Unit_Price": 65, "Discount": 0.00, "Region": "North"},
    {"Order_ID": 1017, "Order_Date": "2025-06-16", "Customer_ID": "C013", "Category": "Beauty", "Product": "Perfume", "Quantity": 1, "Unit_Price": 60, "Discount": 0.15, "Region": "West"},
    {"Order_ID": 1018, "Order_Date": "2025-06-23", "Customer_ID": "C014", "Category": "Home", "Product": "Vacuum Cleaner", "Quantity": 1, "Unit_Price": 150, "Discount": 0.05, "Region": "South"},
    {"Order_ID": 1019, "Order_Date": "2025-07-03", "Customer_ID": "C015", "Category": "Fashion", "Product": "Dress", "Quantity": 2, "Unit_Price": 80, "Discount": 0.10, "Region": "East"},
    {"Order_ID": 1020, "Order_Date": "2025-07-18", "Customer_ID": "C005", "Category": "Electronics", "Product": "Tablet", "Quantity": 1, "Unit_Price": 320, "Discount": 0.20, "Region": "North"},
    {"Order_ID": 1021, "Order_Date": "2025-01-28", "Customer_ID": "C016", "Category": "Electronics", "Product": "Bluetooth Speaker", "Quantity": 2, "Unit_Price": 58, "Discount": 0.08, "Region": "West"},
    {"Order_ID": 1022, "Order_Date": "2025-02-06", "Customer_ID": "C017", "Category": "Home", "Product": "Air Fryer", "Quantity": 1, "Unit_Price": 120, "Discount": 0.12, "Region": "North"},
    {"Order_ID": 1023, "Order_Date": "2025-02-18", "Customer_ID": "C018", "Category": "Fashion", "Product": "Running Shoes", "Quantity": 2, "Unit_Price": 68, "Discount": 0.20, "Region": "East"},
    {"Order_ID": 1024, "Order_Date": "2025-03-05", "Customer_ID": "C019", "Category": "Beauty", "Product": "Hair Dryer", "Quantity": 1, "Unit_Price": 42, "Discount": 0.05, "Region": "South"},
    {"Order_ID": 1025, "Order_Date": "2025-03-19", "Customer_ID": "C020", "Category": "Electronics", "Product": "Wireless Charger", "Quantity": 3, "Unit_Price": 18, "Discount": 0.00, "Region": "West"},
    {"Order_ID": 1026, "Order_Date": "2025-04-08", "Customer_ID": "C021", "Category": "Home", "Product": "Storage Bin", "Quantity": 4, "Unit_Price": 14, "Discount": 0.10, "Region": "North"},
    {"Order_ID": 1027, "Order_Date": "2025-04-15", "Customer_ID": "C022", "Category": "Fashion", "Product": "Sunglasses", "Quantity": 1, "Unit_Price": 40, "Discount": 0.25, "Region": "East"},
    {"Order_ID": 1028, "Order_Date": "2025-04-30", "Customer_ID": "C023", "Category": "Beauty", "Product": "Body Lotion", "Quantity": 2, "Unit_Price": 26, "Discount": 0.05, "Region": "South"},
    {"Order_ID": 1029, "Order_Date": "2025-05-09", "Customer_ID": "C024", "Category": "Electronics", "Product": "Laptop Stand", "Quantity": 1, "Unit_Price": 55, "Discount": 0.00, "Region": "West"},
    {"Order_ID": 1030, "Order_Date": "2025-05-20", "Customer_ID": "C025", "Category": "Home", "Product": "Throw Blanket", "Quantity": 2, "Unit_Price": 36, "Discount": 0.15, "Region": "North"},
    {"Order_ID": 1031, "Order_Date": "2025-06-04", "Customer_ID": "C026", "Category": "Fashion", "Product": "Coat", "Quantity": 1, "Unit_Price": 125, "Discount": 0.10, "Region": "East"},
    {"Order_ID": 1032, "Order_Date": "2025-06-14", "Customer_ID": "C027", "Category": "Beauty", "Product": "Face Serum", "Quantity": 2, "Unit_Price": 33, "Discount": 0.18, "Region": "South"},
    {"Order_ID": 1033, "Order_Date": "2025-06-28", "Customer_ID": "C028", "Category": "Electronics", "Product": "Smart Watch", "Quantity": 1, "Unit_Price": 210, "Discount": 0.05, "Region": "West"},
    {"Order_ID": 1034, "Order_Date": "2025-07-08", "Customer_ID": "C029", "Category": "Home", "Product": "Dining Set", "Quantity": 1, "Unit_Price": 180, "Discount": 0.20, "Region": "North"},
    {"Order_ID": 1035, "Order_Date": "2025-07-22", "Customer_ID": "C030", "Category": "Fashion", "Product": "Hoodie", "Quantity": 3, "Unit_Price": 48, "Discount": 0.10, "Region": "East"},
    {"Order_ID": 1036, "Order_Date": "2025-08-02", "Customer_ID": "C001", "Category": "Beauty", "Product": "Sunscreen", "Quantity": 2, "Unit_Price": 22, "Discount": 0.00, "Region": "West"},
    {"Order_ID": 1037, "Order_Date": "2025-08-07", "Customer_ID": "C003", "Category": "Electronics", "Product": "Camera", "Quantity": 1, "Unit_Price": 310, "Discount": 0.15, "Region": "North"},
    {"Order_ID": 1038, "Order_Date": "2025-08-13", "Customer_ID": "C006", "Category": "Home", "Product": "Bedding Set", "Quantity": 2, "Unit_Price": 72, "Discount": 0.12, "Region": "South"},
    {"Order_ID": 1039, "Order_Date": "2025-08-19", "Customer_ID": "C009", "Category": "Fashion", "Product": "Sandals", "Quantity": 3, "Unit_Price": 29, "Discount": 0.05, "Region": "East"},
    {"Order_ID": 1040, "Order_Date": "2025-08-25", "Customer_ID": "C022", "Category": "Electronics", "Product": "Gaming Mouse", "Quantity": 2, "Unit_Price": 52, "Discount": 0.08, "Region": "West"},
    {"Order_ID": 1041, "Order_Date": "2025-08-28", "Customer_ID": "C010", "Category": "Beauty", "Product": "Nail Kit", "Quantity": 1, "Unit_Price": 19, "Discount": 0.00, "Region": "North"},
    {"Order_ID": 1042, "Order_Date": "2025-09-03", "Customer_ID": "C014", "Category": "Home", "Product": "Plant Pot", "Quantity": 3, "Unit_Price": 16, "Discount": 0.10, "Region": "South"},
    {"Order_ID": 1043, "Order_Date": "2025-09-10", "Customer_ID": "C019", "Category": "Fashion", "Product": "Polo Shirt", "Quantity": 2, "Unit_Price": 35, "Discount": 0.05, "Region": "East"},
    {"Order_ID": 1044, "Order_Date": "2025-09-16", "Customer_ID": "C024", "Category": "Electronics", "Product": "USB Hub", "Quantity": 4, "Unit_Price": 24, "Discount": 0.10, "Region": "West"},
    {"Order_ID": 1045, "Order_Date": "2025-09-21", "Customer_ID": "C017", "Category": "Beauty", "Product": "Lip Balm", "Quantity": 5, "Unit_Price": 9, "Discount": 0.00, "Region": "North"},
    {"Order_ID": 1046, "Order_Date": "2025-09-26", "Customer_ID": "C028", "Category": "Home", "Product": "Wall Clock", "Quantity": 1, "Unit_Price": 28, "Discount": 0.15, "Region": "South"},
    {"Order_ID": 1047, "Order_Date": "2025-10-01", "Customer_ID": "C016", "Category": "Electronics", "Product": "Headphones", "Quantity": 1, "Unit_Price": 45, "Discount": 0.10, "Region": "West"},
    {"Order_ID": 1048, "Order_Date": "2025-10-04", "Customer_ID": "C016", "Category": "Electronics", "Product": "Keyboard", "Quantity": 1, "Unit_Price": 70, "Discount": 0.15, "Region": "West"},
    {"Order_ID": 1049, "Order_Date": "2025-10-07", "Customer_ID": "C016", "Category": "Electronics", "Product": "Mouse", "Quantity": 2, "Unit_Price": 25, "Discount": 0.00, "Region": "West"},
    {"Order_ID": 1050, "Order_Date": "2025-10-09", "Customer_ID": "C024", "Category": "Electronics", "Product": "Headphones", "Quantity": 1, "Unit_Price": 45, "Discount": 0.05, "Region": "West"},
    {"Order_ID": 1051, "Order_Date": "2025-10-12", "Customer_ID": "C024", "Category": "Electronics", "Product": "Keyboard", "Quantity": 1, "Unit_Price": 70, "Discount": 0.10, "Region": "West"},
    {"Order_ID": 1052, "Order_Date": "2025-10-15", "Customer_ID": "C024", "Category": "Electronics", "Product": "Webcam", "Quantity": 1, "Unit_Price": 65, "Discount": 0.00, "Region": "West"},
    {"Order_ID": 1053, "Order_Date": "2025-10-18", "Customer_ID": "C018", "Category": "Fashion", "Product": "T-Shirt", "Quantity": 2, "Unit_Price": 22, "Discount": 0.10, "Region": "East"},
    {"Order_ID": 1054, "Order_Date": "2025-10-20", "Customer_ID": "C018", "Category": "Fashion", "Product": "Jeans", "Quantity": 1, "Unit_Price": 55, "Discount": 0.05, "Region": "East"},
    {"Order_ID": 1055, "Order_Date": "2025-10-23", "Customer_ID": "C018", "Category": "Fashion", "Product": "Sneakers", "Quantity": 1, "Unit_Price": 75, "Discount": 0.15, "Region": "East"},
    {"Order_ID": 1056, "Order_Date": "2025-10-25", "Customer_ID": "C022", "Category": "Fashion", "Product": "T-Shirt", "Quantity": 2, "Unit_Price": 22, "Discount": 0.05, "Region": "East"},
    {"Order_ID": 1057, "Order_Date": "2025-10-28", "Customer_ID": "C022", "Category": "Fashion", "Product": "Sunglasses", "Quantity": 1, "Unit_Price": 40, "Discount": 0.20, "Region": "East"},
    {"Order_ID": 1058, "Order_Date": "2025-10-30", "Customer_ID": "C022", "Category": "Fashion", "Product": "Sneakers", "Quantity": 1, "Unit_Price": 75, "Discount": 0.10, "Region": "East"},
], columns=["Order_ID", "Order_Date", "Customer_ID", "Category", "Product", "Quantity", "Unit_Price", "Discount", "Region"])


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
        return pd.DataFrame([
            {
                "Rule": "No strong association rules found for current thresholds",
                "Support": None,
                "Confidence": None,
                "Lift": None,
            }
        ])
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
    return dashboard, cluster_results, pca_results, category_results, rules


APP_CSS = """
.gradio-container { max-width: 1240px !important; background: #f4f7f6; }
.app-header { padding: 18px 2px 10px; }
.app-header h1 { color: #123b3a; font-size: 36px; letter-spacing: -1px; margin: 5px 0; }
.app-header p { color: #55706e; font-size: 15px; margin: 0; }
.eyebrow, .panel-label { color: #2f7770; font-size: 11px; font-weight: 700; letter-spacing: 1.4px; }
.dashboard { background: #ffffff; border: 1px solid #dbe7e4; border-radius: 14px; padding: 24px; margin: 18px 0; box-shadow: 0 8px 24px rgba(18, 59, 58, .06); }
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


with gr.Blocks(title="E-Commerce Analytics", css=APP_CSS, theme=gr.themes.Soft(primary_hue="teal", neutral_hue="slate")) as app:
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
            support_input = gr.Slider(0.05, 0.50, value=0.10, step=0.05, label="Support", info="Apriori minimum")
            confidence_input = gr.Slider(0.10, 1.00, value=0.30, step=0.05, label="Confidence", info="Apriori minimum")

    summary_output = gr.HTML()
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
