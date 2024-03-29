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

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def 

power_on = True

while power_on:
    choice = input("What would you like? Espresso/latte/cappuccino? : ").lower()
    if choice == "off".lower():
        power_on = False
    elif choice == "report":
        print(resources["water"])
        print(resources["milk"])
        print(resources["coffee"])
        print(profit)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"])
            payment = process_coins()