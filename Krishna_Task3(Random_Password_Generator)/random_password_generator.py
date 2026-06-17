import random
import string
import sys
#initialize character sets
print("----------Random Password Generator-----")

#take password length input from the user
while True:
    length_input=input("enter the password length (minimum 4):")
    try:
        length = int(length_input)
        if length <4:
            print("password length should at least 4.please try again.\n")
        else:
            break
    except ValueError:
        print(" Please enter a valid number.")

#ask user what to include in the passwrod 
use_lower=input("inlcude lowercase letter? (y/n)").strip().lower()
use_upper=input("inlcude uppercase letter? (y/n)").strip().lower()
use_digits=input("include digits ? (y/n)").strip().lower()
use_special=input("include special characters ? (y/n)").strip().lower()
#check if at least one type is selected 
if use_lower!="y" and use_upper!="y" and use_digits!="y" and use_special!="y":
    print("error: you must select at least one character type")
    sys.exit(1)
        
#build a character set based on the user choices
char_set=""
password_list=[]

if use_lower=="y":
    char_set+=string.ascii_lowercase
    password_list.append(random.choice(string.ascii_lowercase))
if use_upper=="y":
    char_set+=string.ascii_uppercase
    password_list.append(random.choice(string.ascii_uppercase))
if use_digits=="y":
    char_set+=string.digits
    password_list.append(random.choice(string.digits))
if use_special=="y":
    char_set+=string.punctuation
    password_list.append(random.choice(string.punctuation))

# if user gave very small lenght (less than the slected types) adjust the length 
if length < len(password_list):
    print("\n error:passsword lenght is too small or selected options")
    print(f"You selected {len(password_list)} character types, but the password length is only {length}.")
    sys.exit(1)

#fill the rest of the password with random characters from the char_set
while len(password_list) < length:
        password_list.append(random.choice(char_set))

#shuffle and create the final password
random.shuffle(password_list)
password="".join(password_list)
print("\nGenerated Password:")
print(password)
print("\n keep it safe!")
    
