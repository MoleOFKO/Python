import sys
import random
import builtins

def to_press():     #Enter to Continue function
    enter = input("\n ...........................Press the Enter to Continue........................... \n")
    
    

def game_exit():
    try:
        quit = input("Do you want to quit? (y/n): ").lower()
        if quit == "y":
            sys.exit()
        # exit no
    except TypeError:
        print("Invalid Input. \nOnly y or n")
        game_exit()
    

def color():    
    # Color picking
    while True:
        print("\nOkie! \n There are colored! So, Which one you wanna choose...")
        to_press()
                    
        # choose colour
        color_choice = int(input(" 1. Red \n 2. Green \n 3. Yellow \n 4. Orange \n 5. Purple \n 6. White \n 7. Brown \n"))
                    
        if color_choice == 1:
            color = "Red" 
        elif color_choice == 2:
            color = "Green"
        elif color_choice == 3:
            color = "Yellow"
        elif color_choice == 4:
            color = "Orange"
        elif color_choice == 5:
            color = "Purple"
        elif color_choice == 6:
            color = "White"
        elif color_choice == 7:
            color = "Brown"
        else:
            print("No No. \n Only Enter 1 number and number should be 1 to 7 \n If you want other color you can donate to us to add colors")
            to_press()
            continue 
                        
        confirm = input(f"So your choice is {color}. Yes? (y/n): ").lower()
        to_press()
        if quality_choose(confirm):
            return color
        else:
            print("Choose the Number 1 to 7")
            continue

        
# confirm function
def quality_choose(confirm):
    if confirm in ["y", "yes", "ye", "yse", "sye", "esy", "es"]:
        return True
    return False

#game choice
def game_choice():
    # game choice
    game_choice = int(input("\n Okie! \n Here the Games are : \n1. Tic Tat Toe\n2. Guess the Number\n3. Maths \n4. Back"))
    if game_choice == 1:
        return "Tic Tac Toe"
    elif game_choice == 2:
        return "Guess the Number"
    elif game_choice == 3:
        return "Maths"
    elif game_choice == 4:
        return "Back"
    else:
        print("No No. \n Only Enter 1 number and number should be 1 to 4")
        to_press()
        game_choice()

# tic tac toe
def tic_tac_toe():
    print("Tic Tac Toe")

# guess the number
def guess_the_number():
    guess_number_difficulty = input("Guess the Number" \
    "\n There are :" \
    "\n1. 1 Digit Guess" \
    "\n2. 2 Digit Guess" \
    "\n3. 3 Digit Guess" \
    "\n4. 4 Digit Guess")
    if guess_number_difficulty == 1:
        print()
        


# maths
def maths():
    print("Maths")

    

    
