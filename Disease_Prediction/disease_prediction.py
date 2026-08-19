#import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

#1. load Dataset
#Read CSV File
data = pd.read_csv("D:\PROJECT\Python\Disease_Prediction\disease_data.csv")

#Display Dataset 
print("Dataset : ")
print(data)

#2. Separate Features and Label or Class or Target
#Features are input values used for prediction 
X = data[
    [
        "Age",
        "BloodPressure",
        "BloodSugar",
        "Cholesterol"
    ]
]

#Target or Label is value we want to predict
#0 = No Disease
#1 = Disease
y = data["Disease"]

#3. Split Dataset into Training and Testing
#80% of data -> Training
#20% of data -> Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y,
    test_size = 0.2,
    random_state = 42,
    stratify = y
)

#4. Create Machine Learning Model
model = DecisionTreeClassifier(
    random_state = 42
)

#5. Train Model
model.fit(X_train, y_train)
print("\nModel Training Completed!")

#6. Test Model
#Make prediction using test data
y_pred = model.predict(X_test)

#7. Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy : ")
print(accuracy)

#8. Classification Report
print("\nClassification Report : ")
print(classification_report(y_test, y_pred))

#9. Predict New Patient
new_patient = [
    [
        55,
        120,
        80,
        150
    ]
]

#Make Prediction
prediction = model.predict(new_patient)

#10. Display Prediction Result
print("\nNew Patient Prediction : ")
if prediction[0] == 1:
    print("Disease")
else:
    print("No Disease")
