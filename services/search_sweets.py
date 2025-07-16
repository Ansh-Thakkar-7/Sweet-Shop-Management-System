import sqlite3
from database.db import Database
from models.sweet import Sweet


class SearchSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        """
        Searches sweets by optional filters: name (LIKE), category, and price range.
        """

        # Input validation
        if name is not None and not isinstance(name, str):
            print(f"[search_sweets ERROR] Invalid name: {name}")
            return []
        if category is not None and not isinstance(category, str):
            print(f"[search_sweets ERROR] Invalid category: {category}")
            return []
        if min_price is not None and not isinstance(min_price, (int, float)):
            print(f"[search_sweets ERROR] Invalid min_price: {min_price}")
            return []
        if max_price is not None and not isinstance(max_price, (int, float)):
            print(f"[search_sweets ERROR] Invalid max_price: {max_price}")
            return []

        query = "SELECT id, name, category, price, quantity FROM sweets WHERE 1=1"
        params = []

        if name:
            query += " AND LOWER(name) LIKE ?"
            params.append(f"%{name.lower()}%")

        if category:
            query += " AND category = ?"
            params.append(category)

        if min_price is not None:
            query += " AND price >= ?"
            params.append(min_price)

        if max_price is not None:
            query += " AND price <= ?"
            params.append(max_price)

        try:
            cursor = self.conn.execute(query, tuple(params))
            rows = cursor.fetchall()
            return [Sweet(*row) for row in rows]
        except Exception as e:
            print(f"[search_sweets ERROR] {e}")
            return []



        