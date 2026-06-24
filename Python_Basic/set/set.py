# A set is an unordered, unchangeable, and unindex collection of unique elements
# it doesn't allow duplicate values
# it is mutable (can add or remove elements)

# set are written with curly brackets
# Syntax : set = {value1, value2,....}


#Access items from a set, you cannot access items by referring to an index or a key
# Can loop through the set items using a for loop by using th in keyword

#Example1
fruits = {"apple", "banana", "cherry"}
print(fruits)

#Access items using for loop
for fruit in fruits:
    print(fruit)


# Add items to a set using add() method
# add() method adds an element to the set
# Syntax : set.add(value)
 
#Example1
cars = {"BMW", "Audi", "Toyota"}
cars.add("Honda")
print(cars)


# update() method adds multiple elements to the set or another set to the existing set
# Syntax : set.update([value1, value2,....])

#Example : add multiple elements to an existing set
numbers = {1,2,3}
numbers.update([4,5,6])
print(numbers)

#Example : add another set to an existing set
fruits = {"apple", "banana", "cherry"}
tastes = {"sweet", "sour", "bitter"}
fruits.update(tastes)


