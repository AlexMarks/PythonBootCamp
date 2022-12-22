import random

def art(move):
    if move=="rock":
        return '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''
    elif move=="paper":
        return '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    else:
        return '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


moves = ["rock","paper","scissors"]
player = input("Rock, paper, or scissors? ").lower()
while player not in moves:
    player = input("Please type a valid input. 'rock', 'paper', or 'scissors'? ")
computer = moves[random.randint(0,2)]
print("You chose " + player)
print(art(player))
print("The computer chose " + computer)
print(art(computer))

if player == computer:
    print("The game is a draw!")
elif (player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="rock"):
    print("You win!")
else:
    print("You lose... better luck next time.")