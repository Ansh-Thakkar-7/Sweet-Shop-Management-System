import sqlite3
from database.db import Database
from models.sweet import Sweet


class SweetShop:
    """
    Service class to handle operations related to the sweet inventory.
    """
    def __init__(self,db_name='sweetshop.db'):
        """
        Initializes the database connection.
        """
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def add_sweet(self, sweet: Sweet):
        """
        Adds a new sweet to the database.
        Returns True if insertion succeeds.
        """

        query = """
        INSERT INTO sweets (id, name, category, price, quantity)
        VALUES (?, ?, ?, ?, ?)
        """
        values = (sweet.id, sweet.name, sweet.category, sweet.price, sweet.quantity)

        try:
            with self.conn: 
                self.conn.execute(query, values)
            return True
        except sqlite3.IntegrityError:
            print(f"[add_sweet ERROR] Sweet with ID {sweet.id} already exists.")
            return False
        except Exception as e:
            print(f"[add_sweet ERROR] {e}")
            return False