# copy() - create a copy of the dictionary
student = {
    "name" : "John Doe",
    "age" : 20
}
new_student = student.copy()
print(new_student)

# fromkeys() - create a dictionary with specified keys and a default value.
keys = ("name", "age", "grade")
students = dict.fromkeys(keys, "Default Value")
print(students)

# get() - return the value of a key
# if key doesn't exist, return None
print(students.get("city"))


# setdefault() - return the value of a key. If key doesn't exist, insert the key with a specified value
person = {
    "name" : "Alice",
    
}
person.setdefault("age", 20)
print(person)