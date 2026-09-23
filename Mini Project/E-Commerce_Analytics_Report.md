# E-Commerce Analytics Project Report

## 1. Project Overview

This project analyzes e-commerce transaction data through one executable Python file with a Gradio interface. The application supports CSV loading, preprocessing, customer/order clustering, dimensionality reduction, anomaly detection, and association rule learning.

Main files:

- `E-Commerce_Analytics.py`: complete analytics application and Gradio UI
- `e_commerce_example.csv`: example input dataset

## 2. Objectives

The project was created to:

1. Load and validate e-commerce transaction data.
2. Calculate transaction revenue after discounts.
3. Group similar transactions with K-Means clustering.
4. Reduce numeric features to two dimensions using PCA.
5. Detect unusual transactions using standardized distance scores.
6. Discover product associations using Apriori rules.
7. Display the results through a Gradio web interface.

## 3. Dataset

The example dataset contains 20 transactions, 15 customers, 20 products, and four product categories.

Required columns:

| Column | Description |
|---|---|
| `Order_ID` | Unique order identifier |
| `Order_Date` | Date of the order |
| `Customer_ID` | Customer identifier |
| `Category` | Product category |
| `Product` | Product name |
| `Quantity` | Number of units purchased |
| `Unit_Price` | Price per unit before discount |
| `Discount` | Discount as a decimal from 0 to 1 |
| `Region` | Customer or order region |

Revenue is calculated as:

```text
Revenue = Quantity * Unit_Price * (1 - Discount)
```

## 4. Methods

### Data Loading and Preprocessing

The application can use the included sample data or an uploaded CSV file. It validates required columns, converts dates, converts numeric fields, limits discounts to the range 0 to 1, rejects invalid dates or prices, and calculates revenue.

### K-Means Clustering

The numeric features used for clustering are:

- Quantity
- Unit price
- Discount
- Revenue

The features are standardized before K-Means is applied. The number of clusters can be selected in the Gradio interface. The default is three clusters.

### Principal Component Analysis

PCA is calculated from the standardized numeric features using the covariance matrix and eigenvectors. The first two principal components are displayed in the dimensionality-reduction table.

For the example data, the first two components explain approximately 62.7% and 24.1% of the variance, or 86.8% combined.

### Anomaly Detection

Each transaction receives a standardized Euclidean distance score. Transactions at or above the 95th percentile are marked as anomalies.

### Association Rule Learning

The application groups products by customer and uses an Apriori-style process to find frequent itemsets. Rules are ranked using support, confidence, and lift. Minimum support and minimum confidence can be changed in the interface.

## 5. Example Results

| Metric | Result |
|---|---:|
| Total revenue | $1,821.15 |
| Total orders | 20 |
| Items sold | 33 |
| Customers | 15 |
| Number of clusters | 3 |
| PCA variance explained | 86.8% for first two components |
| Anomalies detected | 1 |
| Association rules at default thresholds | 0 |

### Cluster Distribution

| Cluster | Transactions |
|---|---:|
| Cluster 1 | 9 |
| Cluster 2 | 9 |
| Cluster 3 | 2 |

### Detected Anomaly

The transaction identified as an anomaly is:

| Order ID | Product | Revenue | Anomaly score |
|---:|---|---:|---:|
| 1020 | Tablet | $256.00 | 4.868 |

This result is reasonable because the tablet transaction has a high price and relatively high discounted revenue compared with most other example transactions.

### Category Performance

| Category | Orders | Units sold | Revenue |
|---|---:|---:|---:|
| Electronics | 6 | 10 | $817.50 |
| Fashion | 5 | 9 | $455.95 |
| Home | 5 | 7 | $357.50 |
| Beauty | 4 | 7 | $190.20 |

Electronics generated the highest revenue in the example dataset.

## 6. How to Run

Install the required packages if they are not already installed:

```powershell
pip install numpy pandas gradio
```

Start the application from the project root:

```powershell
python "Mini Project/E-Commerce_Analytics.py"
```

The application opens a local Gradio URL. The user can either analyze the built-in sample data or upload `e_commerce_example.csv`.

## 7. Interpretation

The example data shows that Electronics is the strongest revenue category. The clustering output separates transactions according to their standardized quantity, price, discount, and revenue patterns. PCA provides a two-dimensional view of those relationships. The anomaly detector highlights the high-value Tablet order for further review.

No association rules are shown with the default thresholds because the example dataset has too few repeated product combinations within customer baskets. A larger transaction history with customers buying multiple recurring product combinations would produce more useful rules.

## 8. Limitations and Future Improvements

- K-Means results depend on the selected number of clusters and feature selection.
- The anomaly detector uses a simple percentile distance threshold rather than a supervised fraud label.
- Association rules require a larger basket-oriented dataset for reliable recommendations.
- The current report displays tables; future work could add interactive charts for clusters, PCA, revenue trends, and anomalies.
- Product and customer names in a real dataset should be reviewed for privacy before sharing results.