# this will be start again and again util user choose to end
from_start = 1
while from_start != 0: 
    # start here
    print("\n Do you wanna Eat FORTUNE COOKIE?")
    to_press()
    print("Who know the FORTUNE COOKIE are telling the truth future....")
    to_press()

    # Main Menu
    main_menu = 1
    while main_menu != 0:
        # start game or exit
        start_end = int(input("Let's Get started!" \
        "\n1. Let's Goo!" \
        "\n2. Later (Exit)"))
        if start_end == 1:

            chosen_taste = ""
            chosen_color = ""

            #taste choose here
            taste_choose = 1
            while taste_choose != 0: 
                chose = int(input("\nHere..  What taste do you wanna choose? \n 1. Sweet \n 2. Sour \n 3. Spicy \n 4. Normal \n 5. back \n 6. Exit\n"))
                
                choice = 0
                #sweet
                if chose == 1:
                    print("\nOhh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
                    to_press()
                    
                    confirm = input("Are you sure you want Sweet? \n y/n: ").lower()
                    if quality_choose(confirm):
                        chosen_taste = "Sweet"
                        taste_choose = 0
                            
                #sour
                elif chose == 2:
                    print("\nOhh..  Your choice SOUR... Huh.. \n Sour..... ( ͠° ͟ʖ ͡°)")
                    to_press()

                    confirm = input("Are you sure you want Sour? \n y/n: ").lower()
                    if quality_choose(confirm):
                        chosen_taste = "Sour"
                        taste_choose = 0

                # spicy
                elif chose == 3:
                    print("\nOhh..  Your choice SPICY... Not Bad, Not bad \n I like spicy too. Our like are same.ヾ(≧▽≦*)o")
                    to_press()

                    confirm = input("Are you sure you want Spicy? \n y/n: ").lower()
                    if quality_choose(confirm):
                        chosen_taste = "Spicy"
                        taste_choose = 0 

                # Normal
                elif chose == 4:
                    print("\nOhh..  Your choice NORMAL... Best Choice! \n It's a recommended one tho. ^_~")
                    to_press()

                    confirm = input("Are you sure you want Normal? \n y/n: ").lower()
                    if quality_choose(confirm):
                        chosen_taste = "Normal"
                        taste_choose = 0

                # Back
                elif chose == 5:
                    print("\nOhh..  Your choice BACK... Not Bad, Not bad \n BTW Eat less Sweet")
                    to_press()
                    
                # Exit
                elif chose == 6:
                    print("Are you going to LEAVE? ≧ ﹏ ≦")
                    confirm = input("Are you sure you want Normal? \n y/n: ").lower()
                    if quality_choose(confirm):
                        while True:
                            print("Bye Bye....ಠ﹏ಠ")
                            exit()
                    
                else:
                    print("Invalid choice, please try again.")

                # taste chosen or not
                if from_start == 0 or chosen_taste == "":
                    continue

            chosen_color = color()

            print(f"\nSummary -> Taste: {chosen_taste} | Color: {chosen_color}")
            to_press()

            print("\nAfter choosing the color and taste of your likes, let's goes to the main theme")
            total_point = 100

            # explain how point work
            know = input(f"Here are your points: {total_point}\nEnter '?' to know what the points are for: ")
            if know == "?":
                print("Point : Special point that use to get the Fortune Cookie. " \
                "\nHow to Get? \n Play games to earn the point. " \
                "\nTic Tat Toe :   10 points " \
                "\n\nGuess Number   :   " \
                "\n1 Digit  :   5 points " \
                "\n2 Digit  :   10 points" \
                "\n3 Digit  :   15 points" \
                "\n4 Digit  :   20 points" \
                "\n\nMath Solve :   " \
                "\nLevel 1  :   5   points " \
                "\nLevel 2  :   10  points" \
                "\nLevel 3  :   15  points" \
                "\nLevel 4  :   20  points" \
                "\nLevel 5  :   25  points" \
                "\nLevel 6  :   30  points " \
                "\n\n Quiz Answer   :   20  points    ")
            to_press()

            from_start1 = 1
            while from_start1 != 0: 
                use_point = input("Here the List of the Fortune Cookie For you " \
                "\n 1. Poor     :   20  points" \
                "\n 2. Normal   :   30  points" \
                "\n 3. Good     :   40  points" \
                "\n 4. Premium  :   50  points" \
                "\n 5. Back" \
                "\n ?. Difference of the Fortune Cookie")
                if use_point == "1":
                    point_use = 20
                elif use_point == "2":
                    point_use = 30
                elif use_point == "3":
                    point_use = 40
                elif use_point == "4":
                    point_use = 50
                elif use_point == "5":
                    point_use = 0
                elif use_point == "?":
                    print("Poor : Taste is Random. Very poor color \n Normal : Taste is not that good. Color is somewhat good. \n Good : 40 points \n Premium : 50 points")
                else:
                    print("Invalid choice, please try again.")
                if point_use != 0:
                    if point_use > total_point:
                        print("You don't have enough points")
                        to_press()
                        play_game_or_not = input("Do you want to play the game? (y/n): ").lower()
                        if play_game_or_not == "y":
                            game_choice()
                            if game_choice() == "Back":
                                from_start1 = 0
                                continue
                            elif game_choice() == "Tic Tac Toe":
                                tic_tac_toe()
                                from_start1 = 0
                                continue
                            elif game_choice() == "Guess the Number":
                                guess_the_number()
                                from_start1 = 0
                                continue
                            elif game_choice() == "Maths":
                                math_solve()
                                from_start1 = 0
                                continue
                        elif play_game_or_not == "n":
                            game_exit()
                        else:
                            from_start1 = 1
                        continue

                    # point use
                    else:
                        total_point -= point_use

                        print(f"You have {total_point} points left")
                        to_press()
                        from_start1 = 0
                else:
                    from_start1 = 0
        elif start_end == 2:
            game_exit()     
        else:
            print("Invalid choice.")