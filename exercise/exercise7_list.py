# Q1.   Write a program that sorts the following list in descending order and print the 3rd largest numbers.
scores = [78,23,16,89,45,38,56,34,80,85,90]
#count how many students scored above 80
scores.sort()
print("Third Largest Numbers : ", scores[2])
i = 0 
count = 0
length = len(scores)
for i in range (0, length):
    if scores[i] > 80:
        count += 1
print("Number of scores that are above 80 : ", count)




# Q2. Create a backup copy of a list. 
# Remove all even numbers from the original list while  keeping the backup unchanged.
# Count how many

#list Comprehension
#[new_value for item in list if condition]


org = [78,23,16,89,45,38,56,34,80,85,90]
backup = org.copy()
org = [num for num in org if num % 2 != 0]

# to_remove= []
# for i in org:
#     if (i % 2) != 0:
#         to_remove.append(i)
# for i in to_remove:
#     scores.remove(i)
# print("After Removing even : ", to_remove)
print("Backup : ", backup)





# Q3. Find the index of the first occurrence of the highest number in a list using max() method
# And reverse a list.
org = [78,23,16,89,45,38,56,34,80,85,90]
org.index(max(org))
print("The index of the first occurrence of the highest number : ", org.index(max(org)))
org.sort(reverse=True)
print("Reverse : ",org)




# Q4. Join two lists and find the index of the largest value after sorting
org1 = [78,23,16,89,45,38,56,34,80,85,90]
org2 = [90, 89, 85, 80, 78, 56, 45, 38, 34, 23, 16]
org1.sort()
org2.sort()
org1.extend(org2) 
print(org1)
print("largest value : ", org1.index(max(org1)))
