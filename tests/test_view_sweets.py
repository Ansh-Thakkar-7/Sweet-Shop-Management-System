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

    def test_get_all_sweets_with_special_characters(self):
        sweet = Sweet(id=2010, name="Kaju ❤️", category="Nut-Based", price=99.99, quantity=5)
        self.adder.add_sweet(sweet)
        result = self.viewer.get_all_sweets()
        self.assertEqual(result[0].name, "Kaju ❤️")
