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

    def test_delete_sweet_with_invalid_id_types(self):
        """
        Test that delete_sweet handles invalid ID types gracefully and returns False.
        """
        invalid_ids = [None, "abc", 12.5, -10]

        for invalid_id in invalid_ids:
            with self.subTest(id=invalid_id):
                result = self.deleter.delete_sweet(invalid_id)
                self.assertFalse(result)

    def test_delete_sweet_twice_should_return_false_second_time(self):
        """
        Test that deleting the same sweet twice returns True once and then False.
        """
        sweet = Sweet(id=3010, name="Jalebi", category="Nut-Based", price=15.0, quantity=10)
        self.adder.add_sweet(sweet)

        result1 = self.deleter.delete_sweet(3010)
        result2 = self.deleter.delete_sweet(3010)

        self.assertTrue(result1)   # First delete should succeed
        self.assertFalse(result2)  # Second delete should fail (already gone)

    def test_delete_sweet_by_name_successfully(self):
        """
        Test that a sweet can be deleted by name.
        """
        sweet = Sweet(id=3020, name="Barfi", category="Milk-Based", price=20.0, quantity=10)
        self.adder.add_sweet(sweet)

        result = self.deleter.delete_sweet_by_name("Barfi")
        self.assertTrue(result)


