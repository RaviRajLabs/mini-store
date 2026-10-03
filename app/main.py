
from app.models import Product, Customer, Order
from app.services import OrderService
from app.payment import WalletPayment,CardPayment, UPIPayment

def run():
    product = Product("Laptop",50000)
    customer = Customer("Ravi","ravi@rsquarenova.com")

    laptop = Product("Laptop", 50000)
    mouse = Product("Mouse", 1000)


    order = Order(customer)

    order.add_product(laptop)
    order.add_product(mouse)

    order_service = OrderService()

    order_service.confirm_order(order)

    wallet = WalletPayment(100000)
    card = CardPayment()
    upi = UPIPayment()

    payment_result = order_service.pay_order(
        order,
        upi
    )

    print("Payment successful:", payment_result)
    print("Order status:", order.status)
    print("Payment status:", order.payment_status)
   

if __name__ == "__main__":
    run()
    

