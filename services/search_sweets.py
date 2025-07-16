import sqlite3
from database.db import Database
from models.sweet import Sweet


class SearchSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        """
        Supports search by name (LIKE) and category (exact match).
        """

        # Validate category
        if category is not None and not isinstance(category, str):
            print(f"[search_sweets ERROR] Invalid category: {category}")
            return []

        query = "SELECT id, name, category, price, quantity FROM sweets WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")

        if category:
            query += " AND category = ?"
            params.append(category)

        try:
            cursor = self.conn.execute(query, tuple(params))
            rows = cursor.fetchall()
            return [Sweet(*row) for row in rows]
        except Exception as e:
            print(f"[search_sweets ERROR] {e}")
            return []


