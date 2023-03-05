#Step 5
from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo

print("Welcome to hangman game \n")
print(logo)

# pick a random word_list
chosen_word = random.choice(word_list)
print(chosen_word)

#replace the characters with dashes
display = []
for char in chosen_word:
    display += '_'

#initalize number of lives
lives = 6
end_game = False
already_guess = []

while not end_game:
    if "_" in display:

        guess = input("Guess a letter in the word: ").lower()
        clear()

        if guess not in already_guess:
            if guess in chosen_word:
                for i in range(len(chosen_word)):
                    if guess == chosen_word[i]:
                        display[i] = guess
            else:
                lives -= 1
                print(f"The letter you chose is not in the word\n")
        else:
            print(f"You have already guessed the letter {guess}\n")

        already_guess += guess

        print(f"{' '.join(display)}")
        print(stages[lives])

        if lives == 0:
            print(f"Game over, the word was {chosen_word} you lose")
            end_game = True

    else:
        print("Game over, you win")
        end_game = True
