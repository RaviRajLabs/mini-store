class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self,name, email):
        self.name = name
        self.email = email
    def introduce(self):
        return f"My name is {self.name}"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.status = "PENDING"
        self.payment_status = "PENDING"
        
    def add_product(self, product):
        self.products.append(product)

    def total(self):
        total= 0

        for product in self.products:
            total += product.price
        return total
    
    def confirm(self):
        if self.status=="CONFIRMED":
            print("Order already confirmed")
            return
        self.status ="CONFIRMED"
    