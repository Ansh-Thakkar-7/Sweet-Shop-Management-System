import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.sort_sweets import SortSweetsService

class TestSortSweets(unittest.TestCase):

    def setUp(self):
        self.db_name = "test_sweetshop.db"
        self.adder = AddSweetService(self.db_name)
        self.sorter = SortSweetsService(self.db_name)

        sweets = [
            Sweet(id=9001, name="Gulab Jamun", category="Milk-Based", price=20.0, quantity=15),
            Sweet(id=9002, name="Barfi", category="Milk-Based", price=25.0, quantity=10),
            Sweet(id=9003, name="Kaju Katli", category="Nut-Based", price=30.0, quantity=20),
        ]

        for sweet in sweets:
            self.adder.add_sweet(sweet)

    def tearDown(self):
        self.sorter.db.close_connection()
        self.adder.db.close_connection()
        time.sleep(0.1)
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_sort_by_name_ascending(self):
        """
        Test that sweets are sorted by name in ascending order.
        """
        result = self.sorter.sort_sweets(by="name", order="asc")
        names = [sweet.name for sweet in result]
        self.assertEqual(names, ["Barfi", "Gulab Jamun", "Kaju Katli"])


    def test_sort_by_name_descending(self):
        """
        Test that sweets are sorted by name in descending order (Z-A).
        """
        result = self.sorter.sort_sweets(by="name", order="desc")
        names = [sweet.name for sweet in result]
        self.assertEqual(names, ["Kaju Katli", "Gulab Jamun", "Barfi"])

    def test_sort_by_price_ascending(self):
        """
        Test that sweets are sorted by price in ascending order.
        """
        result = self.sorter.sort_sweets(by="price", order="asc")
        prices = [sweet.price for sweet in result]
        self.assertEqual(prices, [20.0, 25.0, 30.0])

    def test_sort_by_price_descending(self):
        """
        Test that sweets are sorted by price in descending order (high to low).
        """
        result = self.sorter.sort_sweets(by="price", order="desc")
        prices = [sweet.price for sweet in result]
        self.assertEqual(prices, [30.0, 25.0, 20.0])

    def test_sort_by_quantity_ascending(self):
        """
        Test that sweets are sorted by quantity in ascending order (low to high).
        """
        result = self.sorter.sort_sweets(by="quantity", order="asc")
        quantities = [sweet.quantity for sweet in result]
        self.assertEqual(quantities, [10, 15, 20])

    def test_sort_by_quantity_descending(self):
        """
        Test that sweets are sorted by quantity in descending order (high to low).
        """
        result = self.sorter.sort_sweets(by="quantity", order="desc")
        quantities = [sweet.quantity for sweet in result]
        self.assertEqual(quantities, [20, 15, 10])


    def test_sort_by_category_ascending(self):
        """
        Test that sweets are sorted by category in ascending order (A–Z).
        """
        result = self.sorter.sort_sweets(by="category", order="asc")
        categories = [sweet.category for sweet in result]
        self.assertEqual(categories, ["Milk-Based", "Milk-Based", "Nut-Based"])