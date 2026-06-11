#function is a block of reuseable code
#Why use function?
#1. reusable
#2. code is organized and clean
#3. easy debugging
#4. better readability

#Syntax
#   def function_name()
    #code block

#Example without parameters
def greet():
    print("Hello")

#recall or revoked
greet()


#parameter are variables listed in a function definition
#argument are the values ypu pass into the function when calling it

#Example with one parameter
def info(name):
    print("Hello" , name)
info("Ko")
info("Shane")


#Example with two parameters
def device(brand, price):
    print("This device is " , brand , " and price is ", price)

device("Lenovo", 1200000)
device("Dell" , 1400000)


#Example with return value
#return sends result back to the caller
def add(a,b):
    return a+b
result = add(3,5)
print("Addition is " , result)

#Example with default parameters
#if no value is passed, default value is used

def metro(course = "IT"):
    print("Metro teaches " , course)
metro()


#Example with multiple parameters
def student(name , age , grade):
    print(name , age , grade)
student("Aung Aung" , 13 , "Grade 8")

#Example with Keyword Argument
#when using keyword arguments , order doesn't matter


