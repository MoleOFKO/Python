# remove() method removes the first occurrence of the specified value from the list
# if the value is not found, it raises a ValueError.
things =  ["pen", "pencil" , "eraser" , "notebook" , "pen"]
print("Before Removing : " , things)
things.remove("pen")
print("After Removing : " , things)
#ValueError list.remove(x) : x is not in list
# things.remove("car")



#pop() method removes the item at the specified  index and returning it.
# If no index is specified, it removes and returns the last item in the list.
toys = ["car" , "doll" , "ball" , "puzzle"]
print("Before Removing : " , toys)
#no index
toys.pop()
print("After Removing : " , toys)


#If index is specified, it removes the item at that index
toys.pop(1)
print("After Removing : " , toys) #['car', 'ball']


# del keyword can be used to remove an items at a specific index or to delete the entire list
colors = ["red" , "blue" , "green" , "yellow"]
print("Before  Removing : " , colors)
del colors[2]
print("After Removing : ",colors)
#delete entire list
del colors


# clear() method removes all the items from the list, but keeps the list itself
fruits = ["apple" , "banana" , "orange" , "grape" , "melon"]
print("Before Removing All items : " , fruits)
fruits.clear()
print("After Removing All items : " , fruits)