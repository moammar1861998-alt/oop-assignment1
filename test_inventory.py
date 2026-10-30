import pytest
from product import Product
from inventory import Inventory


def test_valid_product_and_repr():
    p = Product("Milk", "MLK001", 1.25, 12)
    assert p.name == "Milk"
    assert p.sku == "MLK001"
    assert p.price == 1.25
    assert p.quantity == 12
    assert repr(p) == "Product('Milk', 'MLK001', 1.25, 12)"


def test_computed_properties():
    p1 = Product("Milk", "MLK001", 1.25, 12)
    assert p1.line_value == 15.0
    assert p1.is_low_stock is False

    p2 = Product("Bread", "BRD002", 0.90, 3)
    assert round(p2.line_value, 2) == 2.70
    assert p2.is_low_stock is True


def test_negative_price_raises_value_error():
    with pytest.raises(ValueError):
        Product("Milk", "MLK001", -1.0, 12)


def test_non_number_price_raises_type_error():
    with pytest.raises(TypeError):
        Product("Milk", "MLK001", "1.25", 12)


def test_invalid_quantity_raises_error():
    with pytest.raises(TypeError):
        Product("Milk", "MLK001", 1.25, 2.5)
    with pytest.raises(ValueError):
        Product("Milk", "MLK001", 1.25, -3)


def test_is_valid_sku():
    assert Product.is_valid_sku("MLK001") is True
    assert Product.is_valid_sku("BADSKU") is False
    assert Product.is_valid_sku("123456") is False


def test_factories_and_inventory():
    lines = [
        "Milk,MLK001,1.25,12",
        "Bread,BRD002,0.90,3",
        "Eggs,EGG003,2.40,30",
        "Coffee,COF004,7.50,2",
    ]
    inv = Inventory.from_lines(lines)
    assert inv.find("MLK001").name == "Milk"
    assert round(inv.total_value(), 2) == 104.70
    inv.remove("COF004")
    assert inv.find("COF004") is None