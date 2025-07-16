import sqlite3
from database.db import Database

class RestockSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def restock_sweet(self, sweet_id_or_name, quantity: int) -> bool:
        """
        Increases the quantity of a sweet using ID (int) or name (str).
        """

        if not isinstance(quantity, int) or quantity <= 0:
            print(f"[restock_sweet ERROR] Invalid quantity: {quantity}")
            return False

        try:
            if isinstance(sweet_id_or_name, int):
                cursor = self.conn.execute("SELECT id, quantity FROM sweets WHERE id = ?", (sweet_id_or_name,))
            elif isinstance(sweet_id_or_name, str) and sweet_id_or_name.strip():
                cursor = self.conn.execute("SELECT id, quantity FROM sweets WHERE name = ?", (sweet_id_or_name.strip(),))
            else:
                print(f"[restock_sweet ERROR] Invalid sweet identifier: {sweet_id_or_name}")
                return False

            row = cursor.fetchone()

            if not row:
                print(f"[restock_sweet ERROR] Sweet not found: {sweet_id_or_name}")
                return False

            sweet_id, current_quantity = row
            new_quantity = current_quantity + quantity

            self.conn.execute("UPDATE sweets SET quantity = ? WHERE id = ?", (new_quantity, sweet_id))
            self.conn.commit()
            return True

        except Exception as e:
            print(f"[restock_sweet ERROR] {e}")
            return False
