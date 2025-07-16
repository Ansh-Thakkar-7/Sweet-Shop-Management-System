import sqlite3
from database.db import Database
from models.sweet import Sweet


class SearchSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
    """
    Minimal logic: Only supports search by name (case-insensitive).
    """

    if not name:
        return []  # ⬅️ For now, skip all other search types

    query = """
    SELECT id, name, category, price, quantity
    FROM sweets
    WHERE LOWER(name) LIKE ?
    """
    params = [f"%{name.lower()}%"]

    try:
        cursor = self.conn.execute(query, params)
        rows = cursor.fetchall()
        return [Sweet(*row) for row in rows]
    except Exception as e:
        print(f"[search_sweets ERROR] {e}")
        return []

