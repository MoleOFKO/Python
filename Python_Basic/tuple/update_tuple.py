#Tuple cannot be updated or changed.
# Tuples are immutable. meaning that you cannot change, add, or remove items after the tuple has been created.
# However, you can convert a tuple into a list, make changes to the list, and then convert it back into a tuple.

#Example
flowers = ("Rose", "Lily", "Tulip", "Daisy", "Orchid")
#convert tuple into a list using list() method
flowers_list = list(flowers)
#update the list
flowers_list[1] = "Sunflower"
#convert the list back into a tuple using tuple method
flowers = tuple(flowers_list)
print(flowers)

#Adding items Example
#Convert tuple into a list using list() method
food = ("Pizza", "Burger", "Pasta")
food_list = list(food)
#Add items to the list using append() method
food_list.append("Salad")
#Add items to the list using inset() method
food_list.insert(1, "Fries")
#Convert the list back into a tuple using tuple() method
food = tuple(food_list)
print(food)

#Removing items Example
#Convert tuple into a list using list() method
drink = ("Water", "Juice", "Soda", "Tea")
drink_list = list(drink)
#remove items from the list using remove() method
drink_list.remove("Soda")
#remove items from the list using pop() method
drink_list.pop(1)
#Convert the list back into a tuple using tuple() method
drink = tuple(drink_list)
print(drink)