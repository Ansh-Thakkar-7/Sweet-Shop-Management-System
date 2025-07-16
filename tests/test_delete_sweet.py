import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.delete_sweet import DeleteSweetService

class TestDeleteSweet(unittest.TestCase):
    def setUp(self):
        self.test_db_name = "test_sweetshop.db"
        self.adder = AddSweetService(db_name=self.test_db_name)
        self.deleter = DeleteSweetService(db_name=self.test_db_name)

    def tearDown(self):
        self.adder.db.close_connection()
        self.deleter.db.close_connection()
        time.sleep(0.1)
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_delete_existing_sweet(self):
        """
        Test that a sweet with a given ID is deleted successfully.
        """
        sweet = Sweet(id=3001, name="Imarti", category="Nut-Based", price=25.0, quantity=5)
        self.adder.add_sweet(sweet)

        result = self.deleter.delete_sweet(3001)
        self.assertTrue(result)


    def test_delete_non_existing_sweet(self):
        """
        Test that trying to delete a non-existent sweet ID returns False.
        """
        result = self.deleter.delete_sweet(9999)  # ID that doesn't exist
        self.assertFalse(result)

