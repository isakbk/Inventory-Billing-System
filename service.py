from database import create_tables



class userservice:
    def create_user(self):
        print("-----------Create User-----------")
        user_id = input("Enter user id: ")
        user_name = input("Enter user name: ")
        user_password = input("Enter user password: ")
        user_phone_number = input("Enter user phone number: ")
        user_status = input("Enter user status: ")
        user_created_at = input("Enter user created at: ")
        user_type = input("Enter user type: ")
        
        user_list=[user_id, user_name, user_password, user_phone_number, user_status, user_created_at, user_type]
        return user_list


    def save_user(self, user_list):
        database=create_tables()
        database.execute("INSERT INTO userModel VALUES(?, ?, ?, ?, ?, ?, ?)", user_list)
        database.commit()

    
          


class loginservice:
    def login(self):
        print("-----------Login-----------")
        self.user_email=input("Enter user email: ")
        self.user_password=input("Enter user password: ")
        self.user_data=[self.user_email,self.user_password]
        return self.user_data

    def validate_user(self,user_data):
        database=create_tables()
        database.execute("SELECT * FROM userModel WHERE user_email = ? AND user_password = ?", user_data)
        user=database.fetchone()
        if user:
            return True
        else:
            return False



        
        # TODO: Add login logic here

class productservice:
    def create_product(self):
      print("-----------Create Product-----------") 
      product_id=input("Enter product id: ")
      product_name=input("Enter product name: ")
      product_price=input("Enter product price: ")
      product_quantity=input("Enter product quantity: ")
      product_category=input("Enter product category: ")
      product_description=input("Enter product description: ")
      product_status=input("Enter product status: ")
      product_created_at=input("Enter product created at: ")
      product_updated_at=input("Enter product updated at: ")
      product_data=[product_id, product_name, product_price, product_quantity, product_category, product_description, product_status, product_created_at, product_updated_at]
      return product_data
    
    def save_product(self,product_data):
        database=create_tables()
        database.execute("INSERT INTO productModel VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", product_data)
        database.commit()


class orderservice:
    def create_order(self):
      print("-----------Create Order-----------")

class reprotservice:
    def generate_report(self):
      print("-----------Generate Report-----------")



