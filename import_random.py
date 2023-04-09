import random
import time
import string

def password_generator(password_length, include_numbers, include_symbols, include_capital_letters):
    characters = string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    if include_capital_letters:
        characters = string.ascii_letters.upper() + characters
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password

def password_creator():
    while True:
        password_input_1 = input("Enter your password: ").rstrip()
        if len(password_input_1) < 8:
            print("Password length is too short, please use not less than 8 symbols")
        else:
            password_input_2 = input("Repeat your password: ").rstrip()
            if password_input_1 == password_input_2:
                return password_input_1
            else:
                print("Passwords do not match!")
                time.sleep(2)

def generator_inputs():
    while True:
        password_length = int(input("Enter the number of characters for the password: "))
        if password_length < 8:
            print("Password length is too short, please use not less than 8 symbols")
        else:
            questions = ["Include numbers? (y/n): ",
                         "Include symbols? (y/n): ",
                         "Include capital letters? (y/n): "]
            include_numbers, include_symbols, include_capital_letters = ask_yes_no(questions)
            return password_length, include_numbers, include_symbols, include_capital_letters

def ask_yes_no(questions):
    answers = []
    for question in questions:
        while True:
            answer = input(question).lower()
            if answer == "y":
                answers.append(True)
                break
            elif answer == "n":
                answers.append(False)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    return tuple(answers)



def login():
    # Prompts the user for their username and password, and checks if they match the stored account details in the accounts.txt file.
    # If the details match, returns True, otherwise, returns False.

    username = input("Enter your username: ").lower().rstrip()
    password = input("Enter your password: ").lower().rstrip()

    # check if username and password match the stored account details
    with open("accounts.txt", "r") as f:
        count = 0
        for line in f:
            stored_username, stored_password = line.rstrip().split(" ")
            if username == stored_username and password == stored_password:
                count += 1
        if count > 0:
            print("Login successful")
        else:
            print("Invalid username or password")


def register():
    # Prompts the user for their username and password, and saves them to the accounts.txt file.
    username = input("Enter your username: ").lower().rstrip()
    with open("accounts.txt", "r") as f:
        accounts = f.readlines()
        for account in accounts:
            if username in account:
                print("Username already exists")
                return
    password_choice = input("""Would you like to enter your own password or generate one? 
    (enter 'enter' or 'generate'): """)
    if password_choice == "enter":
        password = password_creator()
    elif password_choice == "generate":
        password_length, include_numbers, include_symbols, include_capital_letters = generator_inputs()
        password = password_generator(password_length, include_numbers, include_symbols, include_capital_letters)
        print(f"Your generated password is: {password}")
    else:
        print("Invalid input")
        return

    # save username and password to accounts.txt file
    with open("accounts.txt", "a") as f:
        f.write(f"{username} {password}\n")
    print("Account created successfully")


def view_account():
    # Reads the account details from the accounts.txt file and displays them on the screen for the logged in user.
    # find the account details for the specified username

    with open("accounts.txt", "r") as f:
        for line in f:
            stored_username, stored_password = line.rstrip().split(" ")
            if username == stored_username:
                print(f"Username: {stored_username}, Password: {stored_password}")
                return
            print("Account not found")


def menu():
    # Displays the options (register, login, view account, save file, and exit), prompts the user to choose an option, and
    # calls the appropriate function based on the user's choice.

    while True:
        print("Select an option:")
        print("1. Login")
        print("2. Register")
        print("3. View Account")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            view_account()
        elif choice == "4":
            print("Exiting program...")
            time.sleep(2)
            break
        else:
            print("Invalid choice")
menu()