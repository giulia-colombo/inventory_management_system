class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
# display_info
    def __str__(self):
        return f'Product (name={self.name}, price={self.price})'

