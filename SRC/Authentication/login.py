import sys,os
sys.path.append(os.getcwd())
import json
from SRC.Domain import operation_obj,foodmenu_obj,removemenu_obj,table_obj,order_obj


class User:
    def login_menu(self):
        print()
        print("1 - Admin Login")
        print("2 - Staff Login")
        print("0 - Go Back")

class Admin(User):
    def admin_menu(self):
        print()
        print("1 - Add Food Item")
        print("2 - Remove Food Item")
        print("3 - Display Menu")
        print("4 - Add Table")
        print("0 - Admin Logout")

    def admin_option(self):
        while True:
            try:
                self.admin_menu()
                admin_option = int(input("Enter admin option: "))
                if admin_option == 1:
                    foodmenu_obj.add_menu()
                elif admin_option == 2:
                    removemenu_obj.remove_menu()
                elif admin_option == 3:
                    print(json.dumps(foodmenu_obj.foodmenu_list,indent=3))
                elif admin_option == 4:
                    table_obj.add_table()
                elif admin_option == 0:
                    break
                else:
                    print("Choose valid option ")
            except Exception as err:
                print("Resolving issue..Try again after some time")
                operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

    def admin_login(self):
        try:
            self.__admin_email = input("Enter admin email: ").lower()
            self.__admin_password = input("Enter admin password: ")
            admin_verified = 0
            for user in operation_obj.adminlist:
                if user["email"] == self.__admin_email:
                    if user["password"] == self.__admin_password: 
                        self.admin_option()
                        admin_verified = 1
                        break

            if admin_verified == 0:
                print("Invalid Credentials")
        except Exception as err:
            print("Try again after some time...")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

class Staff(User):
    def staff_menu(self):
        print()
        print("1 - Display Menu")
        print("2 - Place Order")
        print("3 - See available Table")
        print("4 - Book Table")
        print("5 - pay")
        print("6 - Generate Bill")
        print("0 - Staff Logout")
        
    def staff_option(self):
        while True:
            try:
                self.staff_menu()
                staff_option = int(input("Enter staff option: "))
                if staff_option == 1:
                    print(json.dumps(foodmenu_obj.foodmenu_list,indent=4))
                elif staff_option == 2:
                    order_obj.book_order()
                elif staff_option == 3:
                    print(json.dumps(table_obj.tablelist,indent=4))
                elif staff_option == 4:
                    pass
                elif staff_option == 5:
                    pass
                elif staff_option == 6:
                    pass
                elif staff_option == 0:
                    break
            except Exception as err:
                pass

    def staff_login(self):
        staff_email = input("Enter staff email: ").lower()
        staff_password = input("Enter staff password: ")
        staff_verified = 0
        for user in operation_obj.userlist:
            if user["email"] == staff_email:
                if user["password"] == staff_password:
                    self.staff_option()
                    staff_verified = 1
                    break
        if staff_verified == 0:
            print("Invalid Credentials") 

class UserOption(Admin,Staff):
    def user_login(self):
        while True:
            self.login_menu()
            ask_login = int(input("Enter Login Option: "))
            if ask_login == 1:
                self.admin_login()
            elif ask_login == 2:
                self.staff_login()
            elif ask_login == 0:
                break
            else:
                print("Choose valid option")

login_obj = UserOption()