import sys
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
cash_register = MoneyMachine()

machine_continue = True

while machine_continue:
    drink = menu.menu
    answer = input(f"What would you like? {menu.get_items()}: ").lower()
    if answer == "report":
        coffee_maker.report()
        cash_register.report()
    elif answer == "off":
        machine_continue = False
        sys.exit(0)
    else:
        drink = menu.find_drink(answer)

    if drink is not None:
        if coffee_maker.is_resource_sufficient(drink) is False:
            break
        cash_register.make_payment(drink.cost)
        coffee_maker.make_coffee(drink)



