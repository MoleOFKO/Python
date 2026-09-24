# E-Commerce Analytics Project Report

## 1. Executive Summary

This project provides a Gradio application for exploring e-commerce transactions with five complementary techniques: data validation, revenue calculation, K-Means clustering, Principal Component Analysis (PCA), anomaly detection, and Apriori-style association rules.

The verified default run uses the application's built-in sample data. It contains 20 transactions from 15 customers. The transactions generate $1,821.15 in discounted revenue from 33 units. Electronics is the strongest category by revenue, the first two PCA components explain 86.8% of standardized feature variance, and one transaction is flagged by the 95th-percentile anomaly rule.

The results are exploratory rather than predictive. The sample is small, and the clustering, anomaly, and association-rule outputs depend directly on the selected settings and the data uploaded by the user.

## 2. Objectives

The application is designed to:

- validate the columns and numeric fields required for analysis;
- calculate transaction revenue after discounts;
- group similar transactions using standardized numeric features;
- project those features into two dimensions for visualization;
- identify transactions with unusually large standardized distances; and
- find product co-occurrence rules within customer purchase baskets.

## 3. Data and Revenue Calculation

The built-in sample contains 20 rows dated from January through July 2025. It includes 15 customers, 18 distinct product labels across the transaction rows, four categories, and four regions. Uploaded CSV files must include the following columns:

| Column | Purpose |
|---|---|
| `Order_ID` | Order identifier |
| `Order_Date` | Transaction date |
| `Customer_ID` | Customer basket identifier |
| `Category` | Product category |
| `Product` | Product name |
| `Quantity` | Units purchased |
| `Unit_Price` | Price before discount |
| `Discount` | Decimal discount between 0 and 1 |
| `Region` | Order or customer region |

Dates and numeric fields are converted during loading. Discounts are filled with zero when missing and clipped to the range 0 to 1. Invalid dates, quantities, or unit prices cause validation to fail. Revenue is calculated as:

```text
Revenue = Quantity * Unit_Price * (1 - Discount)
```

## 4. Analytical Methodology

### 4.1 Feature Preparation

The model features are `Quantity`, `Unit_Price`, `Discount`, and calculated `Revenue`. Each feature is standardized with its mean and standard deviation. A zero standard deviation is replaced with 1 so that a constant feature does not cause division-by-zero errors.

### 4.2 Deterministic K-Means

K-Means is applied to the standardized transaction features. The application defaults to three clusters and allows the user to select between two and six. Initial centroids are selected from evenly spaced rows rather than randomly, making a given input and setting reproducible. Centroids are updated for at most 100 iterations, and empty clusters retain their previous centroid.

### 4.3 PCA Visualization

PCA is implemented with the covariance matrix and its eigenvectors. The standardized four-feature data is projected onto the two eigenvectors with the largest eigenvalues. These two components are used in the scatter plot and in the PCA output table.

### 4.4 Distance-Based Anomaly Detection

For each transaction, the application calculates the Euclidean distance of its standardized feature vector from the standardized origin:

```text
Anomaly score = sqrt(z_Quantity^2 + z_Unit_Price^2 + z_Discount^2 + z_Revenue^2)
```

Rows whose score is greater than or equal to the 95th percentile are marked `Yes`. This is a statistical outlier flag, not a fraud or error diagnosis.

### 4.5 Association Rules

Products are converted into one set per customer, so repeated purchases of the same product by one customer count once in that basket. The application then generates frequent itemsets and evaluates rules with support, confidence, and lift. The UI defaults are minimum support 0.05 and minimum confidence 0.30.

## 5. Verified Results from the Built-In Sample

### 5.1 Overall Metrics

| Metric | Result |
|---|---:|
| Transactions | 20 |
| Unique customers | 15 |
| Units sold | 33 |
| Net revenue after discounts | $1,821.15 |
| Average revenue per transaction | $91.06 |
| K-Means clusters | 3 |
| PCA variance in first two components | 86.8% |
| Anomalies flagged | 1 |
| Association rules at default thresholds | 8 |

### 5.2 Category Performance

| Category | Orders | Units sold | Revenue |
|---|---:|---:|---:|
| Electronics | 6 | 10 | $817.50 |
| Fashion | 5 | 9 | $455.95 |
| Home | 5 | 7 | $357.50 |
| Beauty | 4 | 7 | $190.20 |

Electronics contributes approximately 44.9% of total revenue and leads the other categories by a substantial margin. Beauty has the lowest revenue in this sample. These are revenue comparisons, not profit comparisons, because the dataset does not include product cost or margin.

