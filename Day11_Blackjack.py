import random
import time

###Globals###
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0
score = [0, 0]

###Support functions###
def appraise(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

def deal():
    player_hand.clear()
    dealer_hand.clear()
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

def hit(hand):
    new_card = random.choice(cards)
    print(f"A {new_card} is drawn from the deck.")
    hand.append(new_card)
    return appraise(hand)

def print_hands(show):
    print(f"Your hand is {player_hand} with a total of {player_total}.")
    if show:
        print(f"The dealer's hand is {dealer_hand} with a total of {dealer_total}.")
    else:
        temp_dealer = dealer_hand.copy()
        temp_dealer[0] = '?'
        print(f"The dealer's hand shows {temp_dealer}.")

def settle_up():
    print_hands(True)
    if player_total <= 21 and (player_total > dealer_total or dealer_total > 21):
        print("You won!!!")
        score[0] = score[0] + 1
    elif player_total == dealer_total:
        print("It's a draw!")
    else:
        print("The dealer wins. Try again next round.")
        score[1] = score[1] + 1
    readability_break()
    print(f"You have won {score[0]} hand(s), and the dealer has won {score[1]} hand(s).")

def readability_break(sec = 2):
    print()
    time.sleep(sec)

####Gameplay###
def round():
    deal()
    global player_total
    player_total = appraise(player_hand)
    global dealer_total
    dealer_total = appraise(dealer_hand)

    done = False
    while player_total < 21 and not done:
        print_hands(False)
        hit_it = input("Would you like to hit? (Y or N): ").lower()
        if hit_it in ['y', 'yes']:
            player_total = hit(player_hand)
            if player_total > 21:
                print("That's over 21. You busted!")
                readability_break()
        elif hit_it in ['n', 'no']:
            done = True
            print("Now it is the dealer's turn.")
            readability_break(4)
        else:
            print("Please enter a valid input.")


    if player_total <= 21:
        done = False
        while (dealer_total < player_total or (dealer_total == player_total and dealer_total <= 13)) and not done:
            print_hands(True)
            if player_total > dealer_total:
                print("The dealer hits.")
                dealer_total = hit(dealer_hand)
                if dealer_total > 21:
                    print("The dealer busted!")
            else:
                print("The dealer passes.")
                done = True
            readability_break(4)
    settle_up()

###Start of code###
print(logo)
print("Welcome to Blackjack! The goal is to get your total as close to 21 as possible without going over. "
      "Picture cards count as 10s, and an ace can be worth 11 or 1.")
playing = True
while playing:
    round()
    cont = ''
    while cont not in ['y', 'yes', 'n', 'no']:
        cont = input("Would you like to play another round?(Y or N): ").lower()
    if cont in ['y', 'yes']:
        continue
    elif cont in ['n', 'no']:
        playing = False
        print("Thanks for playing!")


