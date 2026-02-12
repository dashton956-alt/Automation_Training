# Coffee shop robert 

print("Welcome to Robert's Coffee Shop!")

name = input("What's your name?") 

print("Hi " + name + ", what would you like to order?") 

menu = ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"] 

print("Menu:") 

for item in menu: print("- " + item) 

order = input("Please enter your order: ") 

if order in menu: print("Great choice, " + name + "! Your " + order + " will be ready shortly.") 

else: print("Sorry, we don't have that on the menu. Please choose from the available options.")