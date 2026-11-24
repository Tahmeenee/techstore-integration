import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "data" / "techstore.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def get_products():
    connection = get_connection()

    cursor = connection.execute("""
        SELECT product_id, product_name, category, unit_price
        FROM products
    """)

    products = cursor.fetchall()
    connection.close()

    return products