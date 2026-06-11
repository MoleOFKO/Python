#Q.     print all numbers between 1 and 100 that are divisible by both 3 and 5.

# for i in range(1,101):
#     if i % 3 == 0 and i % 6 == 0:
#         print(i)


#Q Write a program to calculate the sum of numbers from 1 to 100
num = 0
for i in range(1,101):
    num = num + i
print(num)


#Q.     Write a program to print this pattern:
    #* 
    #* * 
    #* * * 
    #* * * * 
    #* * * * * 

for i in range(1,6):
    print("* " * i)


#Q.     Writhe a program to print this pattern:
    #* * * * * 
    #* * * * 
    #* * * 
    #* * 
    #* 
for i in range(5, 0, -1):
    print("* " * i)