import sqlite3
from database.db import Database
from models.sweet import Sweet

class SortSweetsService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def sort_sweets(self, by: str, order: str = "asc"):
        """
        Sort sweets by the specified field (e.g., name).
        """
        # Only minimal logic for this test — sorting by name asc
        if by != "name":
            print(f"[sort_sweets ERROR] Unsupported sort field: {by}")
            return []

        query = "SELECT id, name, category, price, quantity FROM sweets ORDER BY name ASC"

        try:
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
            sweets = [Sweet(*row) for row in rows]
            return sweets
        except Exception as e:
            print(f"[sort_sweets ERROR] {e}")
            return []
