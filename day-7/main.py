import random
import hangman_dictionary
import hangman_art


# Logo print
print(hangman_art.logo)

# Declarations
random_word = random.choice(hangman_dictionary.dictionary)
lives = 6           # because stages are 7


# hint for testing app
# print(random_word)

# blanking

display = []

for i in random_word:
    display += '_'

print(display)


# Game process

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ")

    # Caution: if user writes the letter which was aleady written 
    if guess in display:
        print(f"{guess} is already pressed")

    for position in range(len(random_word)):
        letter = random_word[position]
        if guess == letter:
            display[position] = letter

    print(display)

    # Tracking user's lives, when user lose the game
    if guess not in random_word:
        print(f"{guess} was not in the word, so you lose a life")
        print(hangman_art.stages[lives - 1])
        lives -= 1

        if lives == 0:
            print("You lose!")
            end_of_game = True
            print(f"Word was {random_word}")

    # when user wins
    if '_' not in display:
        end_of_game = True
        print("You win!")

    

































# # hint 
# print(random_word)

# # Blanking

# blanks = []

# for blank in range(len(random_word)):
#     blanks.append("_")
# print(blanks)

# user_guess = input("Guess a letter: ").lower()


# for position in range(len(random_word)):
#     letter = random_word[position]
#     if user_guess == letter:
#         blanks[position] = letter

# print(blanks)