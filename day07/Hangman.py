import random
from Hangmanpic import HANGMANPICS
from Hangmanpic import words

#Generate a random word
chosen_word = random.choice(words)
print(f"Chosen word is {chosen_word}")

#Generate as many blanks as letters in word
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

#Have they run out of lives
lives = 6

end_of_game = False
stages = 0

while not end_of_game:

    #Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    #Is the guessed letter in the word
    for position in range(word_length):
        if chosen_word[position] == guess:
            # Replace the blank with the letter
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(HANGMANPICS[stages])
        stages += 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Are all the blanks filled
    if display.count("_") == 0:
        end_of_game = True
        print("You win.")

    print(f"{' '.join(display)}")

