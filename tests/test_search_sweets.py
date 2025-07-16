import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.search_sweets import SearchSweetService

class TestSearchSweets(unittest.TestCase):

    def setUp(self):
        self.test_db_name = "test_sweetshop.db"
        self.adder = AddSweetService(db_name=self.test_db_name)
        self.searcher = SearchSweetService(db_name=self.test_db_name)

        # Seed sweets
        self.adder.add_sweet(Sweet(id=5001, name="Barfi", category="Milk-Based", price=20.0, quantity=10))
        self.adder.add_sweet(Sweet(id=5002, name="Gulab Jamun", category="Milk-Based", price=30.0, quantity=15))
        self.adder.add_sweet(Sweet(id=5003, name="Candy Pop", category="Candy", price=5.0, quantity=50))
        self.adder.add_sweet(Sweet(id=5004, name="Dark Chocolate", category="Chocolate", price=50.0, quantity=25))

    def tearDown(self):
        self.adder.db.close_connection()
        self.searcher.db.close_connection()
        time.sleep(0.1)
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_search_by_name(self):
        """
        Test searching for sweets by partial name.
        """
        result = self.searcher.search_sweets(name="barfi")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Barfi")
