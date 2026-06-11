print("======Logical Operators======")


print("There are 3 logical operators in Python: and, or, not.")

print("1. Logical AND (and)")
print("It returns true if both conditions are true.")
print("Example: ")
if(5 > 3 and 6 > 4):
    print("Both conditions are true.")
else:
    print("At least one condition is false.")

print("-------------------------------------------------------")


print("2. Logical OR (or)")
print("It returns true if at least one condition is true.")
print("Example: ")
if(5 > 3 or 6 < 4):
    print("At least one condition is true.")  
else:  
    print("Both conditions are false.")  

print("-------------------------------------------------------")

print("3. Logical NOT (not)")
print("It returns true if the condition is false.") 
print("Example: ")
a = 8
b = 8
if not(a == b):
    print("The condition is false")
else:
    print("The condition is true")
print("-------------------------------------------------------")