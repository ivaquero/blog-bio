class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("value must be > 0")


class LineItem:
    weight = Quantity("weight")
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


nutmeg = LineItem("Moluccan nutmeg", 8, 13.95)
print(nutmeg.weight, nutmeg.price)  # (8, 13.95)
print(sorted(vars(nutmeg).items()))
# [('description', 'Moluccan nutmeg'), ('price', 13.95), ('weight', 8)]
