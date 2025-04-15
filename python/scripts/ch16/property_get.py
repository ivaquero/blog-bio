class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f"_{prefix}#{index}"
        cls.__counter += 1

    def __get__(self, instance):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must be > 0")


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


coconuts = LineItem("Brazilian coconut", 20, 17.95)
print(coconuts.weight, coconuts.price)  # (20, 17.95)
print(getattr(coconuts, "_Quantity#0"))  # 20
print(getattr(coconuts, "_Quantity#1"))  # 17.95
