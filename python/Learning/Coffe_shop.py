# Coffee shop robert 

print("Welcome to Robert's Coffee Shop!")

name = input("What's your name?") 

    
def order():
    print("Hi " + name + ", what would you like to order?") 

    menu = ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"] 

    print("Menu:") 

    for item in menu: print("- " + item) 

    order = input("Please enter your order: ") 

    cost = 5

    amount = input("How many would you like?")

    total = cost * int(amount)

    if order in menu: print("\nGreat choice, " + name + "! \nYour " + order + " will cost" + " £ "+ str(total) + "\nIt will be ready shortly" ) 

    else: print("Sorry, we don't have that on the menu. Please choose from the available options.")


if name.lower() in ["ben", "pat"]:
    evil_status = input("Are you still evil?\n")
    if evil_status == "Yes" or evil_status == "yes":
        print(" Your not welcome here! get out")
        exit()
    else:
        order()
        exit()
else:
    order()