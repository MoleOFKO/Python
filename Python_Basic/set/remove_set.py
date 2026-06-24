# remove() method removes the specified element from the set
# If the item to remove does not exist, it will raise a KeyError
# Syntax : set.remove(value)


#Example using remove() method
colors = {"red", "green", "blue"}
# colors.remove("purple") #KeyError
colors.remove("green")
print(colors)


# discard() method removes the specified element from the set
# If the item to remove does not exist, it will NOT rise a KeyError
# Syntax : set.discard(value)

# Example using discard() method
drinks = {"water", "juice", "soda"}
drinks.discard("soda")
print(drinks)

# pop() method removes a random element from the set
# Syntax : set.pop()

# Example using pop() method
# In numbers, pop () method removes the smallest element from the set
numbers = {1, 2, 3, 4, 5}
numbers.pop()
print(numbers)

# In foods, pop() method removes a random element from the set
foods = {"pizza", "burger", "pasta"}
foods.pop()
print(foods)

# clear() keyword removes all element from the set
# Syntax : set.clear()

# del keyword can delete the set completely
#Syntax : del set
