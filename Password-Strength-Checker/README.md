# Password Strength Checker

A simple Python command-line tool to evaluate the strength of a password based on character diversity. This tool gives a detailed analysis and rating of your password's security level.

# Features

- Detects:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
  - Whitespace characters (not recommended, but included for score tracking)
- Scores password strength on a scale of 1 to 5
- Provides helpful remarks based on the strength
- Uses `getpass` to securely input the password (hides typed characters)

# Requirements

- Python 3.x  
- No external libraries required

# How to Run

1. Clone this repository or download the Python script.
2. Open a terminal or command prompt.
3. Run the script using:

```bash
python Password-Strength-checker.py
