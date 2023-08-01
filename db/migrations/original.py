# CREATED AT: 2021-10-20 21:00:00.000000
import sqlite3
from datetime import datetime

def migrate():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('../database.db')
        c = conn.cursor()

        # Create the configs table
        c.execute('''
            CREATE TABLE configs (
                ID INTEGER PRIMARY KEY,
                key TEXT NOT NULL,
                value TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')

        # Create the accounts table
        c.execute('''
            CREATE TABLE accounts (
                ID INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')

        # Create the categories table
        c.execute('''
            CREATE TABLE categories (
                ID INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')

        # Create the transactions table
        c.execute('''
            CREATE TABLE transactions (
                ID INTEGER PRIMARY KEY,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                account_id INTEGER,
                category_id INTEGER,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY(account_id) REFERENCES accounts(ID),
                FOREIGN KEY(category_id) REFERENCES categories(ID)
            )
        ''')

        # Create the meta table
        c.execute('''
            CREATE TABLE meta (
                ID INTEGER PRIMARY KEY,
                account_id INTEGER,
                transaction_id INTEGER,
                category_id INTEGER,
                key TEXT NOT NULL,
                value TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY(account_id) REFERENCES accounts(ID),
                FOREIGN KEY(transaction_id) REFERENCES transactions(ID),
                FOREIGN KEY(category_id) REFERENCES categories(ID)
            )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("Database migration successful.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    migrate()
