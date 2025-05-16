from SRC.Authentication import signup_obj,login_obj
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj

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
            try:
                self.authentication_menu()
                authentication_type = int(input(print_obj.enter_option))
                if authentication_type == 1:
                    signup_obj.user_signup()
                elif authentication_type == 2:
                    login_obj.user_login()
                elif authentication_type == 0:
                    break
                else:
                    print(print_obj.invalid_msg)
            except Exception as err:
                print(print_obj.err_msg)
                operation_obj.write_file(data = operation_obj.get_errdetails(err),path=operation_obj.error_path,mode="a",isJson=0)
