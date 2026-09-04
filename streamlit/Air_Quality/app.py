#1. import laibraries
from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import(
    mean_absolute_error, 
    mean_squared_error, 
    r2_score
)

#2. streamlit page setting
st.set_page_config(
    page_title="Air Quality Prediction",
    page_icon="🌬️",
    layout="wide"
)

#3. Title
st.title("🚑Air Quality Prediction System🚑")
st.write("This application used Machine Learning to predict Air Quality Index (AQI) from Temperature, PM2.5 and RM10 values.")

#4. Load CSV Dataset
csv_path = Path(__file__).resolve().parent / "air_quality.csv"
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error("air_quality.csv is not found!")
    st.stop()

#5. Data Cleaning rows
df = df.drop_duplicates()

#Remove rows containing missing values
df = df.dropna()

#6. Display Dataset
st.header("Dataset")
st.dataframe(df, use_container_width=True)

#7. Optional: display information
st.header("Dataset Information")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Number of Rows",
        df.shape[0]
    )
with col2:
    st.metric(
        "Number of Columns",
        df.shape[1]
    )
with col3:
    st.metric(
        "Number of Duplicates",
        df.duplicated().sum()
    )

#8. Statistical Summary

st.header("Statistical Summary")
st.dataframe(
    df.describe(), 
    use_container_width=True
)

#9. Feature and Label
X = df[[
    "Temperature",
    "PM2.5",
    "PM10"
]]

y = df["AQI"]

#10. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#11. Create Machine Learning Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

#12. Train Model
model.fit(
    X_train,
    y_train
)

#13. Test Predictions
y_pred = model.predict(
    X_test
)

#14. Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

#Display Model Performance 
st.header("ML Model Performance")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        "MAE",
        round(mae, 2)
    )

with col2:
    st.metric(
        "MSE",
        round(mse, 2)
    )

with col3:
    st.metric(
        "RMSE",
        round(rmse, 2)
    )

with col4:
    st.metric(
        "R2 Score",
        round(r2,2)
    )

#16. Actual and Predicated AQI
st.header("Actual and Predicted AQI")

comparison = pd.DataFrame(
    {
        "Actual AQI : ": y_test.values,
        "Predicted AQI : ": y_pred
    }
)

st.dataframe(
    comparison,
    use_container_width = True
)

#17. Line Chart - AQI
st.header("AQI Trend")

fig1, ax1 = plt.subplots(
    figsize = (10,5)
)

ax1.plot(
    df["AQI"],
    marker = "o"
)
ax1.set_title("AQI Trend")

ax1.set_xlabel("Record")

ax1.set_ylabel("AQI")

st.pyplot(fig1)

#18. Bar Chart - Average Values
st.subheader("Average Air Quality Values")

average = df[
    [
        "Temperature",
        "PM2.5",
        "PM10",
        "AQI"
    ]
].mean()

fig2, ax2 = plt.subplots(
    figsize = (10,5)
)

ax2.bar(
    average.index,
    average.values,
    color = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F"]
)

ax2.set_title("Average Air Quality Measurements")

ax2.set_xlabel("Features")

ax2.set_ylabel("Average Values")

st.pyplot(fig2)

#19. Scatter Chart - PM2.5 and AQI

st.subheader("PM2.5 and PM10")

fig3, ax3 = plt.subplots(
    figsize = (10,5)
)

ax3.scatter(
    df["PM2.5"],
    df["AQI"],
    color = "#FF5733",
    label = "PM2.5"
)

ax3.set_title("PM2.5 and AQI")

ax3.set_xlabel("Features")

ax3.set_ylabel("Average Values")

st.pyplot(fig3)

#20. Feature Importance

st.subheader("Feature Importance")

importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }
)
importance = importance.sort_values(
    "Importance",
    ascending = False
)

st.dataframe(
    importance,
    use_container_width=True
)

fig4, ax4 = plt.subplots(
    figsize = (10,5)
)

ax4.bar(
    importance["Feature"],
    importance["Importance"],
    color = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F"]
)

ax4.set_title("Feature Importance")

ax4.set_xlabel("Features")

ax4.set_ylabel("Importance")

st.pyplot(fig4)

#21. AQI Prediction Section

st.subheader("Predict AQI Quality")

col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value = 10.0,
        max_value = 50.0,
        value = 30.0
    )

with col2:
    pm25 = st.number_input(
        "PM2.5 (µg/m³)",
        min_value = 0.0,
        max_value = 500.0,
        value = 20.0
    )

with col3:
    pm10 = st.number_input(
        "PM10 (µg/m³)",
        min_value = 10.0,
        max_value = 500.0,
        value = 20.0
    )

#22. Predict Button
if st.button(
    "Predict AQI",
    use_container_width = True
):
    #Create input DataFrame
    input_data = pd.DataFrame(
        {
            "Temperature" : [temperature],
            "PM2.5" : [pm25],
            "PM10" : [pm10]
        }
    )

    #Make Prediction
    prediction = model.predict(
        input_data
    )

    aqi = prediction[0]

    #Display prediction
    st.subheader("Predicted Air Quality")

    st.metric("Predicted AQI", round(aqi,2))

    #23. AQI Category

    if aqi <= 50:
        st.success("Good - Air quality is good.")

        category = "Good"

    elif aqi <= 100:
        st.info("Moderate - Air quality is acceptable.")

        category = "Moderate"

    elif aqi <= 150:
        st.warning("Unhealthy for sensitive groups")

        category = "Unhealthy for sensitive groups"

    elif aqi <= 200:
        st.error("Unhealthy")

        category = "Unhealthy"

    elif aqi <= 300:
        st.error("Very Unhealthy")

        category = "Very Unhealthy"

    else:
        st.error("Hazardous")

        category = "Hazardous"

    #Display Category
    st.write("Air Quality Category:", category)

    #24. Footer
st.divider()

st.caption("Air Quality Prediction by using Python+Pandas+Matplotlib+Scikit-learn+Streamlit")
