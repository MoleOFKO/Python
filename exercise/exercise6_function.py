#Q1.    Write a function to find average of number in a list
#sum() function is used to calculate the sum of all elements in the list
#len() function is used to calculate the number of elements in the list
def average(numbers):
    return sum(numbers)/len(numbers)
print("Average is : ", average([1,2,3,4,5,6]))



#Q2.    Cont vowels in a given word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Metro IT & Japanese Language Centre"))





#Q3.    Write a function to calculate sum from 1 to n
def sum_num(num):
    total = 0
    for i in range(1, num+1):
        total += i  #total = total + i
    return total
print(sum_num(10))



#Q4.    Write a function to Find largest of two number
def largest_num(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1
print("The largest number is ",largest_num(10,90))