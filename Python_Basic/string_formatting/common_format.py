#  Display Decimal Places
price = 48.897
print(f"{price:.2f}")


#print() function with multiple values
brand = "Samsung"
price = 20000000
year = 2026
print(brand, price, year, )

#  Common Separator

"""
sep(separator) parameter in Python's print() function specifies what is printed between
multiple values. By default, the separator is a space(" ").

syntax : print(value1, value2, value3, sep="separator")


"""

print("Python", "Java", "HTML", "CSS", sep=" / ")
print(1,2,3,4,sep=" , ")


"""
end parameter in Python's print() function specifies what is printed at the end of the output.
By default, ends with a newline (\n), so each print() starts on a new line.

syntax : print(value1, value2, value3, end="end")   
"""


#Default :
print("Hello")
print("World!")

#end = " " (space) - print on the same line with space
print("Hello", end=" ")
print("World!")



# end = "\t" (tab) - followed by a tab
print("Hello", end="\t")
print("World!") 