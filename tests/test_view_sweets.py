import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.view_sweets import ViewSweetsService

class TestViewSweets(unittest.TestCase):

    def setUp(self):
        self.test_db_name = "test_sweetshop.db"
        self.adder = AddSweetService(db_name=self.test_db_name)
        self.viewer = ViewSweetsService(db_name=self.test_db_name)

    def tearDown(self):
        self.adder.db.close_connection()
        self.viewer.db.close_connection()
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_get_all_sweets_returns_list_of_sweets(self):
        sweet1 = Sweet(id=2001, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=10)
        sweet2 = Sweet(id=2002, name="Gulab Jamun", category="Milk-Based", price=30.0, quantity=20)

        self.adder.add_sweet(sweet1)
        self.adder.add_sweet(sweet2)

        result = self.viewer.get_all_sweets()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(s, Sweet) for s in result))


    def test_get_all_sweets_empty_table(self):
        """
        Test that get_all_sweets returns an empty list when no sweets exist.
        """
        result = self.viewer.get_all_sweets()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_get_all_sweets_large_dataset(self):
        """
        Test performance of get_all_sweets when the table contains a large number of records.
        This checks that it still returns correct number of records efficiently.
        """
        # Insert 1,000 sweets
        for i in range(1, 1001):
            sweet = Sweet(
                id=9000 + i,
                name=f"Sweet {i}",
                category="Candy",
                price=10.0 + i,
                quantity=5 + i
            )
            self.adder.add_sweet(sweet)

        result = self.viewer.get_all_sweets()

        self.assertEqual(len(result), 1000)
        self.assertTrue(all(isinstance(s, Sweet) for s in result))

