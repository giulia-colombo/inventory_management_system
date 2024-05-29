from product import Product
from utils import select_action

class Inventory:
    def __init__(self):
        ## list (of Product instances)
        self.product_catalog = []
        ## dictionary of dictionaries. houses the actual current quantity of all the products
        self.inventory = {}
    
    
    def create_product(self):
        # given a product_name (user input),
        # put in lowercase
        while True:
            product_name = input("Please insert the product name.").lower()
            try:
                # given a unit_price (user input),
                # transform into integer/float
                unit_price = round(float (input("Please insert the unit price. Use '.' for decimals. Don't add currency. Price is automatically rounded for simplicity.")))
                # OPTIONAL: check that they actually used . and that the format is right.
                break
            except ValueError:
                print("Invalid price. Please enter a number.")

        # create a product (SKU) for the product catalogue 
        new_product = Product(product_name, unit_price)
        # append product to product catalogue.
        self.product_catalog.append(new_product)
        # display success message
        print(f"Product {product_name} with unit price {unit_price} has been successfully added to product catalogue.")
        select_action()

     def find_product(self):
        # given a name (user input), check if the object exists
        product_name = input("Please insert the product name to look for it.").lower()
        # if it that product name exists in the product catalague, return the object.
        
        # if it doesn't exist, print an error message


    def add_product(self, product_name, product_quantity):
        # given a product_name (user input),
        # check that the product exists (find_product)
        # given a quantity, calculate the value for that stock
        # add the product to Inventory with the correct stock
        # print output?

    # update_product
    def update_product(self, name, price = None):
        #ask for product name

        #check if product actually exists
            # if product does not exists, display error
            # if it exists, ask what user would like to update
                # if user says name, ask for new name
                # validate input
                # confirm y/n
                # actually update name
                # display_info()

                # if user says price, ask for new price
                # validate input
                # confirm y/n
                # actually update price
                # display_info()

    # update_product_quantity

    # delete_product - #REVIEW from catalogue or inventory??? or both? 
    def delete_product(self, name):
        print(f"Product with name ''{name}'' is about to be deleted. This action cannot be undone. Proceed?")
        reply = input("Please enter yes or no.")
        if reply == "yes":
            del self
            print("Product successfully deleted.")
        elif reply == "no":
            print(f"Product {name} has not been deleted.")
        else:
            print("Please enter yes or no.")
    
    def display_product_catalogue(self, product_catalogue):
        # print all the items (SKUs) in product_catalogue

    def display_inventory_levels(self, inventory):
        # display current inventory levels (amount of every product)

    def display_inventory_value(self, inventory):
        # display current inventory value (unit price * quantity per product)
