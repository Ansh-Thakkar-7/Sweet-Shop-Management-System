import sqlite3

import sqlite3

class Database:
    def __init__(self, db_name='sweetshop.db'):
        """
        Initializes the database connection and ensures the 'sweets' table exists.
        If the database file doesn't exist, it will be created automatically.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_sweets_table()

    def create_sweets_table(self):
        """
        Creates the 'sweets' table in the database if it does not already exist.
        The table stores information about each sweet: id, name, category, price, and quantity.
        """
        query = """
        CREATE TABLE IF NOT EXISTS sweets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def get_connection(self):
        """
        Returns the current active SQLite database connection.
        Useful for accessing the DB from other service classes.
        """
        return self.conn

    def close_connection(self):
        """
        Closes the active database connection.
        Should be called when DB operations are complete to free resources.
        """
        self.conn.close()

if __name__ == "__main__":
    db = Database()
    print("Database and table created successfully.")
    db.close_connection()