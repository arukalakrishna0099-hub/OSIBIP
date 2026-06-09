# BMI Calculator 🏋️‍♂️

A simple Python-based Body Mass Index (BMI) Calculator that takes a user's weight and height (in feet and inches), converts the height to meters, calculates BMI, and classifies the result according to standard BMI categories.

## 📌 Features

- User-friendly console interface
- Input validation for weight and height
- Prevents negative and invalid inputs
- Converts height from feet and inches to meters
- Calculates BMI using the standard formula
- Displays BMI category:
  - Underweight
  - Normal Weight
  - Overweight
  - Obese

## 🧮 BMI Formula

\[
BMI = \frac{Weight (kg)}{Height (m)^2}
\]

## 🚀 How It Works

1. Enter your weight in kilograms.
2. Enter your height in feet.
3. Enter the remaining inches.
4. The program:
   - Converts height into meters.
   - Calculates BMI.
   - Displays the BMI value.
   - Shows the corresponding BMI category.

## 📂 Project Structure

BMI-Calculator/
│
├── bmi_calculator.py
└── README.md


--------BMI Calculator--------

Enter your weight in kilograms: 70
Enter your height in feet: 5
Enter the remaining inches: 8

Your height in meters is : 1.727
Your BMI is : 23.46
You have a normal weight.
---------------

## 📊 BMI Categories

| BMI Range | Category |
|------------|------------|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal Weight |
| 25.0 - 29.9 | Overweight |
| 30.0 and above | Obese |

## 🛡️ Input Validation

The program ensures:
- Only numeric values are accepted.
- Negative or zero values are rejected.
- Invalid inputs do not crash the program.

## 🎯 Learning Objectives

This project demonstrates:

- Functions in Python
- Exception Handling (`try-except`)
- Loops and Conditional Statements
- User Input Validation
- Mathematical Calculations
- Code Organization and Readability

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Krishna**

GitHub: https://github.com/arukalakrishna0099-hub
