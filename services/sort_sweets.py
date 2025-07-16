import sqlite3
from database.db import Database
from models.sweet import Sweet

class SortSweetsService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def sort_sweets(self, by: str, order: str = "asc"):
        """
        Sort sweets by the specified field and order.
        Supported fields: name
        Supported order: asc, desc
        """

        if by != "name":
            print(f"[sort_sweets ERROR] Unsupported sort field: {by}")
            return []

        if order not in ["asc", "desc"]:
            print(f"[sort_sweets ERROR] Invalid order: {order}")
            return []

        query = f"SELECT id, name, category, price, quantity FROM sweets ORDER BY name {order.upper()}"

        try:
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
            return [Sweet(*row) for row in rows]
        except Exception as e:
            print(f"[sort_sweets ERROR] {e}")
            return []

