#List is a collection which is ordered and changeable or mutable. Allows duplicate members or items.
#List is created by placing all the items (elements) inside square brackets [], separated by commas.

num = [1,2,3,4,5,1,8]
fruits = ["apple" , "banana" , "orange" , "apple" , "banana"]
list1 = ["Aung Aung", 23 , True, 34.5, False, "Apple"]


#Access list items
#List items are indexed and you can access them by referring to the index number, inside square brackets.
#From left to right, the index starts with 0,1,2, etc.
print(num[5]) #8
print(fruits[0]) #apple

#From right to left, the index starts with -1, -2, -3, etc.
print(num[-1]) #8
print(list1[-5]) #23

#Access a range of list items by using the slicing syntax():.
#Specify the start index and the end index, separated by a colon, to return a part of the list.
print(num[1:4]) #[2, 3, 5]
#using negative indexing
print(fruits[-4:-1]) #['banana', 'orange', 'apple']


#Access a range of items by leaving out the start index, the index, the end index, or both.
#if you leave out the start index, the range will start at the first item.
print(num[:4]) #1, 2, 3, 4
#if you leave out the end index, the range will go to the end of the list
print(fruits[2:]) #orange, apple, banana
print(fruits[-4:]) #banana, orange, apple, banana

