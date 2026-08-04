import sys
import random


def get_input(type):
    
    while True:
        try:
            return input(type)
        except EOFError:
            print("Input error. Please try again.")
        except KeyboardInterrupt:
            print("Input cancelled.")
            return ""


def get_int(type, min_value=None, max_value=None):
    while True:
        raw_value = get_input(type).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Please enter a number less than or equal to {max_value}.")
            continue
        return value


def get_yes_no(type):
    while True:
        answer = get_input(type).strip().lower()
        if answer in ["y", "yes"]:
            return True
        if answer in ["n", "no"]:
            return False
        print("Invalid input. Please enter y or n.")


def to_press():     #Enter to Continue function
    get_input("\n ...........................Press the Enter to Continue........................... \n")


def game_exit():
    if get_yes_no("Do you want to quit? (y/n): "):
        sys.exit()
    

def color():    
    # Color picking
    while True:
        print("\nOkie! \n There are colored! So, Which one you wanna choose...")
        to_press()
                    
        # choose colour
        color_choice = get_int(" 1. Red \n 2. Green \n 3. Yellow \n 4. Orange \n 5. Purple \n 6. White \n 7. Brown \n", 1, 7)
                    
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
                        
        confirm = get_yes_no(f"So your choice is {color}. Yes? (y/n): ")
        to_press()
        if quality_choose(confirm):
            return color
        else:
            print("Choose the Number 1 to 7")
            continue

        
# confirm function
def quality_choose(confirm):
    if isinstance(confirm, str):
        confirm = confirm.strip().lower()
    if confirm in ["y", "yes", "ye", "yse", "sye", "esy", "es", 1, True]:
        return True
    return False

def replay_the_game():
    return get_yes_no("Do you want to play again? (y/n): ")

#game choice
def game_choice():
    # game choice
    game_choice = get_int("\n Okie! \n Here the Games are : \n1. Tic Tat Toe\n2. Guess the Number\n3. Maths \n4. Back\n", 1, 4)
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

def open_fortune_cookie(category=None):
    # If no category is specified, pick a random category first
    if not category:
        category = random.choice(list(fortune_cookies.keys()))
    
    # Pick a random fortune from the chosen category
    fortune = random.choice(fortune_cookies[category])
    
    print(f"🥠 [Fortune Cookie - {category.capitalize()}]")
    print(f'"{fortune}"\n')


def choose_fortune_cookie():
    while True:
        choice_cookie = get_int(
            "Which fortune cookie do you want to open? \n"
            "1. Luck \n"
            "2. Wisdom \n"
            "3. Cryptic \n"
            "4. Humor \n"
            "5. Back\n",
            1,
            5,
        )

        if choice_cookie == 1:
            open_fortune_cookie("luck")
            return "luck"
        elif choice_cookie == 2:
            open_fortune_cookie("wisdom")
            return "wisdom"
        elif choice_cookie == 3:
            open_fortune_cookie("cryptic")
            return "cryptic"
        elif choice_cookie == 4:
            open_fortune_cookie("humor")
            return "humor"
        elif choice_cookie == 5:
            print("Returning to the previous menu...")
            return "back"

# tic tac toe
def tic_tac_toe():
    point_got = 0

    print("\n--- Welcome to the Tic Tac Toe Challenge! ---")
    print("\nLet's get started!")
    to_press()
    print("Are you Ready?")

    while True:
        board = [" "] * 9
        current_player = "X"

        while True:
            print(f" {board[0]} | {board[1]} | {board[2]}")
            print("---+---+---")
            print(f" {board[3]} | {board[4]} | {board[5]}")
            print("---+---+---")
            print(f" {board[6]} | {board[7]} | {board[8]}")

            if current_player == "X":
                choice = get_int("Choose a slot 1-9: ", 1, 9) - 1
                if board[choice] != " ":
                    print("That slot is already taken. Try again.")
                    continue
            else:
                empty_slots = []
                for i, value in enumerate(board):
                    if value == " ":
                        empty_slots.append(i)
                choice = random.choice(empty_slots)
                print(f"Computer chooses slot {choice + 1}.")

            board[choice] = current_player

            if (
                board[0] == board[1] == board[2] != " " or
                board[3] == board[4] == board[5] != " " or
                board[6] == board[7] == board[8] != " " or
                board[0] == board[3] == board[6] != " " or
                board[1] == board[4] == board[7] != " " or
                board[2] == board[5] == board[8] != " " or
                board[0] == board[4] == board[8] != " " or
                board[2] == board[4] == board[6] != " "
            ):
                print(f"{current_player} wins!")
                if current_player == "X":
                    point_got += 10
                break

            if " " not in board:
                print("It's a draw.")
                break

            current_player = "O" if current_player == "X" else "X"

        if not replay_the_game():
            break

    return point_got

