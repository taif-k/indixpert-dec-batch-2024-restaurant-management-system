from SRC.Authentication import user_obj

class User:
    def login_menu(self):
        print()
        print("1 - Admin Login")
        print("2 - Staff Login")
        print("0 - Go Back")

    def admin_menu(self):
        print("1 - See menu")
        print("2 - Remove Menu Item")
        print("3 - Add Menu Item")
        print("4 - Cancel table")
        print("5 - Logout")

    def staff_menu(self):
        print("1 - Display Menu")
        print("2 - Place Order")
        print("3 - See available Table")
        print("4 - Book Table")
        print("5 - pay")
        print("6 - Generate Bill")

    def admin_login(self):
        admin_email = input("Enter email: ")
        admin_password = input("Enter password: ")
        admin_verified = 0
        for user in user_obj.userlist:
            if user["email"] == admin_email:
                if user["password"] == admin_password:
                    self.admin_menu()
                    admin_verified = 1
                    break

        if admin_verified == 0:
            print("Invalid Credentials")        


    def staff_login(self):
        staff_email = input("Enter email: ")
        staff_password = input("Enter password: ")
        staff_verified = 0
        for user in user_obj.userlist:
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
