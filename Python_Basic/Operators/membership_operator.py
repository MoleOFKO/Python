print("======Membership Operators======")

print("They are used to check whether a value exists in a sequence such as a list, tuple, string or dictionary.")
print("1. in : returns true if the value exists in the sequence")
print("2. not in : returns true if the value doesn't exist in the sequence")
print("")
print("Example: ")

text = "Python is very simple programming language and easy to learn."
print("easy" in text)  # True
print("highly" in text)  # False
print("top" not in text)  # True
print("python" not in text)  # True
print("Python" not in text)  # False

#create a list
products = ["laptop", "mobile", "tablet", "monitor"]
product_name = input("Enter the product name: ")
if product_name in products:
    print("Product is available.")
else:
    print("Product is not available.")

#create Another list
login_successful = 0
logins = ["ko shane", "larry", "jimina", "yamada", "kaung kaung"]
pwd = "123456"
while login_successful == 0:
    login_name = input("Enter your login name: ")
    password = input("Enter your password: ")
    if login_name in logins and password == pwd:
        print("Login successful.")
        login_successful = 1
        break
    else:
        print("Login failed.")
        


