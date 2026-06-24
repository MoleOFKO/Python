# Q1. A school stores student data in a tuple

students = (("Alice" , 85, 90, 88),
            ("Bob", 78, 82, 80),
            ("Charlie", 92, 95, 91),
            ("David", 70, 75, 72),
            ("Emma", 88, 90, 85) 
            )

# Part1 :   print the total number of students
print("The total number of students", len(students))

        #   print the first student's record
print(students[0])

        #   print the last student's record
n = len(students)-1
print("The first student's record", students[n])

        #   print the names of all students
for num in students:
    print("Name : ", num[0])

# Part2 : 