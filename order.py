
class Order:
    def __ini__(self, number, date, products):
        self.number = number
        self.date = date
        self.product = product
    def cancel(self):
        pass

class Payment:
    
    def __init__(self, receipt, amount, method, status):
        self.receipt = receipt
        self.amount = amount
        self.method = method
        self.status = status
    def refund(self):
        pass
    def process_payment(self):
        pass

class Delivery:
    def __init__(self, delivery_date, code, address, status):
        self.delivery_date = delivery_date
        self.code = code
        self.address = address
        self.status = status
    def update_status(self):
        pass

