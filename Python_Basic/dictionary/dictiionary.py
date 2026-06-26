# dictionary is used to store data or multiple items in key value pair
# dictionary is mutable, ordered and does not allow duplicates
# It is written in curly braces{} and key value pairs are separated by commas
# Syntax: dictionary_name = {key1:value1, key2value2, key3value3,....}

# Example
students = {
    "name" : "Aye Aye",
    "age" : 23,
    "grade" : "A",
    "gender" : "Female"
}
print(students)

#Accessing values in a dictionary
# You can access the values in a dictionary by using the keys

#Example
print(students["name"])     
print(students["age"])
print(students["grade"])
print(students["gender"])

#Accessing values using get() method
fruits = {
    "price" : 3000,
    "category" : "Sweet"
}
print(fruits.get("price"))



# keys() method is used to access a list of all the keys in the dictionary
languages = {
    "Python" : "High-level programming language",
    "Java" : "Object-oriented programming language",
    "JavaScript" : "Scripting language"
}
print(languages.keys())

# values() method is used to access a list of all the values in the dictionary
print(languages.values())

# items() method is used to access a list of all the values in the dictionary
print(languages.items())


# Dictionary length using len() method
print(len(fruits))
print(len(students))


# Data types of dictionary values using type() method
print(type(students))
print(type(fruits))

#Different data types of dictionary values
person = {
    "name" : "Aye Aye",
    "age" : 23,
    "is_student" : True,
    "hobbies" : ["reading", "traveling", "cooking"]
}
print(person)

# Dictionary Constructor 
# Create a dictionary using dict() method
trees = dict(apple = 1, mango = 2, banana = 3)
print(trees)

# Another Example
employee = dict(name = "Aye Aye", age = 23, department = "IT")
print(employee)


# When duplicate  keys are used in a dictionary
# the last value will overwrite the previous values for that key
student = {
    "name" : "Hla Hla",
    "name" : "Mg Mg"
}
print(student)


# to determine if a specified key is present in a dictionary ues the in keyword
# Example
cars = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1990
}
#check if model is presented
if "model" in cars:
    print("Yes, it is present.")
    