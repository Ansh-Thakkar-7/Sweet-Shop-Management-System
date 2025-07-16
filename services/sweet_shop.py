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
        if not sweet.name.strip():
            print(f"[add_sweet ERROR] Name cannot be empty")
            return False

        if not sweet.category.strip():
            print(f"[add_sweet ERROR] Category cannot be empty")
            return False
        
        if not isinstance(sweet.price, (int, float)):
            print(f"[add_sweet ERROR] Price must be a number: {sweet.price}")
            return False

        if sweet.price < 0:
            print(f"[add_sweet ERROR] Price cannot be negative: {sweet.price}")
            return False
        
        if not isinstance(sweet.quantity, int):
            print(f"[add_sweet ERROR] Quantity must be an integer: {sweet.quantity}")
            return False

        if sweet.quantity <= 0:
            print(f"[add_sweet ERROR] Quantity must be greater than 0: {sweet.quantity}")
            return False
        
            

        
        
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