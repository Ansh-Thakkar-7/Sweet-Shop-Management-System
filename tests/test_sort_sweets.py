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
