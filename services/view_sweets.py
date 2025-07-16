import sqlite3
from database.db import Database
from models.sweet import Sweet


class ViewSweetsService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def get_all_sweets(self):
        """
        Fetches all sweets from the DB and returns them as a list of Sweet objects.
        """
        query = "SELECT id, name, category, price, quantity FROM sweets"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            # Convert each row into a Sweet object
            sweets = [Sweet(*row) for row in rows]
            return sweets

        except Exception as e:
            print(f"[get_all_sweets ERROR] {e}")
            return []
