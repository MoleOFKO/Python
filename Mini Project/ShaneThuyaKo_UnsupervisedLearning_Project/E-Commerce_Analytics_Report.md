# E-Commerce Analytics Project Report

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

The example dataset includes 58 transaction records, 30 customers, 4 product categories, and repeated purchase patterns that are strong enough to support association-rule mining. It contains transaction-level details essential for retail and customer behavior analysis.

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
| Total revenue | $4,635.99 |
| Total orders | 58 |
| Items sold | 101 |
| Customers | 30 |
| Number of clusters | 3 |
| PCA variance explained | 86.8% for first two components |
| Anomalies detected | 1 |
| Association rules at default thresholds | 4 |

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

| Category | Orders | Units Sold | Revenue |
|---|---:|---:|---:|
| Electronics | 19 | 35 | $1,999.05 |
| Fashion | 17 | 30 | $1,282.90 |
| Home | 12 | 21 | $912.42 |
| Beauty | 10 | 15 | $441.62 |

## 6. Interpretation of Findings

The results suggest that customer purchases vary meaningfully by product category, transaction value, and discount behavior. The clustering output indicates that transactions are not homogeneous; instead, they form groups with distinct purchasing patterns. PCA further supports this conclusion by showing that a large proportion of the variation in the data can be summarized using just two components.

The anomaly detection process successfully identified a transaction with unusually high revenue relative to the rest of the dataset. This is useful for highlighting potential outliers or large-value purchases that may deserve additional investigation.

The dataset contains enough repeated co-purchase patterns to produce four meaningful association rules. The strongest rules are the reciprocal electronics cross-sell patterns between Headphones and Keyboard, followed by the fashion pair Sneakers and T-Shirt. These results indicate that customers who buy one item in a pair are likely to purchase the related item, which supports cross-selling and bundle recommendation strategies.

### 5.5 Association Rule Results

| Antecedent | Consequent | Support | Confidence | Lift |
|---|---|---:|---:|---:|
| Headphones | Keyboard | 0.100 | 1.000 | 10.000 |
| Keyboard | Headphones | 0.100 | 1.000 | 10.000 |
| Sneakers | T-Shirt | 0.067 | 0.667 | 6.667 |
| T-Shirt | Sneakers | 0.067 | 0.667 | 6.667 |

These rules suggest that a strong recommendation strategy could pair Headphones with Keyboard and position Sneakers with T-Shirt in promotional bundles or related-product sections. The confidence and lift values show that the co-purchase patterns are not random and are useful for retail recommendation logic.

## 7. Limitations and Future Improvements

Several limitations should be acknowledged when interpreting the results:

- K-Means clustering depends on the selected number of clusters and the chosen features.
- The anomaly detector relies on a percentile-based distance threshold rather than labeled fraud or irregularity data.
- Association rule mining still depends on enough repeated customer purchase combinations to produce stable recommendations.
- The current analysis is based on a sample dataset and may not fully represent broader consumer behavior.
- A more advanced implementation could include interactive charts, trend analysis, and a richer dashboard for presentation.

Overall, the project demonstrates how data analysis techniques can be applied to e-commerce sales data to uncover meaningful patterns in customer spending, product performance, and unusual purchase behavior. The results provide a solid foundation for further development in business intelligence and retail analytics.

