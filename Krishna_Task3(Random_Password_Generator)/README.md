# 🔐 Random Password Generator

A simple Python-based Random Password Generator that creates secure passwords based on user preferences. Users can choose whether to include lowercase letters, uppercase letters, digits, and special characters while specifying the desired password length.

## 📌 Features

- Generate random and secure passwords
- User-defined password length
- Option to include:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Special characters (!, @, #, etc.)
- Input validation for password length
- Ensures at least one character from each selected category
- Handles invalid user inputs gracefully

## 🛠️ Technologies Used

- Python 3
- Built-in Python Modules:
  - random
  - string
  - sys

## 📂 Project Structure

random-password-generator/
│
├── random_password_generator.py
└── README.md

## 🚀 How to Run

### Clone the Repository

---------- Random Password Generator ----------

Enter the password length (minimum 4): 12

Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y

Generated Password:
A7#kP2!xQ9@m

Keep it safe!

## ⚙️ Validation Checks

The program validates:

- Password length must be at least 4 characters.
- User must select at least one character type.
- Password length must be sufficient to accommodate all selected character categories.
- Invalid numeric inputs are handled using exception handling.

## 🧠 Concepts Demonstrated

This project demonstrates the use of:

- Python Variables
- Loops (`while`)
- Conditional Statements (`if`)
- Exception Handling (`try-except`)
- Lists
- String Manipulation
- Randomization
- Python Standard Library Modules

## 🔒 Password Generation Logic

1. Take password length from the user.
2. Ask which character categories to include.
3. Add at least one character from each selected category.
4. Fill the remaining length with random characters from the selected character set.
5. Shuffle the characters for better randomness.
6. Display the generated password.

## 🎯 Future Enhancements

- Password Strength Meter
- GUI Version using Tkinter
- Generate Multiple Passwords at Once
- Copy Password to Clipboard
- Save Generated Passwords to a File
- Exclude Similar Characters (0/O, l/I)

## 👨‍💻 Author

**Krishna**

GitHub: https://github.com/arukalakrishna0099-hub

---

If you found this project useful, consider giving it a ⭐ on GitHub.
