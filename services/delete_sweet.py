import sqlite3
from database.db import Database


class DeleteSweetService:
    def __init__(self, db_name='sweetshop.db'):
        self.db = Database(db_name)
        self.conn = self.db.get_connection()

    def delete_sweet(self, sweet_id: int) -> bool:
        """
        Deletes a sweet with the given ID from the database.
        Returns True if deletion was successful (row existed), False otherwise.
        """
        query = "DELETE FROM sweets WHERE id = ?"

        try:
            with self.conn:
                cursor = self.conn.execute(query, (sweet_id,))
                if cursor.rowcount == 0:
                    print(f"[delete_sweet INFO] No sweet found with ID {sweet_id}")
                    return False
                return True

        except Exception as e:
            print(f"[delete_sweet ERROR] {e}")
            return False

