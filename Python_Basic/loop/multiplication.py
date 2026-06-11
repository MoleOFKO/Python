#Multiplication Table

count = 1
while count <= 12:
    num = int(input("Enter a number : "))
    for i in range(1,13):
        print(num, "*", i, "=" ,num*i)
    count += 1