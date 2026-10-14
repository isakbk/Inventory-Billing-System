from database import create_tables


class userservice:
    def create_user(self):
        print("-----------Create User-----------")
        user_id = input("Enter user id: ")
        user_email = input("Enter user email: ")
        user_name = input("Enter user name: ")
        user_password = input("Enter user password: ")
        user_phone_number = input("Enter user phone number: ")
        user_status = input("Enter user status: ")
        user_created_at = input("Enter user created at: ")
        user_type = input("Enter user type: ")

        user_list = [
            user_id,
            user_email,
            user_name,
            user_password,
            user_phone_number,
            user_status,
            user_created_at,
            user_type,
        ]
        return user_list

    def save_user(self, user_list):
        try:
            database = create_tables()
            database.cursor.execute(
                "INSERT INTO userModel VALUES(?, ?, ?, ?, ?, ?, ?, ?)", user_list
            )
            database.conn.commit()
        except Exception as e:
            print(f"Error saving user: {e}")


class loginservice:
    def login(self):
        print("-----------Login-----------")
        self.user_email = input("Enter user email: ")
        self.user_password = input("Enter user password: ")
        self.user_data = [self.user_email, self.user_password]
        return self.user_data

    def validate_user(self, user_data):
        try:
            database = create_tables()
            database.cursor.execute(
                "SELECT * FROM userModel WHERE user_email = ? AND user_password = ?",
                user_data,
            )
            user = database.cursor.fetchone()
            if user:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error validating user: {e}")
            return False

        # TODO: Add login logic here


class productservice:
    def add_product(self):
        print("-----------Create Product-----------")
        product_id = input("Enter product id: ")
        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")
        product_quantity = input("Enter product quantity: ")
        product_category = input("Enter product category: ")
        product_description = input("Enter product description: ")
        product_status = input("Enter product status: ")
        product_created_at = input("Enter product created at: ")
        product_updated_at = input("Enter product updated at: ")
        product_data = [
            product_id,
            product_name,
            product_price,
            product_quantity,
            product_category,
            product_description,
            product_status,
            product_created_at,
            product_updated_at,
        ]
        return product_data

    def view_products(self):
        print("-----------View Products-----------")

    def update_product(self):
        print("-----------Update Product-----------")

    def delete_product(self):
        print("-----------Delete Product-----------")

    def save_product(self, product_data):
        try:
            database = create_tables()
            database.cursor.execute(
                "INSERT INTO productModel VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                product_data,
            )
            database.conn.commit()
        except Exception as e:
            print(f"Error saving product: {e}")


class orderservice:
    def create_order(self):
        print("-----------Create Order-----------")
        order_id = input("Enter order id")
        order_quantity = input("Enter order quantity:")

    def view_orders(self):
        print("-----------View Orders-----------")

    def save_order(self, order_data):
        try:
            database = create_tables()
            database.cursor.execute(
                "INSERT INTO orderModel VALUES(?, ?, ?, ?)", order_data
            )
            database.conn.commit()
        except Exception as e:
            print(f"Error saving order: {e}")


class reprotservice:
    def generate_report(self):
        try:
            print("printing report...")
            createtable = create_tables()
            product_data = createtable.cursor.execute("SELECT * FROM productModel")
            for product in product_data.fetchall():
                print(product[0])
                print(product[1])
                print(product[2])
                print(product[3])
                print(product[4])
                print(product[5])
                print(product[6])
                print(product[7])
                print(product[8])
                print("----------------")

            user_data = createtable.cursor.execute("SELECT * FROM userModel")
            for user in user_data.fetchall():
                print(user[0])
                print(user[1])
                print(user[2])
                print(user[3])
                print(user[4])
                print(user[5])
                print(user[6])
                print(user[7])
                print("----------------")

            order_data = createtable.cursor.execute("SELECT * FROM orderModel")
            for order in order_data.fetchall():
                print(order[0])
                print(order[1])
                print(order[2])
                print(order[3])
                print("----------------")
        except Exception as e:
            print(f"Error generating report: {e}")


class seles_detail:
    @staticmethod
    def total_sales_create():
        try:
            createtable = create_tables()
            total_sales = createtable.cursor.execute(
                "SELECT SUM(product_price) FROM orderModel"
            )
            total_sales = total_sales.fetchone()[0]
            print(f"Total Sales: {total_sales}")
            return total_sales
        except Exception as e:
            print(f"Error calculating total sales: {e}")
            return 0

    def total_sales_insert(self, total_sales):
        try:
            createtable = create_tables()
            createtable.cursor.execute(
                "INSERT INTO salesModel VALUES(?, ?, ?)", (total_sales, 0, 0)
            )
            createtable.conn.commit()
        except Exception as e:
            print(f"Error inserting total sales: {e}")

    def profit_insert(self, total_sales):
        try:
            profit = total_sales * 0.1
            createtable = create_tables()
            createtable.cursor.execute(
                "INSERT INTO salesModel VALUES(?, ?, ?)", (0, profit, 0)
            )
            createtable.conn.commit()
        except Exception as e:
            print(f"Error inserting profit: {e}")

    def loss_insert(self, total_sales):
        try:
            loss = total_sales * 0.9
            createtable = create_tables()
            createtable.cursor.execute(
                "INSERT INTO salesModel VALUES(?, ?, ?)", (0, 0, loss)
            )
            createtable.conn.commit()
        except Exception as e:
            print(f"Error inserting loss: {e}")


class manu_bar:
    def main_menu(self):
        try:
            print("1. Create Product")
            print("2. Create Order")
            print("3. Generate Report")
            print("4. Exit")
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 0

    def authentaition(self):
        try:
            print("-----------Authentication-----------")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            return int(input("Enter your choice:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 0
