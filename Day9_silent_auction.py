import os

#set-up
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the silent auction.")

bids = {}

item = input("Enter the item to be auctioned: ")

#Bidding process
more_bidders = True
while more_bidders:
    print(f"The lot being auctioned is {item}")
    need_input = True
    while need_input:
        name = input("Please enter your name: ")
        if name in bids.keys():
            print("That name is in use. Try using an alternate name for yourself.")
            continue
        else:
            need_input = False

    need_input = True
    while need_input:
        try:
            bid = round(float(input("How much will you bid?: $")),2)
        except:
            print("Please enter a valid numerical amount.")

        bids[name] = bid
        need_input = False

    need_input = True
    while need_input:
        more = input("Are there any more bidders? 'yes' or 'no'?: ").lower()
        if more == "no":
            more_bidders = False
            need_input = False
        elif more == "yes":
            need_input = False
        else:
            print("Sorry, that is an invalid answer.")
    #clear console so next bidder cannot see previous bid
    os.system('cls')

#Determine and display results
top_bid = 0
winner = ["No Winner"]
for n, b in bids.items():
    if b > top_bid:
        top_bid = b
        winner = [n]
    elif b == top_bid:
        winner.append(n)

formatted_bid = "{:.2f}".format(top_bid)
if len(winner) > 1:
    print(f"There is a tie for top bid of ${formatted_bid} by: ", end=" ")
    for i, w in enumerate(winner):
        print (w, end=" ")
        if i < (len(winner) - 2):
            print(", ", end=" ")
        elif i == (len(winner) - 2):
            print(" and ", end=" ")
else:
    print(f"The top bidder is {winner[0]} with a bid of ${formatted_bid}!")
