from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class WalletPayment(PaymentMethod):
    def __init__(self,balance):
        self.balance = balance

    def process(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True

        return False
    
class CardPayment(PaymentMethod):

    def process(self, amount):
        print(f"Processing card payment of {amount}")
        return True

class UPIPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing UPI payment of {amount}")
        return True