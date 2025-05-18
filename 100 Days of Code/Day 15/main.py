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
    "coffee": 200,
}

def resourcesCheck(drink):
    global resources

    for item in drink:
        if item not in resources or resources[item] < drink[item]:
            print(f'Sorry there is not enough {item}')
            return False
    for item in drink:
        resources[item] -= drink[item]
    return True

def process_coins():
    print('Insert the coins: ')
    quarters = int(input('How many quarters you wanna insert?'))
    dimes = int(input('How many dimes you wanna insert?'))
    nickels = int(input('How many nickels you wanna insert?'))
    pennies = int(input('How many pennies you wanna insert?'))
    return (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)

def render_coffee_paid(coffee_name, coffee_price, machine_coins):
    print(f"Here is ${round(machine_coins - coffee_price, 2)} in change. ")
    print(f'Here is your {coffee_name}. ☕')

machine_is_on = True
while machine_is_on:
    pick = input('What would you like? (espresso/latte/cappuccino):').lower()

    if pick in MENU:
        drink_data = MENU[pick]
        if resourcesCheck(drink_data['ingredients']):
            coins_in_machine = process_coins()
            if coins_in_machine >= drink_data['cost']:
                render_coffee_paid(pick, drink_data['cost'], coins_in_machine)
            else:
                print("Sorry, that's not enough money.")
    elif pick == 'report':
        for resource, amount in resources.items():
            print(f"{resource}: {amount}")
    elif pick == 'off':
        print('The machine is off now!')
        machine_is_on = False
    else:
        print('Invalid input. Please choose espresso, latte or cappuccino.')