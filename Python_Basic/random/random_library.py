"""
random module is used to generate random numbers.
it is useful for : simulation, games, random selections and so on
random library : import random
"""

# 1. random.randrange() - generates a random integer from a specified range
# Syntax : random.randrange(start, stop, step)
# start : start value(inclusive)
# stop : end value(exclusive)
# step : difference between numbers

#Example
import random
number = random.randrange(10)
print(number)
num2 = random.randrange(1, 10)
print(num2)
num3 = random.randrange(1, 10, 2)
print(num3)


# 2. random.seed() - used to initialize the random number generator
# It allows to produce the same random numbers every time
# Syntax : random.seed(value)
# print(random.seed(10))
random.seed(10)
print(random.randrange())
print(random.random())
# print(random.randint())


# Example using random.seed()
import random
# set the seed
random.seed(42)

# Generate a sequence of random numbers
print("Get numbers with seed 42: ")
# for i in range(5):
for _ in range(5):
    print(random.random()) # Generate a random number between 0 and 1
    print(random.randint(1, 100)) # Generate a random integer between 1 and 100


#  3. random.uniform() - generates a random floating-point number between two values
# Syntax : random.uniform(min, max)

import random
temperature = random.uniform(20, 30)
print(temperature)

# 4. random.choice() - selects one random element from a sequence : list, tuple, string
# Syntax : random.choice()

import random
colors = ["red", "green", "blue"]
select_element = random.choice(colors)
print(select_element)


# 5. random.sample() - selects multiple unique random elements
# Syntax : random.sample(sequence, number)

import random
students = ["Aung", "Su", "Mg Mg", "May"]
select = random.sample(students, 2)
print(select)


# 6. random.shuffle() - randomly changes the order of elements in list
# Syntax : random.shuffle(sequence)

import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

