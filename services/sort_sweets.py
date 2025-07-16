import sqlite3
from database.db import Database
from models.sweet import Sweet

class SortSweetsService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def sort_sweets(self, by: str, order: str = "asc"):
        """
        Sort sweets by specified field and order.
        Supported fields: name, price
        Supported orders: asc, desc
        """

        valid_fields = ["name", "price", "quantity", "category"]
        valid_orders = ["asc", "desc"]

        if not isinstance(by, str) or by not in valid_fields:
            print(f"[sort_sweets ERROR] Invalid field: {by}")
            return []

        if not isinstance(order, str) or order not in valid_orders:
            print(f"[sort_sweets ERROR] Invalid order: {order}")
            return []

        query = f"SELECT id, name, category, price, quantity FROM sweets ORDER BY {by} {order.upper()}"

        try:
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
            return [Sweet(*row) for row in rows]
        except Exception as e:
            print(f"[sort_sweets ERROR] {e}")
            return []


