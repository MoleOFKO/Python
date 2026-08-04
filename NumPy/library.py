"""
NumPy (Numerical Python) is one of the most important libraries in AI, ML, Data Science.
It provides fast operations on numerical data,
It stores and processes efficiently.

Need to install library - pip install numpy (Python/VS Code), !pip install numpy (Jupyter Notebook/Google Colab)

1. NumPy Arrays : it is a collection of elements stored in structured format.
- it is a collection of elements stored in structured format.
- it is similar to a Python list but faster and optimized for mathematical operations.
- it is used for large datasets.




"""
#insert library
import numpy as np

#1D Array
arr = np.array([12, 13, 45, 78])
print("One Dimensional Array")
print(arr)


#2D Array
arr = np.array([[23, 14, 24],
                [12, 34, 56]
                ])
print("Two Dimensional Array")
print(arr)

#3D Array
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("Three Dimensional Array")
print(arr)

#Array Information
'''
1. ndim - array dimension
2. shape - row * column
3. size - total elements
4. dtype - data type
'''

print("Array Information")
new_arr = np.arr([45, 23, 67], [34, 12, 34], [56, 34, 23])
print("Array Dimension : " , new_arr.ndim)
print("Shape : " , new_arr.shape)
print("Array size : " , new_arr.size)
print("Data Type : " , new_arr.dtype , " and ", type(new_arr))