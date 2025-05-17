import json
import traceback
import datetime
import os

class DataFile:
    userdata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_staff.json"
    error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"
    admindata_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\registered_admin.json"

    def __init__(self):
        self.userlist = self.read_file()
        self.adminlist = self.read_file(self.admindata_path)

    def write_file(self, data = None, path = None,mode = "w",isJson = 1):
        if data == None and path == None:
            data = self.userlist
            path = self.userdata_path

        with open(path,mode) as file:
            if isJson == 1:
                file.write(json.dumps(data,indent=3))
            else:
                file.write(f"\n{data}")    

    def get_errdetails(self,error = None, get_date = False):
        date = datetime.datetime.now()
        str_date = date.strftime("%Y-%m-%d %H:%M:%S")

        if get_date == True:
            return str_date
        
        if error is not None:
            tb = traceback.extract_tb(error.__traceback__)[-1]
            module_name = os.path.basename(tb.filename)
            function_name = tb.name
            line_no = tb.lineno

            err_details = str({"module":module_name,"function":function_name,"error":error,"date":str_date,"line":line_no}) #will check and do str(error)
            return err_details
        
    def read_file(self,path = None):
        if path == None:
            path = self.userdata_path

        try:
            with open(path,"r") as file:
                user_data = json.load(file)
                return user_data     
        except Exception as err:
            print("Resolving issue..")
            self.write_file(data=self.get_errdetails(err),path=self.error_path,mode="a",isJson=0)
            return []       

operation_obj = DataFile()