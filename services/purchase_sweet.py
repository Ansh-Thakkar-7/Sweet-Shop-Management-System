from exceptions.exceptions import StockError
import sqlite3
from database.db import Database

class PurchaseSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def purchase_sweet(self, sweet_id_or_name, quantity: int) -> bool:
        """
        Purchases a sweet by ID (int) or Name (str), reducing its stock.
        Raises StockError if insufficient stock.
        """

        # Validate quantity
        if not isinstance(quantity, int) or quantity <= 0:
            print(f"[purchase_sweet ERROR] Invalid quantity: {quantity}")
            return False

        try:
            # Get sweet by ID
            if isinstance(sweet_id_or_name, int):
                if sweet_id_or_name <= 0:
                    print(f"[restock_sweet ERROR] Invalid sweet ID: {sweet_id_or_name}")
                    return False
                cursor = self.conn.execute("SELECT id, quantity FROM sweets WHERE id = ?", (sweet_id_or_name,))

            elif isinstance(sweet_id_or_name, str):
                name = sweet_id_or_name.strip()
                if not name or name.isnumeric():
                    print(f"[restock_sweet ERROR] Invalid sweet name: {sweet_id_or_name}")
                    return False
                cursor = self.conn.execute("SELECT id, quantity FROM sweets WHERE name = ?", (name,))

            else:
                print(f"[restock_sweet ERROR] Unsupported identifier type: {type(sweet_id_or_name)}")
                return False

            row = cursor.fetchone()
            if not row:
                print(f"[purchase_sweet ERROR] Sweet not found: {sweet_id_or_name}")
                return False

            sweet_id, current_quantity = row

            if current_quantity < quantity:
                raise StockError(f"Not enough stock. Available: {current_quantity}, Requested: {quantity}")

            new_quantity = current_quantity - quantity
            self.conn.execute("UPDATE sweets SET quantity = ? WHERE id = ?", (new_quantity, sweet_id))
            self.conn.commit()
            return True

        except StockError:
            raise

        except Exception as e:
            print(f"[purchase_sweet ERROR] {e}")
            return False
