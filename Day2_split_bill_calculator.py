bill_total = float(input("What is the bill total including tax?\n$"))
people = int(input("How many people are splitting?\n"))
tip_percent = float(input("What percent tip do you want to leave?\n"))/100

share = round((bill_total / people) * (1 + tip_percent), 2)
formated_share = "{:.2f}".format(share)
print("Each person pays $" + formated_share)