# MiniMart Inventory System (`oop-assignment1`)

University of Nizwa — Object-Oriented Programming with Python  
**Assignment 1 — Object-Oriented Mini-Project (Lectures 0-5)**

## Instructions to Execute the Program

1. Execute the demo script with Python 3.10 or higher:
   ```bash
   python main.py
   ```

2. Execute the `pytest` tests (Part 5 Bonus):
   ```bash
   python -m pytest -v
   ```

## Design Choices

- **Instance Attributes in `__init__` (Lectures 2 & 3)**: Both classes (`Product` and `Inventory`) initialize their instance attributes within `__init__` (`self.products = {}` in `Inventory`) so that separate instances never share mutable state.
- **Encapsulation and Validation (Lectures 4 & 5)**: The attributes `price` and `quantity` are implemented with `@property` getters and setters. Assigning `self.price = price` and `self.quantity = quantity` inside `__init__` ensures all initial values are validated, raising `TypeError` for wrong types and `ValueError` for negative numbers.
- **Computed Read-Only Properties (Lecture 4)**: The `line_value` (`price * quantity`) and `is_low_stock` (`quantity < 5`) properties are read-only `@property` methods with no setter so their values are always computed on access and never become stale.
- **Class Methods and Factories (Lectures 3 & 5)**: `Product.from_csv_line(cls, line)` and `Inventory.from_lines(cls, lines)` use `@classmethod` and `cls(...)` as alternative constructors. `Product.is_valid_sku(sku)` uses `@staticmethod` to check the SKU format because it does not need `self` or `cls`. `Product._count` tracks how many products have been created and is exposed via `@classmethod Product.count(cls)`.
