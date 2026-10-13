import sqlite3



class create_tables:
 conn=sqlite3.connect("shop.db")
 cursor=conn.cursor()   
 def __inti__(self):
    
    cursor.execute("PRAGRMA foreign_key=on")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER primary key,
        user_name TEXT NOT NULL,
        user_password TEXT NOT NULL,
        user_phone_number TEXT NOT NULL,
        user_status TEXT NOT NULL,
        user_created_at TEXT NOT NULL,
        user_type TEXT NOT NULL
        )

        CREATE TABLE IF NOT EXISTS product(
          
          product_id INTEGER PRIMARY KEY,
          product_name TEXT NOT NULL,
          product_price REAL NOT NULL,
          product_quantity INTEGER NOT NULL,
          product_description TEXT,
          product_categories TEXT NOT NULL,
          product_created_at TEXT NOT NULL
         ) 

        CREATE TABLE IF NOT EXISTS order(
          order_id INTEGER PRIMARY KEY,
          FORIEGN KEY (product_id) REFERENCES product(product_id)
          FORIEGN KEY (user_id) REFERENCES  user(user_id)
          order_at TEXT NOT NULL    
        )

        CREATE TABLE IF NOT EXISTS sales(
           total_sale INTEGER NOT NULL,
           profit INTEGER NOT NULL,
           loss INTEGER NOT NULL
           ) 

    """)