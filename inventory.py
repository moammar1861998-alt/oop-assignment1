from product import Product


class Inventory:
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.sku] = product

    def remove(self, sku):
        return self.products.pop(sku)

    def find(self, sku):
        return self.products.get(sku)

    def total_value(self):
        total = 0.0
        for sku, product in self.products.items():
            total += product.line_value
        return total

    @classmethod
    def from_lines(cls, lines):
        inventory = cls()
        for line in lines:
            inventory.add(Product.from_csv_line(line))
        return inventory