### 5.3 Cluster Distribution

| Cluster | Transactions |
|---|---:|
| Cluster 1 | 9 |
| Cluster 2 | 9 |
| Cluster 3 | 2 |

The result shows two large groups and one small group of transactions. The labels themselves do not represent a business ranking; K-Means cluster numbers are identifiers assigned by the implementation. Interpreting the groups requires reviewing the transaction-level output and feature values rather than relying on the label number alone.

### 5.4 Anomaly Result

| Order ID | Customer | Product | Revenue | Score |
|---:|---|---|---:|---:|
| 1020 | C005 | Headphones | $256.00 | 4.868 |

Order 1020 is flagged because its combined standardized quantity, price, discount, and revenue profile is far from the center of the sample. The flag should be reviewed as a high-value or unusual transaction, not automatically treated as an error.

### 5.5 Association-Rule Results

The default settings produce eight directed rules:

| Rule | Support | Confidence | Lift |
|---|---:|---:|---:|
| Webcam -> Skincare Set | 0.067 | 1.000 | 15.0 |
| Skincare Set -> Webcam | 0.067 | 1.000 | 15.0 |
| Mouse -> Desk Lamp | 0.067 | 1.000 | 15.0 |
| Desk Lamp -> Mouse | 0.067 | 1.000 | 15.0 |
| Coffee Maker -> Headphones | 0.067 | 1.000 | 7.5 |
| Headphones -> Coffee Maker | 0.067 | 0.500 | 7.5 |
| Headphones -> Keyboard | 0.067 | 0.500 | 7.5 |
| Keyboard -> Headphones | 0.067 | 1.000 | 7.5 |

The high lift values are driven by rare co-occurrences in only 15 customer baskets. They are useful leads for investigation, but they are not reliable recommendations until confirmed on a much larger transaction history.

## 6. Interpretation

The sample has meaningful variation in transaction value and product behavior: PCA compresses most of the standardized variation into two dimensions, while K-Means separates the transactions into three reproducible groups. Electronics is the main revenue contributor, and order 1020 is the clearest multivariate outlier under the application's distance rule.

The association results indicate a few repeated customer-level product combinations, but their low support of 0.067 means each pattern is present in approximately one of the 15 customer baskets. The rules should therefore be treated as hypotheses for merchandising or bundle testing rather than established customer behavior.

## 7. Limitations and Recommendations

- The sample has only 20 transactions and 15 customers, so results may change considerably with additional data.
- K-Means requires a chosen cluster count and is sensitive to the selected features and initialization strategy.
- The implementation does not calculate validation measures such as silhouette score or compare multiple cluster counts.
- The anomaly method uses a fixed percentile of standardized distance and has no labeled normal or abnormal outcomes.
- Association rules use customer-level sets, which remove purchase frequency and order sequence information.
- Support and confidence are rounded in the displayed table, and rare rules can appear stronger than they are in a small sample.
- Revenue is not profit because product cost, shipping, returns, and taxes are not included.
- Uploaded data should be checked for duplicate orders, negative quantities, currency consistency, and data-entry errors before business decisions are made.

Future work should evaluate the methods on a larger historical dataset, add cluster-quality metrics, analyze revenue over time and by region, include margins and returns, and validate association rules on a holdout period. The current Gradio interface is a useful exploratory foundation for that work.

## 1. Project Overview

This project focuses on analyzing e-commerce transaction data to extract meaningful business insights from customer purchases, product categories, pricing patterns, and transaction behavior. The analysis was implemented in a Python application that integrates data preprocessing, clustering, dimensionality reduction, anomaly detection, and association-rule learning in a single workflow.

The study uses a sample e-commerce dataset containing transaction records across multiple product categories and customer segments. The objective is to understand buying patterns, identify high-value transactions, and evaluate how transactional features relate to one another in a structured data-driven manner.

## 2. Objectives

The project was designed to investigate several key aspects of the dataset, including:

- validating and cleaning transaction records;
- calculating revenue after discounts;
- identifying similarities among transactions using clustering techniques;
- reducing the dimensionality of transaction features for visualization;
- detecting unusual purchase patterns through anomaly detection;
- exploring possible product associations using association-rule mining.

## 3. Dataset Description

The example dataset includes 20 transactions, 15 customers, 20 products, and four product categories. It contains transaction-level details essential for retail and customer behavior analysis.

The required fields in the dataset are:

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Date of the order |
| Customer_ID | Customer identifier |
| Category | Product category |
| Product | Product name |
| Quantity | Number of units purchased |
| Unit_Price | Price per unit before discount |
| Discount | Discount as a decimal between 0 and 1 |
| Region | Customer or order region |

