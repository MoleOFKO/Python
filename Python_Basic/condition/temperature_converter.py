''''
    Sample Output
    
    Temperature Converter
    1.  Celsius to Fahrenheit
    2. Fahrenheit to Celsius

    Enter your choice (1 or 2) 1
    Enter temperature in Celsius
    Temperature in Fahrenheit
'''

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your Choice (1 or 2) : ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius : "))
    #formula
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit : ", fahrenheit)
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Celsius : "))
    #formula
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius : ", celsius)
else:
    print("Invalid Input")