# guess the number
def guess_the_number():
    print("\n--- Welcome to the Guess the Number Challenge! ---")
    point_got = 0

    difficulty_choice = get_int("Guess the Number" \
    "\n There are :" \
    "\n1. 1 Digit Guess" \
    "\n2. 2 Digit Guess" \
    "\n3. 3 Digit Guess" \
    "\n4. 4 Digit Guess\n", 1, 4)
    guess_number_difficulty = get_int(f"\n Are you sure that you will choose ({difficulty_choice}) difficulty? \n1. Yes \n2. No\n", 1, 2)
    while quality_choose(guess_number_difficulty):
        if difficulty_choice == 1:
            replay = 1
            while replay != 0:
                print("\nSo your choice is 1 digit guess...")
                to_press()
                print("Are you Ready?")
                to_press()
                have_to_same_number = random.randint(0, 9)
                guessed_number = get_int("Enter your number 1 Number: ", 0, 9)
                if have_to_same_number == guessed_number:
                    print("Wow! You successfully guess the number.")
                    to_press()
                    point_got += 5
                elif guessed_number < have_to_same_number:
                    print(f"Too low! The random number was {have_to_same_number}.")
                else:
                    print(f"Too high! The random number was {have_to_same_number}.")
                if replay_the_game():
                    replay = 1
                else:
                    replay = 0
        elif difficulty_choice == 2:
            replay = 1
            while replay != 0:
                print("\nSo your choice is 2 digit guess...")
                to_press()
                print("Are you Ready?")
                to_press()
                have_to_same_number = random.randint(10, 99)
                guessed_number = get_int("Enter your number 2 Numbers: ", 10, 99)
                if have_to_same_number == guessed_number:
                    print("Wow! You successfully guess the number.")
                    to_press()
                    point_got += 10
                elif guessed_number < have_to_same_number:
                    print(f"Too low! The random number was {have_to_same_number}.")
                else:
                    print(f"Too high! The random number was {have_to_same_number}.")
                if replay_the_game():
                    replay = 1
                else:
                    replay = 0
        elif difficulty_choice == 3:
            replay = 1
            while replay != 0:
                print("\nSo your choice is 3 digit guess...")
                to_press()
                print("Are you Ready?")
                to_press()
                have_to_same_number = random.randint(100, 999)
                guessed_number = get_int("Enter your number 3 Numbers: ", 100, 999)
                if have_to_same_number == guessed_number:
                    print("Wow! You successfully guess the number.")
                    to_press()
                    point_got += 15
                elif guessed_number < have_to_same_number:
                    print(f"Too low! The random number was {have_to_same_number}.")
                else:
                    print(f"Too high! The random number was {have_to_same_number}.")
                if replay_the_game():
                    replay = 1
                else:
                    replay = 0
        elif difficulty_choice == 4:
            replay = 1
            while replay != 0:
                print("\nSo your choice is 4 digit guess...")
                to_press()
                print("Are you Ready?")
                to_press()
                have_to_same_number = random.randint(1000, 9999)
                guessed_number = get_int("Enter your number 4 Numbers: ", 1000, 9999)
                if have_to_same_number == guessed_number:
                    print("Wow! You successfully guess the number.")
                    to_press()
                    point_got += 20
                elif guessed_number < have_to_same_number:
                    print(f"Too low! The random number was {have_to_same_number}.")
                else:
                    print(f"Too high! The random number was {have_to_same_number}.")
                if replay_the_game():
                    replay = 1
                else:
                    replay = 0
        else:
            print("No No. \n Only Enter 1 number and number should be 1 to 4")
            to_press()
            guess_the_number()
        return point_got

    else:
        print("\nNo No. \nOnly Enter 1 number and number should be 1 to 4")
        to_press()
        guess_the_number()
        
    
        


