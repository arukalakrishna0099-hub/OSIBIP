#BMI CALCULATOR 
#BMI = weight (kg) / height (m) ** 2

def get_float_input(message):
    """"
    safely get a float input from the user
    prevents errors from invalid or negative numbers
    """
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
  
    def get_inches_input(message):
    """
    Safely get inches input (0 to 11) from the user.
    Allows 0 for cases like exactly 5'0".
    """
    while True:
        try:
            value = float(input(message))
            if value < 0 or value >= 12:
                print("Please enter inches between 0 and 11.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number."     
  print("--------BMI Calculator--------\n")
#get weight
weight = get_float_input("Enter your weight in kilograms: ")

#  #height from the user in feet and inches
feet = get_float_input("Enter your height in feet: ")
inches= get_float_input("Enter the remaining inches:")

#convert feet + inches -> meters 
total_inches=(feet * 12) + inches
height_meters= total_inches * 0.0254

#avoid division by zero
if height_meters == 0:
    print("\nError: Height cannot be zero.")
    exit()

#calculate BMI
bmi = weight / (height_meters ** 2)

#ouput the result
print("\n your height in meters is :", round(height_meters, 3))
print("Your BMI is :", round(bmi, 2))

#classify BMI 
if bmi < 18.5:
    category="You are underweight."
elif 18.5 <= bmi < 25:
    category="You have a normal weight."
elif 25 <= bmi < 30:
    category="You are overweight."
else:
    category="You are obese."

print(category)
print("---------------")
