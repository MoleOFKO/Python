def to_press():
    enter = input("\n ...........................Press the Enter to Continue........................... \n")




print("\n Do you wanna Eat FORTUNE COOKIE?")
to_press()
print("Who know the FORTUNE COOKIE are telling the truth future....")
to_press()

taste_choose = 1
while taste_choose != 0: 
    chose = int(input("Here..  What taste do you wanna choose? \n 1. Sweet \n 2. Sour \n 3. Spicy \n 4. Normal \n 5. back \n"))
    if chose == 1:
        print("Ohh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
        to_press()
        taste_choose = 1
        chose = input("Are you sure you want Sweet? \n y/n").lower()
        if chose == "y" or chose == "yes" or chose == "ye" or chose == "yse" or chose == "sye" or chose == "esy" or chose == "es":
            while taste_choose != 0:
                print("Okie! \n There are colored! So, Which one you wanna choose...")
                to_press()
                input("1. Red \n 2. Green \n 3. Yellow \n 4. Orange \n 5. Purple \n 6. White \n 7. Brown \n")
                color = int(input())
                if color == 1:
                    color = "Red" 
                elif color == 2:
                    color == "Green"
                elif color == 3:
                    color == "Yellow"
                elif color == 4:
                    color == "Orange"
                elif color == 5:
                    color == "Purple"
                elif color == 6:
                    color == "white"
                elif color == 7:
                    color == "Brown"
                else:
                    print("No No. \n Only Enter 1 number and number should be 1 to 7 \n If you want other color you can donate to us to add colors")
                    to_press()
                print("So you choice " , color, ". Yes? \n") 
                to_press()
                
                    
        
    elif chose == 2:
        print("Ohh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
        taste_choose = 1
        to_press()
    elif chose == 3:
        print("Ohh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
        taste_choose = 1
        to_press()
    elif chose == 4:
        print("Ohh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
        taste_choose = 1
        to_press()
    elif chose == 5:
        print("Ohh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
        taste_choose = 0
        to_press()
        break
    else:
        taste_choose = 1