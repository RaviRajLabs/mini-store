from app.models import Order
from app.payment import PaymentMethod

class OrderService:
    
    def calculate_total(self, order):
        return order.total()
    
    def confirm_order(self, order):
        order.confirm()
        return order
    
    def pay_order(self, order, payment_method: PaymentMethod):

        if order.status != "CONFIRMED":
            print("Order must be confirmed before payment.")
            return False
        
        amount = order.total()
        payment_success = payment_method.process(amount)

        if payment_success:
            order.payment_status = "PAID"
        return payment_success