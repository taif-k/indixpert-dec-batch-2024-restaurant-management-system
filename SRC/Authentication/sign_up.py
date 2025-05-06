import os,sys
sys.path.append(os.getcwd())
from SRC.Domain import validation_obj,operation_obj
userdata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_staff.json"
error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"

class RestaurantUsers:
    def __init__(self,path,err_path):
        self.__user_path = path
        self.__err_path = err_path

    def user_signup(self):
        try:
            userdict = {}
            userdict["name"] = validation_obj.user_name()
            userdict["user_role"] = validation_obj.user_role()
            userdict["email"] = validation_obj.user_email()
            userdict["contact"] = validation_obj.user_contact()
            userdict["address"] = validation_obj.user_address()
            userdict["user_id"] = userdict["name"].split()[-1] + "_" + validation_obj.id_unique()
            userdict["password"] = validation_obj.user_password()
            userdict["joined_date"] = operation_obj.get_errdetails(get_date=True)
            operation_obj.userlist.append(userdict)
            operation_obj.write_file()
        except Exception as err:
            print("Resolving issue....check after some time")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
            

signup_obj = RestaurantUsers(userdata_path,error_path)
