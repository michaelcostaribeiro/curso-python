from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
mm = MoneyMachine()
macchiato = MenuItem('macchiato', 5, 5, 5, 4)
menu.add_drink(macchiato)

working = True

while working == True:
    choice = input(f'Pick your coffee: {menu.get_items()}: ')
    if choice == 'off':
        working = False
        continue
    elif choice == 'report':
        mm.report()
        maker.report()
        continue
    drink = menu.find_drink(choice)
    if maker.is_resource_sufficient(drink):
        if mm.make_payment(drink.cost):
            maker.make_coffee(drink)
            for item in maker.resources:
                maker.resources[item] -= drink.ingredients[item]