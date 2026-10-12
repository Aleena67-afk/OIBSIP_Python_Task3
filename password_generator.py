import random
import string

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Password length must be at least 8.")
    exit()
characters = ""

lowercase = input("Include lowercase letters? (yes/no): ").lower()
if lowercase not in ["yes", "no"]:
    print("Please enter yes or no.")
    exit()

if lowercase == "yes":
    characters += string.ascii_lowercase

uppercase = input("Include uppercase letters? (yes/no): ").lower()
if uppercase not in ["yes", "no"]:
    print("Please enter yes or no.")
    exit()

if uppercase == "yes":
    characters += string.ascii_uppercase

numbers = input("Include numbers? (yes/no): ").lower()
if numbers not in ["yes", "no"]:
    print("Please enter yes or no.")
    exit()

if numbers == "yes":
    characters += string.digits

symbols = input("Include symbols? (yes/no): ").lower()
if symbols not in ["yes", "no"]:
    print("Please enter yes or no.")
    exit()

if symbols == "yes":
    characters += string.punctuation

selected_types = 0

if lowercase == "yes":
    selected_types += 1

if uppercase == "yes":
    selected_types += 1

if numbers == "yes":
    selected_types += 1

if symbols == "yes":
    selected_types += 1

if selected_types < 2:
    print("Please select at least 2 character types.")
    exit()

again = "yes"

while again == "yes":
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated password:", password)

    again = input("Generate another password? (yes/no): ")