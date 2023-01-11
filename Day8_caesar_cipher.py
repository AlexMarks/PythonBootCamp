

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, direction):
    new_message = ""
    for l in message:
        try:
            i = letters.index(l)
            if (direction == "encode"):
                new_message += letters[(i + shift) % 26]
            elif(direction == "decode"):
                new_message += letters[(i - shift) % 26]
        except ValueError:
            new_message += l

    return new_message

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
cmd = ""
while cmd != "exit":
    cmd = input("Type 'encode', 'decode', or 'exit': ")
    if cmd == "encode" or cmd == "decode":
        message = input("Enter the message that you want to use: ").lower()
        shift = input("Enter the number to shift by: ")
        try:
            shift = int(shift) % 26
        except:
            print("Invalid value entered for shift. Please enter a numeric value next time.")
            continue
        result = caesar(message, shift, cmd)
        print(f"Your message now looks like: {result}")
    elif cmd != "exit":
        print("Please enter a valid command from the list.")


