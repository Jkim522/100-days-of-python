import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J', 'K']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator")
nr_letters = int(input("How many letters would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))

password_list = []

for x in range(nr_letters):
    password_list += letters[random.randint(0,21)]

for x in range(nr_numbers):
    password_list += numbers[random.randint(0,9)]

for x in range(nr_symbols):
    password_list += symbols[random.randint(0,8)]

random.shuffle(password_list)

password = ''
for char in password_list:
    password += char

print(f"Password is {password}")
