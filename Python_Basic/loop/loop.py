#loop is used to execute a block of code repeatedly, python provides two main types of
# 1.    for loop    -   it is used to iterate through a sequence such as list, tuple, string or range.
    #Syntax:
    #for variable in sequence:
        #statements
# 2.    while loop  -   it executes as ling as a condition is True
    #Syntax:
    #while condition:
        #statements

#for loop examples
#range(one argument)    -   number of times or loop
#always start from zero
print("One argument")
for i in range(6): 
    print(i)
print("----------------------------------")


#range(two arguments)   -   (start, end)
print("Two argument")
for i in range(1,6):
    print(i)
print("----------------------------------")


#range(three arguments) -   (start, end, step)
print("Three argument")
for i in range(2,11,2):
    print(i)
print("----------------------------------")



#while loop examples
count = 1
while count <= 3:
    print(count)
    count += 1  #count = count + 1

