"""
String Formatting is the process of inserting variables or values into a string to create readable
and well-formatted output.
Python provides three main ways to format string:
1. f-strings(latest and recommended)
2. format() method
3. % operator
"""

# 1. f-string (format string)
# Syntax : f"Text(variable)"
name = "Alice"
age = 20
print(f"My name is {name}.")
print(f"I'm {age} years old.")

# 2. format() method : it replaces {} placeholders with values
# Syntax : "{}".format(value)
print("My name is {} and I'm {} years old.".format(name, age))


# 3. % operator : it uses format specifiers such as %s, %d, and %f
print("My name is %s." % name)
print("I'm %d years old." % age)
