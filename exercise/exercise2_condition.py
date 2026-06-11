print("====Subject and Marks====")

english = int(input("Enter the English marks :"))
math = int(input("Enter the math marks :"))
science = int(input("Enter the Science marks :"))
computer = int(input("Enter the Computer marks :"))

count = 0
if english > 40:
    count = count + 1;

if math > 40:
    count = count + 1;

if science > 40:
    count = count + 1;

if computer > 40:
    count = count + 1

avg = (english + math + science + computer) / 4

if avg > 40 or count >= 3: 
    print("Passed")
else:
    print("Failed")
