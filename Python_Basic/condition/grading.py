print("====Grading====")

grade = int(input("Input the Mark : "))
if 100 < grade:
    print("More than grade marks")
elif  80<= grade:
    print("Pass with Grade A")
elif 70 <= grade:
    print("Pass with Grade B")
elif 60 <= grade:
    print("Pass with Grade C")
elif 50 <= grade:
    print("Pass with Grade D")
elif 0 <= grade:
    print("Fail")
else:
    print("Input Invalid")