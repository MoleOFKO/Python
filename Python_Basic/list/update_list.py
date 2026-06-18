#Create List
animals = ["car" , "dog" , "rabbit" , "hamster" , "parrot"]
print("Before Updating : " , animals)

#update list
animals[2] = "bird"
print("After Updating : " , animals)

#Update List with Range
languages = ["Python" , "Java" , "C++" , "JavaScript" , "Ruby"]
print("Before Update: " , languages)
languages[1:3] = ["CSS" , "HTML"]
print("After Updating : " , languages)


#update list with range by leaving out the end index
numbers = [1,2,3,4,5]
print("Before Updating : " , numbers)
numbers[2:] = [7,3,9]
print("After Updating : ", numbers)

#update list with range by leaving out the start index
fruits = ["apple","banana", "orange", "grape", "melon"]
print("Before Updating : " , fruits)
fruits[:3] = ["kiwi", "peach", "pear"]
print("After Updating : ", fruits)


#update list using insert() method
#insert() method inserts an item at the specified index
colors = ["red","blue", "green", "yellow"]
print(len(colors))
print("Before Update : ", colors)
colors.insert(2, "purple")
print("After Updating : " , colors)
