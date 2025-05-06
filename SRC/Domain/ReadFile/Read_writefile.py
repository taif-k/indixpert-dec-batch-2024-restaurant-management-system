import json
import traceback
import datetime
import os,sys
sys.path.append(os.getcwd())

userdata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_staff.json"
error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"
admindata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_admin.json"

class DataFile:
    def __init__(self, path, err_path,admin_path):
        self.user_path = path
        self.err_path = err_path
        self.admin_path = admin_path
        self.userlist = self.read_file()
        self.adminlist = self.read_file(self.admin_path)

    def write_file(self, data = None, path = None,mode = "w",isJson = 1):
        if data == None and path == None:
            data = self.userlist
            path = self.user_path

        with open(path,mode) as file:
            if isJson == 1:
                file.write(json.dumps(data,indent=3))
            else:
                file.write(f"\n{data}")    

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
            print("Resolving issue..")
            self.write_file(data=self.get_errdetails(err),path=self.err_path,mode="a",isJson=0)
            return []       

operation_obj = DataFile(userdata_path,error_path,admindata_path)