import random
from Day7_hangman_resources import stages, logo, word_list

#set up for the game
print(logo)

letter_bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = list(random.choice(word_list))
solution = []
lives = 6

for letter in word:
    solution.append("_")

def player_status():
    print(stages[lives])
    print(solution)
    print(f"You have {lives} lives left.\n")

#Ask player to guess letters
while (lives > 0) and ("_" in solution):
    player_status()

    print("Your remaining letters are: ")
    print(letter_bank)
    guess = input("Guess a letter: ").lower()
    while guess not in letter_bank:
        print("Try again. Choose a letter from the letter bank.")
        guess = input("Guess a letter: ").lower()
    letter_bank.remove(guess)


    #Check guess against the solution
    letter_found = False
    for index, letter in enumerate(word):
        if letter == guess:
            solution[index] = letter
            letter_found = True

    if not letter_found:
        lives = lives - 1
        print ("There is no " + guess + " in the word.")

#print results
player_status()
if "_" not in solution:
    print("Congratulations! You won hangman!")
else:
    print("Sorry, you are out of lives. The answer was: ")
    print(word)