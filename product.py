class Product:
    _count = 0

    def __init__(self, name, sku, price, quantity):
        if not Product.is_valid_sku(sku):
            raise ValueError("sku must be three letters followed by three digits")
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
        Product._count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = float(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity must be >= 0")
        self._quantity = value

    @property
    def line_value(self):
        return self._price * self._quantity

    @property
    def is_low_stock(self):
        return self._quantity < 5

    @classmethod
    def from_csv_line(cls, line):
        name, sku, price_text, qty_text = line.strip().split(",")
        return cls(name, sku, float(price_text), int(qty_text))

    @staticmethod
    def is_valid_sku(sku):
        if not isinstance(sku, str) or len(sku) != 6:
            return False
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        for ch in sku[:3]:
            if ch.upper() not in letters:
                return False
        for ch in sku[3:]:
            if ch not in digits:
                return False
        return True

    @classmethod
    def count(cls):
        return cls._count

    def __repr__(self):
        return f"Product('{self.name}', '{self.sku}', {self.price}, {self.quantity})"