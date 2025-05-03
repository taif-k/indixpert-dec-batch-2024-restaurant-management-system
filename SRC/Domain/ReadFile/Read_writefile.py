import json
import traceback
import datetime
import os,sys
sys.path.append(os.getcwd())

userdata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_users.json"
error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"

class DataFile:
    def __init__(self, path, err_path):
        self.user_path = path
        self.err_path = err_path
        self.userlist = self.read_file()

    def write_file(self, data = None, path = None):
        if data == None and path == None:
            data = self.userlist
            path = self.user_path

        with open(path,"w") as file:
            file.write(json.dumps(data,indent=3))

    def write_error(self,err_data):
        with open(self.err_path,"a") as file:
            file.write(f"\n{err_data}")    

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
        
    def read_file(self,path = None):
        if path == None:
            path = self.user_path

        try:
            with open(path,"r") as file:
                user_data = json.load(file)
                return user_data     
        except Exception as err:
            self.write_error(self.get_errdetails(err))
            return []       

operation_obj = DataFile(userdata_path,error_path)