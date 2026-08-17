#Disease (1) or NO Disease (0)
import numpy as np

print("=====Disease Prediction Example=====")

#Features: Age, Blood Pressur, Sugar Level
X = np.array([
    [23, 124, 90],
    [25, 110, 180],
    [28, 140, 100],
    [30, 120, 220]

])

#Labels : no disease 0, disease 1
y = np.array([0, 1, 0, 1])

print("Patient Data")
print(X)

print("Labels")
print(y)