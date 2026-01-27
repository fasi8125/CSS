Menu = {
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
    },
    "tea": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "tea": 10,
        },
        "cost": 1.0,
    },
    "coffee": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "coffee": 15,
        },
        "cost": 1.2,
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "tea": 50,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy ☕")


is_on = True

while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino/tea/coffee): "
    ).lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Tea: {resources['tea']}g")
        print(f"Money: ${profit}")

    elif choice in Menu:
        drink = Menu[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])

    else:
        print("Invalid choice ❌")

'''
# Coffee Machine Simulation
#outputs a menu of drinks, processes user input for drink selection,
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\14.py"
What would you like? (espresso/latte/cappuccino/tea/coffee): tea
Please insert coins.
how many quarters?: 1
how many dimes?: 1
how many nickels?: 1
how many pennies?: 1
Sorry that's not enough money. Money refunded.
What would you like? (espresso/latte/cappuccino/tea/coffee): coffee
Please insert coins.
how many quarters?: 4
how many dimes?: 4
how many nickels?: 4
how many pennies?: 4
Here is $0.44 in change.
Here is your coffee. Enjoy ☕
What would you like? (espresso/latte/cappuccino/tea/coffee): report
Water: 200ml
Milk: 150ml
Coffee: 85g
Tea: 50g
Money: $1.2
What would you like? (espresso/latte/cappuccino/tea/coffee): latte 
Please insert coins.
how many quarters?: 3
how many dimes?: 3
how many nickels?: 3
how many pennies?: 3
Sorry that's not enough money. Money refunded.
What would you like? (espresso/latte/cappuccino/tea/coffee): latte 
Please insert coins.
how many quarters?: 12
how many dimes?: 12
how many nickels?: 12
how many pennies?: 12
Here is $2.42 in change.
Here is your latte. Enjoy ☕
What would you like? (espresso/latte/cappuccino/tea/coffee): report
Water: 0ml
Milk: 0ml
Coffee: 61g
Tea: 50g
Money: $3.7
What would you like? (espresso/latte/cappuccino/tea/coffee): tea
Sorry there is not enough water.
What would you like? (espresso/latte/cappuccino/tea/coffee): off
'''