# maths
def math_solve():
    print("\n--- Welcome to the Math Solve Challenge! ---")
    point_got = 0
    
    # Let the user pick their difficulty tier
    level_choice = get_int(
        "Select your Math Level:\n"
        "1. Level 1 (Addition, Subtraction)      [5 Points]\n"
        "2. Level 2 (Addition, Subtraction, Subtraction, Multiplication)   [10 Points]\n"
        "3. Level 3 (Addition, Subtraction, Subtraction, Multiplication with 2 operators)[15 Points]\n"
        "4. Level 4 (Addition, Subtraction, Subtraction, Multiplication with 3 operators [Easy])      [20 Points]\n"
        "5. Level 5 (Addition, Subtraction, Subtraction, Multiplication with 3 operators [Hard])    [25 Points]\n"
        "6. Level 6 (Addition, Subtraction, Subtraction, Multiplication with 3 operators [Very Hard])    [30 Points]\n"
        "7. Back\n", 1, 7
    )
    
    if level_choice == 7:
        return 0

    confirm = get_yes_no(f"Are you sure you want to attempt Level {level_choice}? (y/n): ")
    if not quality_choose(confirm):
        return math_solve() # Restart selection if they change their mind

    replay = 1
    while replay != 0:
        print(f"\nPreparing Level {level_choice} problem...")
        to_press()
        
        # Core Math logic generators for each level
        if level_choice == 1:
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
            operator = random.choice(["+", "-"])
            if operator == "+":
                correct_answer = num1 + num2
                problem_text = f"What is {num1} + {num2}? "
            elif operator == "-":
                correct_answer = num1 - num2
                problem_text = f"What is {num1} - {num2}? "
            points_allocated = 5

        elif level_choice == 2:
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
            operator = random.choice(["+", "-", "*", "/"])
            if operator == "+":
                correct_answer = num1 + num2
                problem_text = f"What is {num1} + {num2}? "
            elif operator == "-":
                correct_answer = num1 - num2
                problem_text = f"What is {num1} - {num2}? "
            elif operator == "*":
                correct_answer = num1 * num2
                problem_text = f"What is {num1} × {num2}? "
            elif operator == "/":
                correct_answer = num1 / num2
                problem_text = f"What is {num1} ÷ {num2}? "
            points_allocated = 10

        elif level_choice == 3:
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
            num3 = random.randint(1, 99)
            first_operator = random.choice(["+", "-", "*", "/"])
            second_operator = random.choice(["+", "-", "*", "/"])
            if first_operator == "+":
                
                if second_operator == "+":
                    correct_answer = num1 + num2 + num3
                    problem_text = f"What is {num1} + {num2} + {num3}? "

                elif second_operator == "-":
                    correct_answer = num1 + num2 - num3
                    problem_text = f"What is {num1} + {num2} - {num3}? "

                elif second_operator == "*":
                    correct_answer = num1 + num2 * num3
                    problem_text = f"What is {num1} + {num2} * {num3}? "

                elif second_operator == "/":
                    correct_answer = num1 + num2 / num3
                    problem_text = f"What is {num1} + {num2} ÷ {num3}? "

            elif first_operator == "-":

                if second_operator == "+":
                    correct_answer = num1 - num2 + num3
                    problem_text = f"What is {num1} - {num2} + {num3}? "

                elif second_operator == "-":
                    correct_answer = num1 - num2 - num3
                    problem_text = f"What is {num1} - {num2} - {num3}? "

                elif second_operator == "*":
                    correct_answer = num1 - num2 * num3
                    problem_text = f"What is {num1} - {num2} * {num3}? "

                elif second_operator == "/":
                    correct_answer = num1 - num2 / num3
                    problem_text = f"What is {num1} - {num2} ÷ {num3}? "

            elif first_operator == "*":

                if second_operator == "+":
                    correct_answer = num1 * num2 + num3
                    problem_text = f"What is {num1} * {num2} + {num3}? "

                elif second_operator == "-":
                    correct_answer = num1 * num2 - num3
                    problem_text = f"What is {num1} * {num2} - {num3}? "

                elif second_operator == "*":
                    correct_answer = num1 * num2 * num3
                    problem_text = f"What is {num1} * {num2} * {num3}? "

                elif second_operator == "/":
                    correct_answer = num1 * num2 / num3
                    problem_text = f"What is {num1} * {num2} ÷ {num3}? "

            elif first_operator == "/":

                if second_operator == "+":
                    correct_answer = num1 / num2 + num3
                    problem_text = f"What is {num1} / {num2} + {num3}? "

                elif second_operator == "-":
                    correct_answer = num1 / num2 - num3
                    problem_text = f"What is {num1} / {num2} - {num3}? "

                elif second_operator == "*":
                    correct_answer = num1 / num2 * num3
                    problem_text = f"What is {num1} / {num2} * {num3}? "

                elif second_operator == "/":
                    correct_answer = num1 / num2 / num3
                    problem_text = f"What is {num1} ÷ {num2} ÷ {num3}? "

            points_allocated = 15

        elif level_choice == 4:
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
            num3 = random.randint(1, 99)
            num4 = random.randint(1, 99)
            first_operator = random.choice(["+", "-", "*", "/"])
            second_operator = random.choice(["+", "-", "*", "/"])
            third_operator = random.choice(["+", "-", "*", "/"])
            if first_operator == "+":
                
                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 + num2 + num3 + num4
                        problem_text = f"What is {num1} + {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 + num3 - num4
                        problem_text = f"What is {num1} + {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 + num3 * num4
                        problem_text = f"What is {num1} + {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 + num3 / num4
                        problem_text = f"What is {num1} + {num2} + {num3} / {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 + num2 - num3 + num4
                        problem_text = f"What is {num1} + {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 - num3 - num4
                        problem_text = f"What is {num1} + {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 - num3 * num4
                        problem_text = f"What is {num1} + {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 - num3 / num4
                        problem_text = f"What is {num1} + {num2} - {num3} / {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 + num2 * num3 + num4
                        problem_text = f"What is {num1} + {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 * num3 - num4
                        problem_text = f"What is {num1} + {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 * num3 * num4
                        problem_text = f"What is {num1} + {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 * num3 / num4
                        problem_text = f"What is {num1} + {num2} * {num3} / {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 + num2 / num3 + num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 / num3 - num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 / num3 * num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 / num3 / num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "-":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 - num2 + num3 + num4
                        problem_text = f"What is {num1} - {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 + num3 - num4
                        problem_text = f"What is {num1} - {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 + num3 * num4
                        problem_text = f"What is {num1} - {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 + num3 / num4
                        problem_text = f"What is {num1} - {num2} + {num3} ÷ {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 - num2 - num3 + num4
                        problem_text = f"What is {num1} - {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 - num3 - num4
                        problem_text = f"What is {num1} - {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 - num3 * num4
                        problem_text = f"What is {num1} - {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 - num3 / num4
                        problem_text = f"What is {num1} - {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 - num2 * num3 + num4
                        problem_text = f"What is {num1} - {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 * num3 - num4
                        problem_text = f"What is {num1} - {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 * num3 * num4
                        problem_text = f"What is {num1} - {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 * num3 / num4
                        problem_text = f"What is {num1} - {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 - num2 / num3 + num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 / num3 - num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 / num3 * num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 / num3 / num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "*":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 * num2 + num3 + num4
                        problem_text = f"What is {num1} * {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 + num3 - num4
                        problem_text = f"What is {num1} * {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 + num3 * num4
                        problem_text = f"What is {num1} * {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 + num3 / num4
                        problem_text = f"What is {num1} * {num2} + {num3} / {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 * num2 - num3 + num4
                        problem_text = f"What is {num1} * {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 - num3 - num4
                        problem_text = f"What is {num1} * {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 - num3 * num4
                        problem_text = f"What is {num1} * {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 - num3 / num4
                        problem_text = f"What is {num1} * {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 * num2 * num3 + num4
                        problem_text = f"What is {num1} * {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 * num3 - num4
                        problem_text = f"What is {num1} * {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 * num3 * num4
                        problem_text = f"What is {num1} * {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 * num3 / num4
                        problem_text = f"What is {num1} * {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 * num2 / num3 + num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 / num3 - num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 / num3 * num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 / num3 / num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "/":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 / num2 + num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 + num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 + num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 + num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} ÷ {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 / num2 - num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 - num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 - num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 - num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 / num2 * num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 * num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 * num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 * num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 / num2 / num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 / num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 / num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 / num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} ÷ {num4}? "
            points_allocated = 20

        elif level_choice == 5:
            num1 = random.randint(100, 999)
            num2 = random.randint(100, 999)
            num3 = random.randint(100, 999)
            num4 = random.randint(100, 999)
            first_operator = random.choice(["+", "-", "*", "/"])
            second_operator = random.choice(["+", "-", "*", "/"])
            third_operator = random.choice(["+", "-", "*", "/"])
            if first_operator == "+":
                
                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 + num2 + num3 + num4
                        problem_text = f"What is {num1} + {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 + num3 - num4
                        problem_text = f"What is {num1} + {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 + num3 * num4
                        problem_text = f"What is {num1} + {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 + num3 / num4
                        problem_text = f"What is {num1} + {num2} + {num3} / {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 + num2 - num3 + num4
                        problem_text = f"What is {num1} + {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 - num3 - num4
                        problem_text = f"What is {num1} + {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 - num3 * num4
                        problem_text = f"What is {num1} + {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 - num3 / num4
                        problem_text = f"What is {num1} + {num2} - {num3} / {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 + num2 * num3 + num4
                        problem_text = f"What is {num1} + {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 * num3 - num4
                        problem_text = f"What is {num1} + {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 * num3 * num4
                        problem_text = f"What is {num1} + {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 * num3 / num4
                        problem_text = f"What is {num1} + {num2} * {num3} / {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 + num2 / num3 + num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 / num3 - num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 / num3 * num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 / num3 / num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "-":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 - num2 + num3 + num4
                        problem_text = f"What is {num1} - {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 + num3 - num4
                        problem_text = f"What is {num1} - {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 + num3 * num4
                        problem_text = f"What is {num1} - {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 + num3 / num4
                        problem_text = f"What is {num1} - {num2} + {num3} ÷ {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 - num2 - num3 + num4
                        problem_text = f"What is {num1} - {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 - num3 - num4
                        problem_text = f"What is {num1} - {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 - num3 * num4
                        problem_text = f"What is {num1} - {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 - num3 / num4
                        problem_text = f"What is {num1} - {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 - num2 * num3 + num4
                        problem_text = f"What is {num1} - {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 * num3 - num4
                        problem_text = f"What is {num1} - {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 * num3 * num4
                        problem_text = f"What is {num1} - {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 * num3 / num4
                        problem_text = f"What is {num1} - {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 - num2 / num3 + num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 / num3 - num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 / num3 * num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 / num3 / num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "*":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 * num2 + num3 + num4
                        problem_text = f"What is {num1} * {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 + num3 - num4
                        problem_text = f"What is {num1} * {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 + num3 * num4
                        problem_text = f"What is {num1} * {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 + num3 / num4
                        problem_text = f"What is {num1} * {num2} + {num3} / {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 * num2 - num3 + num4
                        problem_text = f"What is {num1} * {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 - num3 - num4
                        problem_text = f"What is {num1} * {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 - num3 * num4
                        problem_text = f"What is {num1} * {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 - num3 / num4
                        problem_text = f"What is {num1} * {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 * num2 * num3 + num4
                        problem_text = f"What is {num1} * {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 * num3 - num4
                        problem_text = f"What is {num1} * {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 * num3 * num4
                        problem_text = f"What is {num1} * {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 * num3 / num4
                        problem_text = f"What is {num1} * {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 * num2 / num3 + num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 / num3 - num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 / num3 * num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 / num3 / num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "/":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 / num2 + num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 + num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 + num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 + num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} ÷ {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 / num2 - num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 - num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 - num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 - num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 / num2 * num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 * num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 * num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 * num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 / num2 / num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 / num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 / num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 / num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} ÷ {num4}? "
            points_allocated = 25

        elif level_choice == 6:
            num1 = random.randint(1000, 9999)
            num2 = random.randint(1000, 9999)
            num3 = random.randint(1000, 9999)
            num4 = random.randint(1000, 9999)
            first_operator = random.choice(["+", "-", "*", "/"])
            second_operator = random.choice(["+", "-", "*", "/"])
            third_operator = random.choice(["+", "-", "*", "/"])
            if first_operator == "+":
                
                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 + num2 + num3 + num4
                        problem_text = f"What is {num1} + {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 + num3 - num4
                        problem_text = f"What is {num1} + {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 + num3 * num4
                        problem_text = f"What is {num1} + {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 + num3 / num4
                        problem_text = f"What is {num1} + {num2} + {num3} / {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 + num2 - num3 + num4
                        problem_text = f"What is {num1} + {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 - num3 - num4
                        problem_text = f"What is {num1} + {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 - num3 * num4
                        problem_text = f"What is {num1} + {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 - num3 / num4
                        problem_text = f"What is {num1} + {num2} - {num3} / {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 + num2 * num3 + num4
                        problem_text = f"What is {num1} + {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 * num3 - num4
                        problem_text = f"What is {num1} + {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 * num3 * num4
                        problem_text = f"What is {num1} + {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 * num3 / num4
                        problem_text = f"What is {num1} + {num2} * {num3} / {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 + num2 / num3 + num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 + num2 / num3 - num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 + num2 / num3 * num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 + num2 / num3 / num4
                        problem_text = f"What is {num1} + {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "-":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 - num2 + num3 + num4
                        problem_text = f"What is {num1} - {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 + num3 - num4
                        problem_text = f"What is {num1} - {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 + num3 * num4
                        problem_text = f"What is {num1} - {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 + num3 / num4
                        problem_text = f"What is {num1} - {num2} + {num3} ÷ {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 - num2 - num3 + num4
                        problem_text = f"What is {num1} - {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 - num3 - num4
                        problem_text = f"What is {num1} - {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 - num3 * num4
                        problem_text = f"What is {num1} - {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 - num3 / num4
                        problem_text = f"What is {num1} - {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 - num2 * num3 + num4
                        problem_text = f"What is {num1} - {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 * num3 - num4
                        problem_text = f"What is {num1} - {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 * num3 * num4
                        problem_text = f"What is {num1} - {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 * num3 / num4
                        problem_text = f"What is {num1} - {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 - num2 / num3 + num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 - num2 / num3 - num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 - num2 / num3 * num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 - num2 / num3 / num4
                        problem_text = f"What is {num1} - {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "*":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 * num2 + num3 + num4
                        problem_text = f"What is {num1} * {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 + num3 - num4
                        problem_text = f"What is {num1} * {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 + num3 * num4
                        problem_text = f"What is {num1} * {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 + num3 / num4
                        problem_text = f"What is {num1} * {num2} + {num3} / {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 * num2 - num3 + num4
                        problem_text = f"What is {num1} * {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 - num3 - num4
                        problem_text = f"What is {num1} * {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 - num3 * num4
                        problem_text = f"What is {num1} * {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 - num3 / num4
                        problem_text = f"What is {num1} * {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 * num2 * num3 + num4
                        problem_text = f"What is {num1} * {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 * num3 - num4
                        problem_text = f"What is {num1} * {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 * num3 * num4
                        problem_text = f"What is {num1} * {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 * num3 / num4
                        problem_text = f"What is {num1} * {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 * num2 / num3 + num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 * num2 / num3 - num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 * num2 / num3 * num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 * num2 / num3 / num4
                        problem_text = f"What is {num1} * {num2} ÷ {num3} ÷ {num4}? "

            elif first_operator == "/":

                if second_operator == "+":
                    
                    if third_operator == "+":
                        correct_answer = num1 / num2 + num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 + num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 + num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 + num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} + {num3} ÷ {num4}? "

                elif second_operator == "-":

                    if third_operator == "+":
                        correct_answer = num1 / num2 - num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 - num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 - num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 - num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} - {num3} ÷ {num4}? "

                elif second_operator == "*":

                    if third_operator == "+":
                        correct_answer = num1 / num2 * num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 * num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 * num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 * num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} * {num3} ÷ {num4}? "

                elif second_operator == "/":

                    if third_operator == "+":
                        correct_answer = num1 / num2 / num3 + num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} + {num4}? "

                    elif third_operator == "-":
                        correct_answer = num1 / num2 / num3 - num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} - {num4}? "

                    elif third_operator == "*":
                        correct_answer = num1 / num2 / num3 * num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} * {num4}? "

                    elif third_operator == "/":
                        correct_answer = num1 / num2 / num3 / num4
                        problem_text = f"What is {num1} ÷ {num2} ÷ {num3} ÷ {num4}? "
            points_allocated = 30

        # type user for the answer
        user_answer = get_int(problem_text)
        
        if user_answer == correct_answer:
            print(f"🎉 Correct! You got {points_allocated} points.")
            point_got += points_allocated
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")
            
        to_press()
        
        if replay_the_game():
            replay = 1
        else:
            replay = 0
            
    return point_got

    

    
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
        start_end = get_int("Let's Get started!" \
        "\n1. Let's Goo!" \
        "\n2. Later (Exit)\n", 1, 2)
        if start_end == 1:

            chosen_taste = ""
            chosen_color = ""

            #taste choose here
            taste_choose = 1
            while taste_choose != 0: 
                chose = get_int("\nHere..  What taste do you wanna choose? \n 1. Sweet \n 2. Sour \n 3. Spicy \n 4. Normal \n 5. back \n 6. Exit\n", 1, 6)
                
                choice = 0
                #sweet
                if chose == 1:
                    print("\nOhh..  Your choice SWEET... Not Bad, Not bad \n BTW Eat less Sweet")
                    to_press()
                    
                    confirm = get_yes_no("Are you sure you want Sweet? \n y/n: ")
                    if quality_choose(confirm):
                        chosen_taste = "Sweet"
                        taste_choose = 0
                            
                #sour
                elif chose == 2:
                    print("\nOhh..  Your choice SOUR... Huh.. \n Sour..... ( ͠° ͟ʖ ͡°)")
                    to_press()

                    confirm = get_yes_no("Are you sure you want Sour? \n y/n: ")
                    if quality_choose(confirm):
                        chosen_taste = "Sour"
                        taste_choose = 0

                # spicy
                elif chose == 3:
                    print("\nOhh..  Your choice SPICY... Not Bad, Not bad \n I like spicy too. Our like are same.ヾ(≧▽≦*)o")
                    to_press()

                    confirm = get_yes_no("Are you sure you want Spicy? \n y/n: ")
                    if quality_choose(confirm):
                        chosen_taste = "Spicy"
                        taste_choose = 0 

                # Normal
                elif chose == 4:
                    print("\nOhh..  Your choice NORMAL... Best Choice! \n It's a recommended one tho. ^_~")
                    to_press()

                    confirm = get_yes_no("Are you sure you want Normal? \n y/n: ")
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
                    confirm = get_yes_no("Are you sure you want Normal? \n y/n: ")
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
            total_point = 20

            # explain how point work
            know = get_input(f"Here are your points: {total_point}\nEnter '?' to know what the points are for: ")
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
            fortune_cookies = {
                "luck": [
                    "An unexpected item will soon bring you great fortune.",
                    "Your next gamble will pay off handsomely.",
                    "A rare encounter awaits you in the most unlikely place.",
                    "Bad luck will look away from you for the next three days.",
                    "A golden opportunity is hiding in plain sight.",
                    "The next chest you open contains exactly what you didn't know you needed.",
                    "A minor misstep today will save you from a catastrophic fall tomorrow.",
                    "Lady Luck is fickle, but tonight she’s buying the rounds.",
                    "An item you once discarded will soon find its way back to save you.",
                    "The wind blows in your favor; now is the time to hoist the sails.",
                    "A stranger will soon offer you a trade that seems unfair, but favors you immensely.",
                    "The next time you flip a coin, trust the outcome blindly.",
                    "A path you take by mistake will lead to the treasure you were actually looking for.",
                    "Your next critical strike will land exactly when you need it most.",
                    "Fortune favors the bold, but it absolutely adores the reckless today."
                ],
                "wisdom": [
                    "The sharpest blade is forged in the hottest fire.",
                    "To find the path forward, look closely at where you fell.",
                    "A hoard of gold is worthless if you lack the strength to carry it.",
                    "Do not mistake a brief rest for the end of the journey.",
                    "The wisest warrior knows when to walk away from a empty chest.",
                    "An unmapped road is not empty; it is simply waiting for your footprints.",
                    "The loudest thunder brings the shortest rain; speak softly but carry substance.",
                    "A shield is only as strong as the conviction of the hand holding it.",
                    "Do not curse the darkness when you are the one carrying the torch.",
                    "The cost of a mistake is small compared to the price of doing nothing.",
                    "Knowing the name of the monster is half the battle; knowing its hunger is the rest.",
                    "The water reflects the sky, yet it remains firmly rooted to the earth.",
                    "Do not blame the arrow for missing the target if the bow was drawn in anger.",
                    "A map only shows you where others have been, not where you ought to go.",
                    "The value of a secret decreases the moment you realize you aren't the only one who knows it."
                ],
                "cryptic": [
                    "Beware of the shadow that moves faster than the light.",
                    "The walls have eyes, but the floor has secrets.",
                    "What you seek is also seeking you.",
                    "When the clock strikes midnight, do not look behind you.",
                    "A closed door is sometimes the safest place to be.",
                    "The mirror reflects everything except the one thing you came to see.",
                    "Listen closely to the silence; it is trying to warn you.",
                    "The key you lost was never meant to open a door you could see.",
                    "Count the stairs on your way down. If the number changes, do not turn back.",
                    "They are not following you; you are simply walking the path they cleared.",
                    "If you hear your own voice calling from the trees, do not answer it.",
                    "The shadows grow longer even as the sun rises higher.",
                    "The water in the well is rising, but the bucket remains completely dry.",
                    "Look for the door that wasn't there yesterday.",
                    "The threads are tangling, and you are the one holding the scissors."
                ],
                "humor": [
                    "You will soon feel a sudden urge to buy more health potions.",
                    "Error 404: Fortune not found. Try breaking another cookie.",
                    "Help! I am trapped inside a fortune cookie factory!",
                    "Do not look back. Something might be gaining on you. (Just kidding, or am I?)",
                    "Your pockets will soon be heavy, but mostly with useless rocks."
                    "You will soon face your greatest, most terrifying foe: inventory management.",
                    "That NPC wasn't ignoring you; they just forgot their dialogue lines.",
                    "The dragon is more afraid of you than you are of it. (Note: This is a blatant lie.)",
                    "A critical failure is just a critical success in the wrong direction.",
                    "Your future holds great wealth, though mostly in copper coins and rusted daggers."
                    "You will soon achieve greatness, right after you finish procrastinating.",
                    "Warning: Do not pet the glowing moss. No matter how fluffy it looks.",
                    "Your luck is like a broken clock: completely wrong until it suddenly isn't.",
                    "The gods are watching you. They find your playstyle highly chaotic.",
                    "You are about to find a legendary weapon! Too bad it requires a different class to use."
                ]
            }

            while from_start1 != 0:
                print(f"\nYour current points: {total_point}")
                print("1. Play Tic Tac Toe")
                print("2. Play Guess the Number")
                print("3. Play Maths")
                print("4. Open Fortune Cookie")
                print("5. Exit")
                menu_choice = get_int("Choose an option: ", 1, 5)

                if menu_choice == 1:
                    get_point = tic_tac_toe()
                    total_point += get_point
                    print(f"You earned {get_point} points. Total points: {total_point}")
                    to_press()

                elif menu_choice == 2:
                    get_point = guess_the_number()
                    total_point += get_point
                    print(f"You earned {get_point} points. Total points: {total_point}")
                    to_press()

                elif menu_choice == 3:
                    get_point = math_solve()
                    total_point += get_point
                    print(f"You earned {get_point} points. Total points: {total_point}")
                    to_press()

                elif menu_choice == 4:
                    while True:
                        print(f"\nYou have {total_point} points.")
                        print("1. Poor     (20 points)")
                        print("2. Normal   (30 points)")
                        print("3. Good     (40 points)")
                        print("4. Premium  (50 points)")
                        print("5. Back")

                        fortune_choice = get_int("Choose an option: ", 1, 5)

                        if fortune_choice == 5:
                            break

                        if fortune_choice == 1:
                            point_use = 20
                        elif fortune_choice == 2:
                            point_use = 30
                        elif fortune_choice == 3:
                            point_use = 40
                        else:
                            point_use = 50

                        if point_use > total_point:
                            print("You don't have enough points.")
                            if get_yes_no("Do you want to play a game to earn points? (y/n): "):
                                break
                            else:
                                game_exit()
                        else:
                            total_point -= point_use
                            choose_fortune_cookie()
                            print(f"You have {total_point} points left.")
                            to_press()
                            break

                elif menu_choice == 5:
                    game_exit()

                else:
                    print("Invalid choice.")
                from_start1 = 1
        elif start_end == 2:
            game_exit()     
        else:
            print("Invalid choice.")