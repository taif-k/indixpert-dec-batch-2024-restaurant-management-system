import uuid
import json
import traceback
import datetime
import os,sys
sys.path.append(os.getcwd())

from SRC.Domain import validation_obj
userdata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_users.json"
error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"

class RestaurantUsers:
    def __init__(self,path,err_path):
        self.user_path = path
        self.err_path = err_path
        self.userlist = self.read_file()

    def write_file(self, data = None, path = None):
        if data == None and path == None:
            data = self.userlist
            path = self.user_path
        with open(path,"w") as file:
            file.write(json.dumps(data,indent=3))    

    def get_errdetails(self,error = None, get_date = False):
        date = datetime.datetime.now()
        str_date = date.strftime("%d/%m/%Y, %H:%M:%S")

        if get_date == True:
            return str_date
        
        if error is not None:
            tb = traceback.extract_tb(error.__traceback__)[-1]
            module_name = os.path.basename(tb.filename)
            function_name = tb.name
            line_no = tb.lineno

            err_details = str({"module":module_name,"function":function_name,"error":error,"date":str_date,"line":line_no})
            return err_details
        
    def read_file(self):
        try:
            with open(self.user_path,"r") as file:
                user_data = json.load(file)
                return user_data     
        except Exception as err:
            self.write_file(self.get_errdetails(err),self.err_path)
            return []       

    def user_signup(self):
        userdict = {}
        userdict["name"] = validation_obj.user_name()
        userdict["email"] = validation_obj.user_email()
        userdict["contact"] = validation_obj.user_contact()
        userdict["address"] = validation_obj.user_address()
        userdict["user_id"] = userdict["name"] + "_" + str(uuid.uuid4())[:4]
        userdict["user_role"] = "staff"
        userdict["password"] = validation_obj.user_password()
        userdict["joined_date"] = self.get_errdetails(get_date=True)
        self.userlist.append(userdict)
        self.write_file()

user_obj = RestaurantUsers(userdata_path,error_path)