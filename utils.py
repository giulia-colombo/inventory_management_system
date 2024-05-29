

def select_action():
    '''Displays a menu of actions for the user and gets a valid choice from user.'''
    print("What would you like to do?")
    print("A: see product catalog. \nB: create a new product. \nC: delete an existing product from catalog.  \nD: add products to your inventory. \nE: delete an existing product from inventory.\nF: display current inventory. \nG: display inventory value. \nQ: quit the program.")

    while True:
        choice = (input("Please enter a letter.")).lower()
    # validate user input?
        if choice in ['a', 'b', 'c', 'd', 'e', 'f', 'g','q']:
            return choice
        else:
            print("Invalid input. Please enter a valid letter from the menup to select your next action.")
    # perform action here or somewhere else?


def execute_action(inventory, choice):
    '''Executes an action based on the user's choice'''
    match choice:
        case 'a':
            inventory.print_product_catalog()
        case 'b':
            inventory.create_product()
        case 'c':
            inventory.delete_product_catalog()
        case 'd':
            inventory.add_product()
        case 'e':
            inventory.delete_product_inventory()
        case 'f':
            inventory.display_inventory_levels()
        case 'q':
            print('Quitting the program.')
            exit()
        case '_':
            print("Invalid input. Please enter a letter from A to G or Q to quit.")
