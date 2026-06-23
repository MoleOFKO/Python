# sort() methods is used to sort the list  is ascending order by default
numbers= [3, 9, 1, 6, 3, 2]
numbers.sort()
print("Ascending Order : ", numbers)


languages = ["Python" , "Java" , "C++" , "JavaScript" , "Ruby"]
languages.sort()
print("Ascending Order : ", languages)


# descending order
# Syntax: sort(reverse=true)
numbers.sort(reverse=True)
print("Descending Order : ", numbers)


languages.sort(reverse=True)
print("Descending Order : ", languages)


# copy() method is used to create a copy of the list
# it returns a new list containing all the elements of the original list.
fruits = ["apple","banana", "orange", "grape", "melon"]
new_fruits = fruits.copy()
print(new_fruits)

#count() method counts how many items a value appears
names = ["John", "Doe", "John", "Alex"]
print(names.count("John"))

# index() method  finds the position of an items
colors = ["red", "blue", "green"]
print(colors.index("green"))


#reverse() method reverses the order of items
num = [3,4,5,6]
num.reverse()
print(num)


#join() method is used to join the elements of a list into a single string
# with a specified separator between them.

#Example:
list1 = ["Hello", "World", "Python"]
list2 = ["this", "is", "a", "test"]



#Example 1: Joining a list of strings with a space as a separator
separator = ""
new_list = separator.join(list1)
print(new_list)

#Example 2: Joining a list of strings with a comma as a separator
separator = " , "
new_list = separator.join(list1)
print(new_list)

#Example 3: Joining a list of strings with a hyphen as a separator
separator = " - "
new_list = separator.join(list1)
print(new_list)

#Example 4: Joining a list of strings with a + operator as a separator
new_list = list1 + list2
print(new_list)

#Example 5: Joining a list of strings with a extend() method as a separator
numbers.extend(num)
print(numbers)



