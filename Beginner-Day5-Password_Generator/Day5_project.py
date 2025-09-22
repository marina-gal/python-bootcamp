import random
from operator import concat

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# First option
password = "" # Starting with a string. This variable will change with the 3 loops.
for char in range(0,nr_letters): # Depending on the number of letters the user chooses, it creates a range of size n. As it is a loop, it randomly chooses n times inside the concerned list.
    password += random.choice(letters)
for char in range(0,nr_symbols):
    password += random.choice(symbols)
for char in range(0,nr_numbers):
    password += random.choice(numbers)

print(f"Your password is: {password}")

# Second option
password_list = [] # Starting with a list
for char in range(0,nr_letters): # Depending on the number of letters the user chooses, it creates a range of this size. As it is a loop, it randomly chooses n times inside the concerned list.
    password_list.append(random.choice(letters)) # Instead of concatenate the string, as it is a list, we "append" characters to a list: password_list
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

# With a list: password_list, it is possible to shuffle the elements of a list
print(password_list)
random.shuffle(password_list)
print(password_list)

# Reconverting the list into a string
password = ""
for char in password_list: # with a loop we take each character of the list and we concatenate it in a empty string.
    password += char

print(f"Your password is: {password}")
