from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}






products = {
    #"key": value the synatx to make dictionay
    "water":100,
    "milk":50,
    "coffee":90,
    "money":3,

}



def is_resource_sufficient(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return round(total, 2)  # rounding to 2 decimal places



def is_trtion_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} your change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not the sufficient amount . Money refunded")
        return False



#every time someone orders a drink
def make_coffee(drink):
    order_ingredients = MENU[drink]["ingredients"]
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Dispensing your {drink}... Enjoy!\n")








# Prompt user by asking “
def coffee_order():
    while True:

        order = input("What would you like? (espresso/latte/cappuccino/report/off):").lower()

        if order == "off":
            print("Maintainer denied the access. shuting dwon the coffee machine. bye")

        elif order in ['espresso', 'latte', 'cappuccino']:
            if is_resource_sufficient(order):
                payment = process_coins()
                if is_trtion_successful(payment, MENU[order]["cost"]):
                    make_coffee(order)


        elif order == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")

        elif order == ['espresso', 'latte', 'cappuccino']:
            make_coffee(order)
        else:
            print("Sorry we dont serve that. Please choose espresso, latte, or cappuccino.\n")


coffee_order()


    


# Turn off the Coffee Machine by entering  off​ to the prompt.

