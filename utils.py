def select_action():
    print("What would you like to do?")
    print("A: see product catalogue. \nB: create a new product. \nC: update an existing product. \nD: delete an existing product. \nE: add products to your inventory. \nF: display current inventory. \nG: display inventory value.")
    user_choice = (input("Please enter a letter.")).lower()
    # validate user input?
    if user_choice in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        return user_choice
    print("Invalid input. Please enter a letter from A to G to select your next action.")
    # perform action here or somewhere else?


def execute_action():
    # after calling select_action, depending on the the value of user_choice, execute the corresponding action from the menu (by calling the appropriate Inventory method).
    # use match-case?




def validate_input(input):
    # takes some input as argument
    # checks if the input is of correct type
    # perform other validations