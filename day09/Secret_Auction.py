from art import logo
import os
print(logo)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

dict = {} #Want {Jin: 102, John: 220}
should_continue = True

while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    dict[name] = bid
    more_bidders = input("Are there other users who want to bid? yes or no ")
    if more_bidders == "no":
        should_continue = False
    elif more_bidders == "yes":
        clear_screen()

highest_bid = 0
winner = ""
for name in dict:
    if dict[name] > highest_bid:
        highest_bid = dict[name]
        winner = name

print(f"Winning bid is {highest_bid} by {winner}")
