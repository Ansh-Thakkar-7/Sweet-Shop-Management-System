import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.purchase_sweet import PurchaseSweetService


class TestPurchaseSweet(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_sweetshop.db"
        self.adder = AddSweetService(self.db_name)
        self.purchaser = PurchaseSweetService(self.db_name)

        sweet = Sweet(id=7001, name="Kalakand", category="Milk-Based", price=30.0, quantity=10)
        self.adder.add_sweet(sweet)

    def tearDown(self):
        self.adder.db.close_connection()
        self.purchaser.db.close_connection()
        time.sleep(0.1)
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_purchase_reduces_quantity(self):
        """
        Test that purchasing a sweet reduces the quantity in stock.
        """
        result = self.purchaser.purchase_sweet(7001, 3)  # Purchase 3 out of 10
        self.assertTrue(result)

        # Check updated quantity
        sweets = self.purchaser.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (7001,))
        quantity = sweets.fetchone()[0]
        self.assertEqual(quantity, 7)  


    def test_purchase_fails_if_not_enough_stock(self):
        """
        Test that purchase fails if requested quantity exceeds available stock.
        Original quantity = 10, trying to purchase 15.
        """
        result = self.purchaser.purchase_sweet(7001, 15)  # Too much
        self.assertFalse(result)

        # Confirm quantity in DB is unchanged
        sweets = self.purchaser.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (7001,))
        quantity = sweets.fetchone()[0]
        self.assertEqual(quantity, 10)

