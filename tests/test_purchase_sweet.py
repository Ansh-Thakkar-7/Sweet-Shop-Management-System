import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.purchase_sweet import PurchaseSweetService
from exceptions.exceptions import StockError


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


    def test_purchase_raises_exception_if_not_enough_stock(self):
        """
        Test that purchase fails if requested quantity exceeds available stock.
        Original quantity = 10, trying to purchase 15.
        """
        with self.assertRaises(StockError):
            self.purchaser.purchase_sweet(7001, 15) 


        # Confirm quantity in DB is unchanged
        sweets = self.purchaser.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (7001,))
        quantity = sweets.fetchone()[0]
        self.assertEqual(quantity, 10)


    def test_purchase_fails_with_invalid_sweet_id(self):
        """
        Test that purchase fails if sweet_id is not an integer or doesn't exist in DB.
        """
        # Invalid ID types
        self.assertFalse(self.purchaser.purchase_sweet(None, 2))
        self.assertFalse(self.purchaser.purchase_sweet("abc", 2))
        self.assertFalse(self.purchaser.purchase_sweet(12.5, 2))
        self.assertFalse(self.purchaser.purchase_sweet(-10, 2))

        # Valid type but sweet doesn't exist
        self.assertFalse(self.purchaser.purchase_sweet(9999, 2))  # Non-existent ID

    def test_purchase_fails_with_invalid_quantity(self):
        """
        Test that purchase fails when quantity is not a positive integer.
        """
        self.assertFalse(self.purchaser.purchase_sweet(7001, None))
        self.assertFalse(self.purchaser.purchase_sweet(7001, "two"))
        self.assertFalse(self.purchaser.purchase_sweet(7001, 2.5))
        self.assertFalse(self.purchaser.purchase_sweet(7001, -1))
        self.assertFalse(self.purchaser.purchase_sweet(7001, 0))  # 0 is invalid

