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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee(user_coffee):
    for item in user_coffee["ingredients"]:
        resources[item] -= user_coffee["ingredients"][item]


def is_resource_sufficient(required):
    is_enough = True
    for item in required:
        if required[item] > resources[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False

    return is_enough


def refill():
    resources['water'] += int(input("How much water you want to add: "))
    resources['milk'] += int(input("How much milk you want to add: "))
    resources['coffee'] += int(input("How much coffee you want to add: "))


def process_coins():
    print("Please insert coins ")
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunds")
        return False


is_on = True
profit = 0
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False

    elif choice == "report":

        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: ${profit}")
    elif choice == "refill":
        refill()
        print("Refilling Completed")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                coffee(drink)
                print(f"Here is your {choice} coffee")
