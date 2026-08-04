import numpy as np

#Special Arrays
#zeros function is used to create an array filled with zeros.
arr = np.zeros((3, 4))
print(arr)

#ones functions is used to create an array filled with ones.
arr = np.ones((2, 3))
print(arr)

#eyes function is used to create an identity matrix.
#Syntax : np.eye(n)
arr = np.eye(4)
print(arr)

#arange functions is used to create a
# syntax : np.arange (start , stop, step)

#example with stop value only
arr = np. arange(10)
print(arr)

#example with start and stop value
arr = np.arange(1, 11)
print(arr)

#Example with start, stop, and step value
arr = np.arange(2, 20, 3)
print(arr)

arr = np.arange(20, 0, -1)
print(arr)
