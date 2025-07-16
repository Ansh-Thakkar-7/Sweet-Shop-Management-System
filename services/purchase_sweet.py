import sqlite3
from database.db import Database


class PurchaseSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def purchase_sweet(self, sweet_id: int, quantity: int) -> bool:
        """
        Purchases a sweet by reducing its stock.
        Returns True if purchase is successful.
        """

        try:
            cursor = self.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (sweet_id,))
            row = cursor.fetchone()

            if not row:
                print(f"[purchase_sweet ERROR] Sweet ID {sweet_id} not found.")
                return False

            current_quantity = row[0]
            if current_quantity < quantity:
                print(f"[purchase_sweet ERROR] Not enough stock. Available: {current_quantity}, Requested: {quantity}")
                return False

            new_quantity = current_quantity - quantity

            self.conn.execute("UPDATE sweets SET quantity = ? WHERE id = ?", (new_quantity, sweet_id))
            self.conn.commit()

            return True

        except Exception as e:
            print(f"[purchase_sweet ERROR] {e}")
            return False
