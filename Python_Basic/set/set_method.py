# union() method returns a new set with all items from both sets
# Syntax : set.union(set)

# Example using union() method
bikes = {"Honda", "Yamaha",  "Suzuki"}
prices = {1000, 2000, 3000}
bikes_prices = bikes.union(prices)
print(bikes_prices)

# you can also use the | operator to join two sets
# Example using | operator
num1 = {1,2,3}
num2 = {4,5,6}
num3 = num1 | num2
print(num3)


# If you want to combine more than two sets
# you can use the union() method or the | operator multiple times
# Syntax : set.union(set1, set2, set3,....) or set1 | set2| set3 |....

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {7, 8, 9}
set4 = {"a", "b", "c"}
set5 = {True, False}

# output:
# 1 and True is considered as same value, so only one of them will be present in the final set
# 0 and False is considered as same value, so only one of them will be present in the final set

new_set = set5.union(set1, set2, set3, set4)
print(new_set)

# In python, True is considered as 1 and false is considered as 0.
# when you combine sets that contain boolean values and integers
# the boolean values will be treated as integers, and the resulting set will contain only unique values


# intersection() method returns a new set with only the items that are present in both sets
# Syntax : set.intersection(set)
fruits = {"apple", "banana", "cherry"}
favorite_fruits = {"banana", " kiwi", "mango"}
common_fruits = fruits.intersection(favorite_fruits)
print(common_fruits)


# you can also use the & operator to find the intersection of two sets
# Example using & operator
devices1 = {"laptop", "tablet", "smartphone"}
devices2 = {"smartwatch", "tablet", "desktop"}
common_devices = devices1 & devices2
print(common_devices)