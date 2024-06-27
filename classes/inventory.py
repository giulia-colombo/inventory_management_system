from classes.product import Product
from utils import select_action
# import matplotlib as plt
# import numpy as np


class Inventory:
    def __init__(self):
        ## list (of Product instances)
        self.product_catalog = []
        ## dictionary of dictionaries. houses the actual current quantity of all the products
        self.inventory = []
    
    
    def create_product(self):
        ''' Creates a new product and adds it to product_catalog '''
        # given a product_name (user input),
        # put in lowercase
        while True:
            product_name = input("Please insert the product name.\n\n").lower()
            # check that user has not entered empty string
            if not product_name:
                print("Product name cannot be empty. Please try again.")
                continue
            # check if a product with that name already exists in the product catalog.
            elif any(product.name.lower() == product_name for product in self.product_catalog):
                print(f"Product with name '{product_name}' already exists in catalog.\n\n")
                return None
            else:
                try:
                    # given a unit_price (user input),
                    # transform into integer/float
                    unit_price = round(float (input("Please insert the unit price. Use '.' for decimals. Don't add currency. Price is automatically rounded for simplicity.\n\n")))
                    # OPTIONAL: check that they actually used . and that the format is right.
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.\n\n")

        # create a product (SKU) for the product catalog 
        new_product = Product(product_name, unit_price)
        # append product to product catalog.
        self.product_catalog.append(new_product)
        # display success message
        print(f"Product {product_name} with unit price {unit_price} has been successfully added to product catalog.\n\n")
        return new_product

    def find_product(self):
        # given a name (user input), check if the object exists
        product_name = input("Please insert the product name to look for it.\n\n").lower()
        # loop through the list of Product instances to check every single one.
        for product in self.product_catalog:
        # if product is in product catalague, return it.
            if product.name.lower() == product_name:
                print(f"We found a product with name '{product_name}' in the catalog.\n\n")
                return product
        # if product is not in product catalog, print an error message
        print(f"We couldn't find the product with name {product_name} in the catalog.\n\n")
        return None

    def add_product(self):
        '''Adds a product (that already exists in the catalog) to the inventory, with the desired quantity.'''
        # given a product_name (user input),
        # check that the product exists (find_product)
        # IF the product does not exist, print error
        found_product = self.find_product()
        if not found_product:
            print("This product does not exists in the catalog. Please add a product to the catalog before adding it to the inventory.\n\n")


        while True:
            try:
                # OPTIONAL add also the case for decreasing the quantity
                additional_quantity = int(input("Please insert the product quantity to add it to the inventory.\n\n"))
            except ValueError:
                print("Please enter a positive integer number.\n\n")
                continue
        
            # Check if the product is already in inventory:
            # found_product is an object (a Product instance) -- product is a dictionary (in a list of dictionaries)
            for product in self.inventory:
                if found_product.name == product['name']:
                    # if it is, increase the inventory level
                    product['quantity'] += additional_quantity
                    # if it is, update the inventory value for that product
                    product['value'] = product['quantity'] * found_product.price
                    print(f"Added {additional_quantity} additional unit(s) of {product['name']}. \nTotal quantity is now {product['quantity']} for a total value of {product['value']}")
                
            # if it is not, create new product
            added_product =  {
            "name": found_product.name,        
            "price": found_product.price,
            "quantity": additional_quantity,
            "value": additional_quantity * found_product.price
        }
            self.inventory.append(added_product)   
                     
            # print success message
            print(f"{additional_quantity} unit(s) of product '{found_product.name}' successfully added to inventory.\n\n")
            break

    # # OPTIONAL update_product. ALSO this should go in Product class
    # def update_product(self, name, price = None):
    #     #ask for product name

    #     #check if product actually exists
    #         # if product does not exists, display error
    #         # if it exists, ask what user would like to update
    #             # if user says name, ask for new name
    #             # validate input
    #             # confirm y/n
    #             # actually update name
    #             # display_info()

    #             # if user says price, ask for new price
    #             # validate input
    #             # confirm y/n
    #             # actually update price
    #             # display_info()

    # # OPTIONAL update_product_quantity

    # delete_product - #REVIEW from catalog or inventory??? or both? 
    def delete_product_catalog(self):
        product_to_delete = input("Please enter the name of the product you would like to delete from the catalog.\n\n").lower()
        product_object_to_delete = self.find_product(product_to_delete)

        if product_object_to_delete:
            print(f"Product with name '{product_to_delete}' is about to be deleted. This action cannot be undone. Proceed?\n\n")
            reply = input("Please enter yes or no.\n\n").lower()
            if reply == "yes":
                self.product_catalog.remove(product_object_to_delete)
                print("Product successfully deleted.\n\n")
            else:
                print(f"Product '{product_to_delete}' has not been deleted.\n\n")
        else:
            print(f"Product {product_to_delete} not found in catalog.\n\n")

    def delete_product_inventory(self):
        # ask for product name
        product_to_delete = input("Please enter the name of the product you would like to delete from the inventory.\n\n")
        # try to find product in inventory]
        if product_to_delete not in self.inventory:
            print("We cannot find that product in the inventory. Please enter the name of a product that's currently in your inventory.\n\n")
        else:
            # if found product, ask user to confirm"
            print(f"Product with name '{product_to_delete}' is about to be deleted. This action cannot be undone. Proceed?\n")
            reply = input("Please enter yes or no.\n\n").lower()
            # if user confirms deletion, delete product dict from inventory
            if reply == "yes":
                del self.inventory[product_to_delete]
                print("Product successfully removed from inventory.\n\n")
        # if user does not confirm, exit.
            elif reply == 'no':
                print(f"Product {product_to_delete} has not been removed from inventory.\n\n")
    
    def print_product_catalog(self):
        # loop through product catalog to print all the items 
        number_of_products = len(self.product_catalog)
        print(f"There are currently {number_of_products} product(s) in the catalog.\n\n")
        for product in self.product_catalog:
            # OPTIONAL: format this better
            print(product)

    def print_inventory(self):
        # loop through self.inventory to print the inventory levels for each product.
        # format each items for readibility
        for product in self.inventory:
            print(f"Product: {product['name']} - Quantity: {product['quantity']} - Value: {product['value']} \n -----------\n")


    # def display_inventory_levels(self):
    #     # display current inventory levels (amount of every product)

    # def display_inventory_value(self):
    #     # display current inventory value (unit price * quantity per product)
