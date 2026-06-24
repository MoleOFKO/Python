# tuple is a collection which is ordered and unchangeable or immutable
# tuple allows duplicate items and different data types.
# In python tuples are written with round brackets.
# Syntax : tuple_name (value1, value2, value3, ....)

#Example
dogs = ("Bulldog", "Beagle", "Poodle")
print(dogs)
print(len(dogs))
print(type(dogs))

#Example with one item, a comma is required after the item to indicate that it is a tuple.
dog = ("Bulldog",)
print(type(dog))#tuple

#Example without a comma, it will be considered as a string.
dog = ("Bulldog")
print(type(dog)) #String

# Accessing tuple items
# You can access tuple items by referring to the index number, inside square brackets.
cars = ("BMW", "Volvo", "Ford")
print(cars[0]) #BMW


#from right to left, the index starts from 0
print(cars[1]) #Volvo

#from right to left, the index starts from -1
print(cars[-1]) #Ford

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to the range.
flowers = ("Rose", "Lily", "Tulip", "Daisy", "Orchild")
print(flowers[1:4]) #('Lily', 'Tulip', 'Daisy')

##if you omit the end value, the range will go on to the end of the list.
print(flowers[:3]) #("Rose", "Lily", "Tulio")

#if you omit the end value, the range will go on to the end of the list.
print(flowers[2:]) #("Tulip", "Daisy", "Orchild")

#check if item exists
#You can use the in keyword to check if a certain item is present in a tuple
#Tou can use the not in keyword to ce=heck if a certain item is present in a tuple
fruits = ("Apple", "Banana", "Cherry")
if "apple" in fruits:
    print("Yes, it's exist")
else:
    print("No, it doesn't exist")


#Example using not in keyword
cats = ("Persian" , "Siamese", "Maine Coon")
if "Bengal" not in cats:
    print("No, it doesn't exist.")
else:
    print("Yes, it's exist")