import sqlite3


class create_tables:
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    def __init__(self):

        self.cursor.execute("PRAGMA foreign_key=on")
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS userModel(
        user_id INTEGER primary key,
        user_email TEXT NOT NULL,
        user_name TEXT NOT NULL,
        user_password TEXT NOT NULL,
        user_phone_number TEXT NOT NULL,
        user_status TEXT NOT NULL,
        user_created_at TEXT NOT NULL,
        user_type TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS productModel(
          
          product_id INTEGER PRIMARY KEY,
          product_name TEXT NOT NULL,
          product_price REAL NOT NULL,
          product_quantity INTEGER NOT NULL,
          product_description TEXT,
          product_category TEXT NOT NULL,
          product_status TEXT NOT NULL,
          product_created_at TEXT NOT NULL,
          product_updated_at TEXT NOT NULL
         );

        CREATE TABLE IF NOT EXISTS orderModel(
          order_id INTEGER PRIMARY KEY,
          product_id INTEGER,
          user_id INTEGER,
          order_at TEXT NOT NULL,
          FOREIGN KEY (product_id) REFERENCES productModel(product_id),
          FOREIGN KEY (user_id) REFERENCES userModel(user_id)
        );

        CREATE TABLE IF NOT EXISTS salesModel(
           total_sale INTEGER NOT NULL,
           profit INTEGER NOT NULL,
           loss INTEGER NOT NULL
           );
    """
        )
        self.conn.commit()
