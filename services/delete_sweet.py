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

        if not isinstance(sweet_id, int) or sweet_id <= 0:
            print(f"[delete_sweet ERROR] Invalid ID: {sweet_id}")
            return False
        
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

    def delete_sweet_by_name(self, name: str) -> bool:
        """
        Deletes a sweet from the database by its name.
        Returns True if deletion was successful, False if no match.
        """
        if not isinstance(name, str) or not name.strip():
            print(f"[delete_sweet_by_name ERROR] Invalid name: {name}")
            return False

        query = "DELETE FROM sweets WHERE name = ?"

        try:
            with self.conn:
                cursor = self.conn.execute(query, (name.strip(),))
                if cursor.rowcount == 0:
                    print(f"[delete_sweet_by_name INFO] No sweet found with name '{name}'")
                    return False
                return True

        except Exception as e:
            print(f"[delete_sweet_by_name ERROR] {e}")
            return False