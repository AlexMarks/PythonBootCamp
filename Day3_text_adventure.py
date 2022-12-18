print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
def end(num):
    match num:
        case 1:
            print("You walk along the shore, which becomes rockier and eventually gives\n"
                "way to cliffs. The view is immaculate, but the footing leaves something\n"
                "to be desired. Soil crumbles beneath your foot and you plummet.\n"
                "Game over.\n")
        case 2:
            print("At first the water feels refreshing after the hike in the humid summer.\n"
                  "However, you soon feel the fatigue from your trek catching up to your\n"
                  "muscles. You are equidistant from the shore and the island. Oh no.\n"
                  "Game over.")
        case 3:
            print("You reach out for the potion to pull it from the shelf, but find\n"
                "that it is attached to a mechanism. A previously concealed doorway\n"
                "pops open, and you peer through. The treasure!\n"
                "You win!")
        case 4:
            print("You quickly snatch the red potion off of the counter and\n"
                "upend it into your mouth. You instantly catch fire.\n"
                "Game over.")
        case 5:
            print("You sample it. Not bad. You try a bit more before feeling\n"
                "your eyelids grow heavy. A quick nap can't hurt. You find \n"
                "a place to lay down and fall asleep. Forever.\n"
                "Game over.\n")

def scene3():
    potion = input("The boatman eventually notices you and rows up to the bank where \n"
                   "you stand. 'Need a lift?,' he offers. You accept, and the house on\n"
                   "the island slowly looms closer. Upon arrival, you feel an intense thirst.\n"
                   "The boatman tells you to help yourself while he finishes up checking his\n"
                   "fishing traps for the day. You step into the house, and see all manner\n"
                   "of colorful concoctions in the kitchen. Which color do you try: 'blue',\n"
                   "'red', or 'yellow'?\n")
    if potion == 'yellow':
        end(3)
    elif potion == 'red':
        end(4)
    else:
        end(5)
def scene2():
    water = input("After pushing through the brush for some time, you come to a lake.\n"
                  "In the center of the lake, you can see an island that seems to be\n"
                  "inhabited. At the very least you can see smoke from a chimney and a\n"
                  "boat on the water. You can try to swim to the island or wait for the\n"
                  "boatman to notice you. Do you 'wait' or 'swim'?\n")
    if water == "wait":
        scene3()
    else:
        end(2)
def scene1():
    direction = input("You observe your surroundings after saying your goodbyes \n"
                  "to the crew that dropped you off. To your left is a forested \n"
                  "area. To your right, the shoreline stretches into the distance. \n"
                  "Will you go 'left' or 'right'?\n")

    if direction == "left":
        scene2()
    else:
        end(1)

scene1()
