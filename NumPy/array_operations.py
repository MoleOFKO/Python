'''
Array Operations:
-mathematical operations performed directly on NumPy arrays
-unlike python list, numpy performs element-wise operations
(each element is calculated with the corresponding element in another array)


Notes:
- array must have the same shape for element wise operations
- numpy operations are faster and more memory-efficient than using loops



'''

import numpy as np

#addition
x = np.array([10, 20, 30])
y = np.array([20, 30, 40])

#Adding feature values or updating model parameters
print("addition is : ", x + y)

#Calculating difference or errors between actual and predicted values
print("subtraction is : ", x - y)

#Each element is multiplied by its corresponding element, it is not matrix multiplication
print("Multiplication is : " , x * y)

#Matrix Multiplication:
#np.dot() - matrix multiplication, not element-wise multiplication
#it is essential in neural networks and deep learning
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix is : " , np.dot(A,B))

#Divides corresponding elements and it is usually a floating-point array
print("Division is : " , x / y)

#Returns the remainder after division and it is useful for checking even/odd numbers or grouping data
print("Modulus is : " , x % y)

#Exponent : raises each element to a power
#it is commonly used in mathematical formulas and machine learning
arr = np.array([2, 3, 4])
print("Exponent is :", x ** 2)


# Scalar Operations
#it is automatically applied to every element in the array (broadcasting)
#it is a single number
print("Scalar Operation")
print(arr + 5)
print(arr * 2)


#Comparison Operation
arr = np.array([10, 20, 30, 40])
print(arr > 20)
print(arr >= 10)
print(arr < 40)
