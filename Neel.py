
#Rock function
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
#NAME
def get_name():
    name = input("What is your name?(First name only)\n").capitalize()
    while len(name) == 0 or not name.isalpha():
        name = input("What is your name?\n").capitalize()
    return name
#AGE
def get_age():
    age = input("How old are you?\n")
    while len(age) == 0 or not age.isdigit():
        age = input("How old are you?\n")
    return int(age)
#HEIGHT
def get_height():
    height = input("What is your height (cm)?\n")
    while len(height) == 0 or not height.isdigit():
        height = input("What is your height (cm)?\n")
    return int(height)
#GREET
def greet_user(name, age, height):
    print(f"Hello {name}, aged {age} and {height}cm tall! 🙏")
# VALIDATION
def validate_user(age, height):
    if age >= 18 and age < 100 and height >= 170:
        print("You are an adult and meet the height requirement of 170 cm. You are free to use this assistant.")
    elif age < 18 and height < 170:
        print("You are not an adult and do not meet the height requirement of 170 cm, so I will have to ask you to leave.")
        exit()
    elif age >= 100:
        print("You exceed the age limit.")
        exit()
    elif age <= 0:
        print("You are not born yet???")
        exit()
    elif age > 18:
        print("You are an adult but don't meet the height requirement of 170 cm.")
        exit()
    else:
        print("You meet the height requirement but are not an adult, so I will have to ask you to leave.")
        exit()
#CALCULATER
def Calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")

    choosess = ["1", "2", "3", "4", "5"]

    choice = input("Enter choice (1/2/3/4/5): ")
    while len(choice) == 0 or not choice.isdigit() or choice not in choosess :
        print("Invalid Choice")
        choice = input("Enter choice (1/2/3/4/5): ")
    
    
    chooses = ["1", "2", "3", "4"]
    if choice in chooses:
        num1 = (input("Enter the first number: "))
        while len(num1) == 0 or not num1.isdigit():
            num1 = (input("Enter the first number: "))
        num1 = float(num1)
        num2 = (input("Enter the second number: "))
        while len(num2) == 0 or not num2.isdigit():
            num2 = (input("Enter the second number: "))
        num2 = float(num2) 
    else:
        num1 = (input("Enter the base: "))
        while len(num1) == 0 or not num1.isdigit():
            num1 = (input("Enter the base: "))
        num1 = float(num1)
        num2 = (input("Enter the power: "))
        while len(num2) == 0 or not num2.isdigit():
            num2 = (input("Enter the power: "))
        num2 = float(num2) 
        

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        print("Result:", num1 / num2 if num2 != 0 else "Error! Division by zero is not allowed.")
    elif choice == "5":
        print("Result:", num1 ** num2)
    else:
        print("Invalid input")
#MAIN MENU
def main_menu():
    functions = {
        "1": "Who are you?",
        "2": "Who made you?",
        "3": "What are you made for?",
        "4": "Calculator",
        "5": "Rock, Paper, Scissors",
    }

    print("This is a list of functions:")
    for key, value in functions.items():
        print(f"{key}. {value}")

    instruction = input("What function do you want?\n")
    
    if instruction == "1":
        print("My name is Neel, your personal assistant.")
    elif instruction == "2":
        print("The world-renowned programmer Noel made me.")
    elif instruction == "3":
        print("I was made to serve you.")
    elif instruction == "4":
        Calculator()
    elif instruction == "5":
        rock_paper_scissors()  # Added Rock, Paper, Scissors function here
    else:
        print("There is no such function.")

# Main Execution
if __name__ == "__main__":
    print("I am your personal assistant.")
    user_name = get_name()
    user_age = get_age()
    user_height = get_height()
    
    greet_user(user_name, user_age, user_height)
    validate_user(user_age, user_height)
    
    while True:
        main_menu()
        repeat = input("Anything else? (y/n)\n")
        if repeat.lower() != "y":
           print("OK then.Bye")
           exit()
