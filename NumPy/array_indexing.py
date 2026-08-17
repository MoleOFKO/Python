'''
Array indexing :
- It is the process of accessing one or more elements from a numpy array using index(position) 
- It use zero-based indexing (first element is zero)
- Negative index starts from the end of the array (-1 is the last element)


'''
import numpy as np
#indexing in 1D array
arr = np.array([10, 20, 30, 40, 50])
print("indexing in 1D array")
print(arr[0]) # first element - 10
print(arr[1]) #second element - 20
print(arr[-1]) #last element - 50
print[arr[-2]] #second last element - 40


#indexing in 2D array
arr = np.array([[10, 20, 30] , [40, 50, 60]])
print(arr[0,0]) #first row, first column    - 10
print(arr[0,1]) #first row, second column   - 20 
print(arr[1,0]) #second row, first column   - 40    
print(arr[1,1]) #second row, second column  - 60


#indexing in 3D array
#Syntax: arr [depth_index, row_index, column_index]
arr = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])
print("Indexing in 3D array")
print(arr[0, 0, 0]) # first depth, first row, first column - 10
print(arr[0, 1, 2]) # first depth, second row, third column - 60
print(arr[1, 0, 1]) # second depth, first row, second column - 80
print(arr[1, 1, 2]) # second depth, second row, third column - 120


#Modify Array Element using index
arr = np.array([10, 20, 30])
arr[1] = 40
print(arr)