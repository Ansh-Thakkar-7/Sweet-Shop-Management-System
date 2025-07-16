import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.restock_sweet import RestockSweetService

class TestRestockSweet(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_sweetshop.db"
        self.adder = AddSweetService(self.db_name)
        self.restocker = RestockSweetService(self.db_name)

        sweet = Sweet(id=8001, name="Ladoo", category="Nut-Based", price=25.0, quantity=5)
        self.adder.add_sweet(sweet)

    def tearDown(self):
        self.adder.db.close_connection()
        self.restocker.db.close_connection()
        time.sleep(0.1)
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_restock_increases_quantity(self):
        """
        Test that restocking a sweet correctly increases its quantity.
        """
        result = self.restocker.restock_sweet(8001, 10)
        self.assertTrue(result)

        cursor = self.restocker.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (8001,))
        quantity = cursor.fetchone()[0]
        self.assertEqual(quantity, 15)  # 5 + 10

    def test_restock_fails_with_invalid_quantity(self):
        """
        Test that restocking fails if quantity is not a positive integer.
        """
        self.assertFalse(self.restocker.restock_sweet(8001, None))
        self.assertFalse(self.restocker.restock_sweet(8001, "ten"))
        self.assertFalse(self.restocker.restock_sweet(8001, 0))
        self.assertFalse(self.restocker.restock_sweet(8001, -5))
        self.assertFalse(self.restocker.restock_sweet(8001, 2.5))

    def test_restock_fails_for_nonexistent_sweet(self):
    """
    Test that restocking fails if the sweet ID does not exist in the database.
    """
    result = self.restocker.restock_sweet(9999, 10)  # ID 9999 does not exist
    self.assertFalse(result)