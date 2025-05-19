import json
import traceback
import datetime
import os
from SRC.Domain.Path.all_paths import path_obj

class DataFile:

    def __init__(self):
        self.userlist = self.read_file()
        self.adminlist = self.read_file(path_obj.admindata_path)

    def write_file(self, data = None, path = None,mode = "w",isJson = 1):
        if data == None and path == None:
            data = self.userlist
            path = path_obj.userdata_path

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

            err_details = json.dumps({"module":module_name,"function":function_name,"error":str(error),"date":str_date,"line":line_no}) #will check and do str(error)
            return err_details
        
    def read_file(self,path = None):
        if path == None:
            path = path_obj.userdata_path

        try:
            with open(path,"r") as file:
                if path == path_obj.error_path:
                    err_list = []
                    for line in file:
                        err_list.append(json.loads(line))
                    return err_list
                else:
                    return json.load(file)
                
        except Exception as err:
            print("Resolving issue..")
            self.write_file(data=self.get_errdetails(err),path=path_obj.error_path,mode="a",isJson=0)
            return []       

operation_obj = DataFile()