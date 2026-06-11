'''
    Create a list named mylist that includes numbers from 100 to 110. write a python program to check whether
    the number entered by the user is in the list or not using the membership operator
'''


input = input("Please enter 1 number : ")
mylist = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
if input in mylist:
    print("The number" + input +"is in the list")
else:
    print("sorry, " + input + " wasn't in the list")