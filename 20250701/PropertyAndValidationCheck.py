class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError(f"Weight cannot be negative: {value}")
        self._weight = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

a_book = Item('book', 10, 9.5)
print(a_book.subtotal())
try:
    a_book.weight = -10
except ValueError as e:
    print(e)
print(a_book.subtotal())
