# Password-Strength-checker.py

import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    
    # Character category counters
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    strength = 0
    remarks = ''

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    # Strength logic
    if lower_count > 0:
        strength += 1
    if upper_count > 0:
        strength += 1
    if num_count > 0:
        strength += 1
    if special_count > 0:
        strength += 1
    if wspace_count > 0:
        strength += 1  # Usually whitespace is discouraged, but keeping for scoring logic match

    # Remarks based on strength
    if strength == 1:
        remarks = "Very Bad Password! ❌ Change ASAP."
    elif strength == 2:
        remarks = "Not a Good Password! ⚠️ Consider changing."
    elif strength == 3:
        remarks = "Weak Password. ⚠️ Try to improve."
    elif strength == 4:
        remarks = "Strong Password. 👍 Almost there!"
    elif strength == 5:
        remarks = "Excellent! ✅ Very Strong Password."

    # Output result
    print("\n--- Password Analysis ---")
    print(f"Lowercase letters     : {lower_count}")
    print(f"Uppercase letters     : {upper_count}")
    print(f"Numeric digits        : {num_count}")
    print(f"Whitespace characters : {wspace_count}")
    print(f"Special characters    : {special_count}")
    print(f"Password Strength     : {strength}/5")
    print(f"Hint: {remarks}\n")

def ask_pwd(again=False):
    while True:
        if again:
            choice = input("Do you want to check another password? (y/n): ").lower()
        else:
            choice = input("Do you want to check a password? (y/n): ").lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == '__main__':
    print("+++ Welcome to the Password Strength Checker +++")
    while ask_pwd():
        check_pwd()

