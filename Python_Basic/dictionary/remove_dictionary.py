# pop() method is used to remove items from a dictionary with the specified key name
# Syntax : dictionary.pop(key)
#Example
flowers = {
    "name" : "Rose",
    "color" : "Red",
    "price" : 500
}
flowers.pop("color")
print(flowers)

# popitem() method is used to remove the last inserted item 
# Syntax : dictionary.popitem()
students = {
    "name" : "Aye Aye",
    "age" : 23,
    "grade" : "A",
    "gender" : "Female"
}
students.popitem()
print(students)


# del keyword removes item with the specified key name 
# Syntax : del dictionary[key]

del students["age"]
print("After Deleting : ", students)

# del keyword also delete the entire dictionary
#! del students

# clear() methods is used to delete all items from the dictionary
# Syntax : dictionary.clear()

students.clear()
print(students)