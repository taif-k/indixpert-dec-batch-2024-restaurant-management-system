from Authentication import user_obj,login_obj


class Restaurant:
    def __init__(self):
        pass
    
    def authentication_menu(self):
        print("1 - Sign Up")
        print("2 - Login")
        print("0 - Exit")

    def authentication_option(self):
        print("\n----Restaurant Managment System----\n")
        while True:
            self.authentication_menu()
            authentication_type = int(input("Enter option: "))
            if authentication_type == 1:
                user_obj.user_signup()
            elif authentication_type == 2:
                login_obj.user_login()
            elif authentication_type == 0:
                break
            else:
                print("Invalid option")