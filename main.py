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
#coins and important stuff
not_enough = True
not_enough_money = True
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
user_money = 0


def money_calcu(type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    change = total - MENU[type]['cost']
    if change < 0:
        print(f"Not enough money for this coffee, refunding {round(total, 2)}$")
        return False
    else:
        print(f"here's your change {round(change, 2)}. Enjoy your {type.capitalize()}")


def resources_calcu():
    if resources['water'] < coffe_selected_water:
        print('Sorry there is not enough water.')
        return False
    elif resources['coffee'] < coffe_selected_coffee:
        print('Sorry there is not enough coffee.')
        return False
    if user_command == 'latte' or user_command == 'cappuccino':
        if resources['milk'] < coffe_selected_milk:
            print('Sorry there is not enough milk.')
            return False
    else:
        return True


def resources_reduce(type):
    resources['water'] -= MENU[type]['ingredients']['water']
    resources['coffee'] -= MENU[type]['ingredients']['coffee']
    if type == 'latte' or type == 'cappuccino':
        resources['milk'] -= MENU[type]['ingredients']['milk']


def machine_resources():
    for key, value in resources.items():
        print(f"{key} : {value}")


while not_enough:
    not_enough_money = True
    user_command = str(input("WHat would you like? (Espresso/Latte/Cappuccino): ")).lower()
    if user_command == "report":
        machine_resources()
        continue
    if user_command == "espresso" or user_command == 'latte' or user_command == 'cappuccino':
        coffe_selected_coffee = MENU[user_command]['ingredients']['coffee']
        coffe_selected_water = MENU[user_command]['ingredients']['water']
    if user_command == 'latte' or user_command == 'cappuccino':
        coffe_selected_milk = MENU[user_command]['ingredients']['milk']
    not_enough = resources_calcu()
    not_enough_money = money_calcu(user_command)
    if not_enough_money == False:
        continue
    resources_reduce(user_command)
