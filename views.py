import os

from service import (
    productservice,
    orderservice,
    reprotservice,
    loginservice,
    manu_bar,
    userservice,
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def productMenu():
    while True:
        clear_screen()
        print("--- Product Management ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("0. Back to Main Menu")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    product_service = productservice()
                    product_data = product_service.add_product()
                    product_service.save_product(product_data)
                    print("Product added successfully!")
                case 2:
                    product_service = productservice()
                    product_service.view_products()
                case 3:
                    product_service = productservice()
                    product_service.update_product()
                case 4:
                    product_service = productservice()
                    product_service.delete_product()
                case 0:
                    return
                case _:
                    print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")


def orderMenu():
    while True:
        clear_screen()
        print("--- Order Management ---")
        print("1. Create Order")
        print("2. View Orders")
        print("0. Back to Main Menu")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    order_service = orderservice()
                    order_service.create_order()
                case 2:
                    order_service = orderservice()
                    order_service.view_orders()
                case 0:
                    return
                case _:
                    print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")


def manuHandle():
    try:
        login_service = loginservice()
        user_data = login_service.login()
        validate_user = login_service.validate_user(user_data)
        if validate_user:
            print("Login successful")
            while True:
                clear_screen()
                print("--- Main Menu ---")
                print("1. Product Management")
                print("2. Order Management")
                print("3. Generate Report")
                print("4. Logout")
                try:
                    choice = int(input("Enter your choice: "))
                    match choice:
                        case 1:
                            productMenu()
                        case 2:
                            orderMenu()
                        case 3:
                            report_service = reprotservice()
                            report_service.generate_report()
                            print("\nPress Enter to continue...")
                            input()
                        case 4:
                            print("Logging out...")
                            return
                        case 0:
                            print("Invalid input")
                except ValueError:
                    print("Please enter a valid number")
        else:
            print("sorry the user name and password is invalid")
    except Exception as e:
        print(f"Error: {e}")


def registerHandle():
    try:
        user_service = userservice()
        user_list = user_service.create_user()
        user_service.save_user(user_list)
        print("Register successful")
        manuHandle()
    except Exception as e:
        print(f"Error during registration: {e}")


while True:
    clear_screen()
    menu = manu_bar()
    option = menu.authentaition()

    match option:
        case 1:
            manuHandle()

        case 2:
            try:
                print("1. Register\n2. Login")
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        registerHandle()
                    case 2:
                        manuHandle()
            except ValueError:
                print("Invalid input. Please enter a number.")

        case 3:
            print("Exiting...")
            break

        case 0:
            print("Invalid input")
