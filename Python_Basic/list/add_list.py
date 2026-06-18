# append() method is used to add an item to the end of the list
numbers = [1,2,3,4,5]
print("Before Adding : " , numbers)
numbers.append(8) #value
print("After Adding : " , numbers)

snacks = ["chips" , "cookies", "candy"]
print("Before Adding : ", snacks)
snacks.append("popcorn")
print("After Adding : " , snacks)

#insert() method is used to add an item at the specified index
colors = ["red","blue", "green", "yellow"]
print(len(colors))
print("Before Update : ", colors)
colors.insert(2, "purple")
print("After Updating : " , colors)


#extend() method is used to add the elements of a list (or any iterable), to the end of the current list.
list1 = [1, 2, 3]
list2 = [True , False, 0, 1]
list2.extend(list1)
print(list2)