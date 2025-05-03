import uuid
import os,sys
sys.path.append(os.getcwd())

userdata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_users.json"
error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"

class RestaurantUsers:
    def __init__(self,path,err_path):
        self.user_path = path
        self.err_path = err_path

    def user_signup(self):
        try:
            from SRC.Domain import validation_obj,operation_obj
            userdict = {}
            userdict["name"] = validation_obj.user_name()
            userdict["email"] = validation_obj.user_email()
            userdict["contact"] = validation_obj.user_contact()
            userdict["address"] = validation_obj.user_address()
            userdict["user_id"] = userdict["name"] + "_" + validation_obj.user_id()
            userdict["user_role"] = "staff"
            userdict["password"] = validation_obj.user_password()
            userdict["joined_date"] = operation_obj.get_errdetails(get_date=True)
            operation_obj.userlist.append(userdict)
            operation_obj.write_file()
        except Exception as err:
            print("Resolving issue....check after some time")
            operation_obj.write_error(operation_obj.get_errdetails(err))
            

user_obj = RestaurantUsers(userdata_path,error_path)