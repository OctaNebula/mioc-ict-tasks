class PaymentMethods:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Card(PaymentMethods):
    def __init__(self, name, value, ID, expiration_date):
        super().__init__(name, value)
        self.ID = int(ID)
        self.expiration_date = str(expiration_date)

class Paypal(PaymentMethods):
    def __init__(self, name, value, email):
        super().__init__(name, value)
        self.email = email

example = Paypal("Paypal", 100, "johndoe@gmail.com")
print(example.value)