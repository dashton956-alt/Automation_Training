# Coffee shop robert 

print("Welcome to Robert's Coffee Shop!")

name = input("What's your name?") 

print("Hi " + name + ", what would you like to order?") 

menu = ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"] 

print("Menu:") 

for item in menu: print("- " + item) 

order = input("Please enter your order: ") 

cost = 5

amount = input("How many would you like?")

total = cost * int(amount)

if order in menu: print("\nGreat choice, " + name + "! \nYour " + order + " will cost" + " £" + str(total) + "\nIt will be ready shortly" ) 

else: print("Sorry, we don't have that on the menu. Please choose from the available options.")