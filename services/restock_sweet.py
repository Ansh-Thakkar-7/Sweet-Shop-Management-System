import sqlite3
from database.db import Database

class RestockSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def restock_sweet(self, sweet_id: int, quantity: int) -> bool:
        """
        Increases the quantity of a sweet in the database.
        """

        if not isinstance(quantity, int) or quantity <= 0:
            print(f"[restock_sweet ERROR] Invalid quantity: {quantity}")
            return False

        # Step 1: Get current quantity
        cursor = self.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (sweet_id,))
        row = cursor.fetchone()

        if not row:
            return False  # sweet not found

        current_quantity = row[0]
        new_quantity = current_quantity + quantity

        # Step 2: Update quantity
        self.conn.execute("UPDATE sweets SET quantity = ? WHERE id = ?", (new_quantity, sweet_id))
        self.conn.commit()

        return True
