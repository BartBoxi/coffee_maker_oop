import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Print report
# Check if the resources are sufficient
# Process coins
# Check transaction successful?
# Make coffee

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem()


is_on = True


coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ? ({options}) ")
    if choice == "off":
        coffee_maker.report()







