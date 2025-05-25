import os,sys
sys.path.append(os.getcwd())
from SRC.Domain.Validation import validation_obj
from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj


class RestaurantUsers:
    def user_signup(self):
        try:
            userdict = {}
            userdict["name"] = validation_obj.user_name()
            userdict["user_role"] = validation_obj.user_role(role = "staff")
            userdict["email"] = validation_obj.user_email()
            userdict["contact"] = validation_obj.user_contact()
            userdict["address"] = validation_obj.user_address()
            userdict["user_id"] = userdict["name"].split()[-1] + "_" + validation_obj.id_unique()
            userdict["password"] = validation_obj.user_password()
            userdict["joined_date"] = file_operation_obj.get_errdetails(get_date=True)
            file_operation_obj.userlist.append(userdict)
            file_operation_obj.write_file()
            print(f"\033[32m\n{userdict["name"]} Signed up Successfully as Staff :) \033[0m")
            print()
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

signup_obj = RestaurantUsers()
