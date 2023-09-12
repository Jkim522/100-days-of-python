import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors")
player_choice = int(input("Press 1 for Rock, 2 for Paper, 3 for Scissors "))

computer_choice = random.randint(1,3)

if player_choice == 1 and computer_choice == 2:
    print(rock)
    print(paper)
    print("Paper beats rock. You lose")
elif player_choice == 1 and computer_choice == 3:
    print(rock)
    print(scissors)
    print("Rock beats scissors. You win!")
elif player_choice == 1 and computer_choice == 1:
    print(rock)
    print(rock)
    print("Computer chose rock. Draw.")
elif player_choice == 2 and computer_choice == 1:
    print(paper)
    print(rock)
    print("Paper beats rock. You win!")
elif player_choice == 2 and computer_choice == 3:
    print(paper)
    print(scissors)
    print("Scissors beats paper. You lose.")
elif player_choice == 2 and computer_choice == 2:
    print(paper)
    print(paper)
    print("Computer chose paper. Draw")
elif player_choice == 3 and computer_choice == 1:
    print(scissors)
    print(rock)
    print("Rock beats scissors. You lose.")
elif player_choice == 3 and computer_choice == 2:
    print(scissors)
    print(paper)
    print("Scissors beats paper. You win!")
elif player_choice == 3 and computer_choice == 3:
    print(scissors)
    print(scissors)
    print("Computer chose scissors. Draw")
