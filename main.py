from inventory import Inventory
from product import Product

SAMPLE = [
    "Milk,MLK001,1.25,12",
    "Bread,BRD002,0.90,3",
    "Eggs,EGG003,2.40,30",
    "Coffee,COF004,7.50,2",
]


def main():
    inventory = Inventory.from_lines(SAMPLE)

    print("=== MiniMart Inventory Report ===")
    for sku, product in inventory.products.items():
        print(f"{product.sku}  {product.name}  price: {product.price:.2f}  qty: {product.quantity}  line value: {product.line_value:.2f}")

    print(f"\nTotal inventory value: {inventory.total_value():.2f}")
    print(f"Total products created: {Product.count()}")

    low_stock = [
        product for sku, product in inventory.products.items()
        if product.is_low_stock
    ]
    print("\nLow-stock items:")
    for item in low_stock:
        print(f"  - {item.name} ({item.sku}): {item.quantity}")


if __name__ == "__main__":
    main()