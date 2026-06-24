# Join Tuple using +
# + operator is used to combines two or more tuples into a new tuple

#Example1
tuple1 = (1,3,4,6,7)
tuple2 = (1,6,8)
new_tuple = tuple1 + tuple2
print(new_tuple)

#Example2
fruit1 = ("orange", "banana")
fruit2 = ("apple",)
new_fruits = fruit1 + fruit2
print(new_fruits)

#Multiply Tuple using *
# * operator is used to repeat the tuple a specified number of times

#Example1
numbers = (1,2,3)
new_numbers = numbers * 3
print(new_numbers)

#Example2
colors = ("red", "green", "blue")
new_colors = colors * 2
print(new_colors)


# count() method returns the numbers of times a specified value appears in the tuple
# Syntax : tuple.count(value)
print(new_numbers.count(2))


# index() method returns the position (index) of the first occurrence of a specified value
# Syntax : tuple.index(value)
print(new_colors.index("red"))

