import unittest
from services.sweet_shop import SweetShop
from models.sweet import Sweet
import os
import time

class TestSweetShop(unittest.TestCase):
    """
    Test suite for the SweetShop service class.
    All test cases follow TDD principles and validate core business logic.
    """

    def setUp(self):
        self.test_db_name = 'test_sweetshop.db'
        self.shop = SweetShop(db_name=self.test_db_name)

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
