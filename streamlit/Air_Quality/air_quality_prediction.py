#import libraries
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

#Create Air Quality Dataset
data = {
    "Temperature": [
        20, 22, 25, 28, 30,
        32, 35, 27, 24, 31,
        29, 26, 33, 26, 23,
        21, 34, 30, 28, 25
    ],
    "PM2.5": [
        10, 15, 20, 35, 45,
        60, 75, 30, 18, 55,
        40, 25, 70, 85, 12,
        8, 65, 50, 32, 22
    ],
    "RM10": [
        20, 30, 40, 60, 80,
        100, 120, 50, 35, 90,
        70, 45, 110, 130, 25,
        15, 105, 85, 58, 42
    ],
    "AQI": [
        25, 35, 50, 75, 100,
        125, 150, 60, 40, 110,
        90, 55, 140, 160, 30,
        20, 130, 95, 70, 45
    ]
}

#Convert dictionary to DataFrame
df = pd.DataFrame(data)

#Display dataset
print(df.head())

#Read CSV
df = pd.read_csv("air_quality.csv")

#Display complete dataset
print(df)

#Data Cleaning

#Check missing values
print("Missing Values : ")
print(df.isnull().sum())

#Check duplicate values
print("Duplicate Values : ")
print(df.duplicated().sum())

#remove duplicate rows
df = df.drop_duplicates()

print("Data Cleaning Complete!")


#Data Visualization
#Line Chart

plt.figure(figsize=(10, 5))
plt.plot(df["AQI"], marker="o")
plt.title("AQI Trend")
plt.xlabel("Record")
plt.ylabel("AQI")

plt.show()