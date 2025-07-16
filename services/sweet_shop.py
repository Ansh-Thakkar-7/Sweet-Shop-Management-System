from database.db import Database
from models.sweet import Sweet


class SweetShop:
    """
    Service class to handle operations related to the sweet inventory.
    """
    def __init__(self):
        """
        Initializes the database connection.
        """
        self.db = Database()
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

        try:
            self.conn.execute(query, (sweet.id, sweet.name, sweet.category, sweet.price, sweet.quantity))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding sweet: {e}")
            return False