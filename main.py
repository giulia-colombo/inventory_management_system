# Project Description:
# Develop a command-line application to manage inventory for a small business. This system should allow the user to add new products, update existing product quantities, and delete products. It should also provide functionality to display the inventory and visualize inventory data through plots.

# Requirements:
# Use at least two classes: Product and Inventory.
# Implement loops to iterate through inventory items.
# Use if conditions to check for product existence and validity of operations.
# Utilize lists to store product instances.
# Create at least two plots: one for inventory levels and another for the value of the inventory.
# Develop a custom library to handle inventory operations.
# Write at least 40 lines of code.
from classes.inventory import Inventory
from utils import select_action, execute_action

my_inventory = Inventory()

def main():
    while True:
        choice = select_action()
        if choice ==  'q':
            break
        execute_action(my_inventory, choice)

if __name__ == '__main__':
    main()




