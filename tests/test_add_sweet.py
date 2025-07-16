import unittest
from services.add_sweet import AddSweetService
from models.sweet import Sweet
import os
import time

class TestAddSweet(unittest.TestCase):
    """
    Test suite for the SweetShop service class.
    All test cases follow TDD principles and validate core business logic.
    """

    def setUp(self):
        self.test_db_name = 'test_sweetshop.db'
        self.shop = AddSweetService(db_name=self.test_db_name)

    def tearDown(self):
        if hasattr(self.shop, 'db'):
            self.shop.db.close_connection()

        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_add_sweet(self):
        """
        Test that a new sweet can be successfully added to the shop.
        """
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=20)
        result = self.shop.add_sweet(sweet)  
        self.assertTrue(result)

    def test_add_duplicate_sweet_id(self):
        """
        Test that adding a sweet with a duplicate ID is not allowed.
        """
        sweet1 = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=15.0, quantity=10)
        sweet2 = Sweet(id=1002, name="Duplicate Sweet", category="Milk-Based", price=20.0, quantity=5)

        self.shop.add_sweet(sweet1)         
        result = self.shop.add_sweet(sweet2)
        self.assertFalse(result)

    def test_add_sweet_with_negative_price(self):
        """
        Test that adding a sweet with negative price is not allowed.
        Expected: add_sweet() should return False.
        """
        sweet = Sweet(id=3001, name="Bad Sweet", category="Candy", price=-10.0, quantity=5)
        result = self.shop.add_sweet(sweet)
        self.assertFalse(result)


    def test_add_sweet_with_missing_or_invalid_fields(self):
        """
        Test that adding a sweet with missing or invalid fields is not allowed.
        Includes:
        - Empty name
        - Empty category
        - Zero or negative quantity
        """
        invalid_sweets = [
            Sweet(id=3003, name="   ", category="Candy", price=10.0, quantity=5),     # Empty name
            Sweet(id=3004, name="Valid", category=" ", price=10.0, quantity=5),       # Empty category
            Sweet(id=3005, name="Valid", category="Candy", price=10.0, quantity=0),   # Zero quantity
            Sweet(id=3006, name="Valid", category="Candy", price=10.0, quantity=-3),  # Negative quantity
        ]

        for sweet in invalid_sweets:
            result = self.shop.add_sweet(sweet)
            self.assertFalse(result)

    def test_add_sweet_with_non_numeric_price_or_quantity(self):
        """
        Test that adding a sweet with non-numeric price or quantity is rejected.
        """
        invalid_sweets = [
            Sweet(id=4001, name="Toffee", category="Candy", price="free", quantity=10),    # Invalid price (string)
            Sweet(id=4002, name="Barfi", category="Milk-Based", price=20.0, quantity="ten"), # Invalid quantity (string)
        ]

        for sweet in invalid_sweets:
            result = self.shop.add_sweet(sweet)
            self.assertFalse(result)



    def test_add_sweet_with_invalid_category(self):
        """
        Test that a sweet with a category not in the allowed list is rejected.
        """
        sweet = Sweet(id=5001, name="Weird Sweet", category="Ice Cream", price=15.0, quantity=5)
        result = self.shop.add_sweet(sweet)
        self.assertFalse(result)


    def test_add_valid_sweet_passes_all_validations(self):
        """
        Test that a sweet with valid name, category, price, and quantity is successfully added.
        """
        sweet = Sweet(
            id=6001,
            name="Chocolate Bar",
            category="Chocolate",  
            price=25.0,
            quantity=10
        )
        result = self.shop.add_sweet(sweet)
        self.assertTrue(result)


def test_add_sweet_with_duplicate_name_and_category(self):
    """
    Test that adding a sweet with the same name and category (even with different ID) is not allowed.
    """
    sweet1 = Sweet(id=4101, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=10)
    sweet2 = Sweet(id=4102, name="Kaju Katli", category="Nut-Based", price=60.0, quantity=5)

    self.service.add_sweet(sweet1)
    result = self.service.add_sweet(sweet2)

    self.assertFalse(result)
