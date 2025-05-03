import sys,os
sys.path.append(os.getcwd())
import json
from SRC.Domain import operation_obj,foodmenu_obj,removemenu_obj


class User:
    def login_menu(self):
        print()
        print("1 - Admin Login")
        print("2 - Staff Login")
        print("0 - Go Back")

    def admin_menu(self):
        print("1 - Add Food Item")
        print("2 - Remove Food Item")
        print("3 - Display Menu")
        print("0 - Logout")

    def admin_option(self):
        while True:
            self.admin_menu()
            admin_option = int(input("Enter admin option: "))
            if admin_option == 1:
                foodmenu_obj.add_menu()
            elif admin_option == 2:
                removemenu_obj.remove_menu()
            elif admin_option == 3:
                print(json.dumps(foodmenu_obj.foodmenu_list,indent=3))
            elif admin_option == 4:
                pass # cancel order/table
            elif admin_option == 0:
                break
            else:
                print("Choose valid option ")

    def staff_menu(self):
        print("1 - Display Menu")
        print("2 - Place Order")
        print("3 - See available Table")
        print("4 - Book Table")
        print("5 - pay")
        print("6 - Generate Bill")

    def admin_login(self):
        self.__admin_email = input("Enter email: ")
        self.__admin_password = input("Enter password: ")
        admin_verified = 0
        for user in operation_obj.userlist:
            if user["email"] == self.__admin_email and self.__admin_email == "admin@mail.com":
                if user["password"] == self.__admin_password and self.__admin_password == "pass@word":
                    self.admin_option()
                    admin_verified = 1
                    break

        if admin_verified == 0:
            print("Invalid Credentials")        


    def staff_login(self):
        staff_email = input("Enter email: ")
        staff_password = input("Enter password: ")
        staff_verified = 0
        for user in operation_obj.userlist:
            if user["email"] == staff_email:
                if user["password"] == staff_password:
                    self.staff_menu()
                    staff_verified = 1
                    break
        if staff_verified == 0:
            print("Invalid Credentials") 


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

login_obj = User()
