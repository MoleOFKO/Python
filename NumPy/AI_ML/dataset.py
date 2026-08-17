'''
ML models use datasets where each row is sample and each column is a feature


'''


import numpy as np
#feature example : height(cm), weight(kg), Age
#X = feature matrix to store training data
X = np.array([
    [123, 124, 25],
    [126, 127, 28],
    [135, 137, 38]
])
print(X)

#label(target values) - used in classification problems
#y = label to predict
y = np.array([1, 0, 1])
# 0 = yes
# 1 = no


#train/test split using indexing
X = np.arange(20)

train = X[:15]
test = X[15:]

print("Train : ", train)
print("Test : ", test)
1