The revenue for each transaction was computed using the formula:

```text
Revenue = Quantity * Unit_Price * (1 - Discount)
```

## 4. Methodology

### 4.1 Data Preprocessing

The dataset was loaded and validated to ensure consistency and reliability. Empty or missing values, invalid dates, incorrect numeric formats, and discounts outside the acceptable range were identified and handled. After preprocessing, revenue was calculated for each transaction to create a more informative analysis variable.

### 4.2 K-Means Clustering

A K-Means clustering model was applied to the standardized transaction features, including quantity, unit price, discount, and revenue. Standardization was necessary to ensure that features with different scales contributed fairly to the clustering process. The model grouped transactions into clusters based on similarity in purchasing and pricing behavior.

### 4.3 Principal Component Analysis (PCA)

Principal Component Analysis was used to reduce the dimensionality of the standardized feature set into two principal components. This allowed the dataset to be visualized in a lower-dimensional space while preserving as much variance as possible. The first two components explained approximately 86.8% of the total variance, indicating that the reduced representation captured most of the underlying structure in the data.

### 4.4 Anomaly Detection

An anomaly detection approach based on standardized Euclidean distance was applied to identify unusually high-value or irregular transactions. Transactions above the 95th percentile of the distance score were marked as anomalies, which helped highlight transactions that departed significantly from the typical purchasing pattern.

### 4.5 Association Rule Learning

Association rule analysis was conducted to identify product combinations that frequently appeared together within customer baskets. Using an Apriori-style method, rules were evaluated based on support, confidence, and lift to determine whether certain products tended to be purchased together.

## 5. Results and Analysis

### 5.1 Overall Transaction Summary

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

### 5.2 Cluster Distribution

| Cluster | Transactions |
|---|---:|
| Cluster 1 | 9 |
| Cluster 2 | 9 |
| Cluster 3 | 2 |

The clustering results suggest that the dataset contains three noticeable transaction groups with different purchase patterns. The distribution indicates that most transactions fall into two larger clusters, while a smaller cluster contains transactions with more distinct characteristics.

### 5.3 Anomaly Identification

The anomaly detected in the dataset was a high-value tablet order:

| Order ID | Product | Revenue | Anomaly Score |
|---:|---|---:|---:|
| 1020 | Tablet | $256.00 | 4.868 |

This transaction stands out because it combines a relatively high unit price with a large discounted revenue contribution. The anomaly score indicates that it deviates significantly from the general pattern of the dataset and may warrant further review.

### 5.4 Category Performance

| Category | Orders | Units Sold | Revenue |
|---|---:|---:|---:|
| Electronics | 6 | 10 | $817.50 |
| Fashion | 5 | 9 | $455.95 |
| Home | 5 | 7 | $357.50 |
| Beauty | 4 | 7 | $190.20 |

The category analysis shows that Electronics generated the highest total revenue, followed by Fashion, Home, and Beauty. This suggests that electronic products contribute the most value in the sample dataset and are likely the most profitable category overall.

## 6. Interpretation of Findings

The results suggest that customer purchases vary meaningfully by product category, transaction value, and discount behavior. The clustering output indicates that transactions are not homogeneous; instead, they form groups with distinct purchasing patterns. PCA further supports this conclusion by showing that a large proportion of the variation in the data can be summarized using just two components.

The anomaly detection process successfully identified a transaction with unusually high revenue relative to the rest of the dataset. This is useful for highlighting potential outliers or large-value purchases that may deserve additional investigation.

The absence of strong association rules at the default thresholds indicates that there are not enough repeated product combinations within customer baskets to produce meaningful recommendations. This is common in small or sparse transaction datasets, where repeated co-purchase patterns are limited.

## 7. Limitations and Future Improvements

Several limitations should be acknowledged when interpreting the results:

- K-Means clustering depends on the selected number of clusters and the chosen features.
- The anomaly detector relies on a percentile-based distance threshold rather than labeled fraud or irregularity data.
- Association rule mining requires a larger dataset with more repeated customer purchase combinations to produce robust recommendations.
- The current analysis is based on a small sample and may not fully represent broader consumer behavior.
- A more advanced implementation could include interactive charts, trend analysis, and a richer dashboard for presentation.

Overall, the project demonstrates how data analysis techniques can be applied to e-commerce sales data to uncover meaningful patterns in customer spending, product performance, and unusual purchase behavior. The results provide a solid foundation for further development in business intelligence and retail analytics.

