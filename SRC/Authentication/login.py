from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Menu import foodmenu_obj,removemenu_obj,updateitem_obj,display_menu_obj
from SRC.Domain.Table.book_table import table_obj
from SRC.Domain.Table.display_table import display_table_obj
from SRC.Domain.Order import order_obj,cancel_obj
from SRC.Domain.Payment import pay_obj
from abc import ABC,abstractmethod
import pwinput

class User(ABC):
    @abstractmethod
    def user_login(self):
        pass

    @abstractmethod
    def user_menu(self):
        pass

    @abstractmethod
    def user_option(self):
        pass

class Admin(User):
    def user_menu(self):
        print()
        print("1 - Add Food Item")
        print("2 - Remove Food Item")
        print("3 - Update Food item Price")
        print("4 - Display Menu")
        print("5 - Add Table")
        print("6 - Cancel Order")
        print("0 - Admin Logout")
        

    def user_option(self):
        while True:
            try:
                self.user_menu()
                admin_option = int(input("Enter admin option: "))
                if admin_option == 1:
                    foodmenu_obj.add_menu()
                elif admin_option == 2:
                    removemenu_obj.remove_menu()
                elif admin_option == 3:
                    updateitem_obj.update_item()
                elif admin_option == 4:
                    display_menu_obj.formatted_menu()
                elif admin_option == 5:
                    table_obj.add_table()
                elif admin_option == 6:
                    cancel_obj.order_cancel()
                elif admin_option == 0:
                    break
                else:
                    print("Choose valid option ")
            except Exception as err:
                print("Resolving issue..Try again after some time")
                operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

    def user_login(self):
        try:
            admin_email = input("Enter admin email: ").lower()
            admin_password = pwinput.pwinput(prompt="Enter admin password: ",mask="#")
            admin_verified = 0
            for user in operation_obj.adminlist:
                if user["email"] == admin_email:
                    if user["password"] == admin_password: 
                        self.user_option()
                        admin_verified = 1
                        break

            if admin_verified == 0:
                print("Invalid Credentials")
        except Exception as err:
            print("Try again after some time...")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
admin_obj = Admin()

class Staff(User):
    def user_menu(self):
        print()
        print("1 - Display Menu")
        print("2 - Place Order")
        print("3 - See available Table")
        print("4 - Book Table")
        print("5 - pay Bill")
        print("0 - Staff Logout")

        
    def user_option(self):
        while True:
            try:
                self.user_menu()
                staff_option = int(input("Enter staff option: "))
                if staff_option == 1:
                    display_menu_obj.formatted_menu()
                elif staff_option == 2:
                    order_obj.book_order()
                elif staff_option == 3:
                    display_table_obj.available_tables()
                elif staff_option == 4:
                    order_obj.select_table()
                elif staff_option == 5:
                    pay_obj.payment_option()
                elif staff_option == 0:
                    break
            except Exception as err:
                operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

    def user_login(self):
        staff_email = input("Enter staff email: ").lower()
        staff_password = pwinput.pwinput(prompt="Enter staff password: ",mask="#")
        staff_verified = 0
        for user in operation_obj.userlist:
            if user["email"] == staff_email:
                if user["password"] == staff_password:
                    self.user_option()
                    staff_verified = 1
                    break
        if staff_verified == 0:
            print("Invalid Credentials") 
staff_obj = Staff()

class UserOption():
    def select_user(self):
        print()
        print("1 - Admin Login")
        print("2 - Staff Login")
        print("0 - Go Back")

    def user_login(self):
        while True:
            self.select_user()
            ask_login = int(input("Enter Login Option: "))
            if ask_login == 1:
                admin_obj.user_login()
            elif ask_login == 2:
                staff_obj.user_login()
            elif ask_login == 0:
                break
            else:
                print("Choose valid option")

login_obj = UserOption()