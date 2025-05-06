import sys,os
sys.path.append(os.getcwd())
from SRC.Domain import operation_obj
alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"

class Table:
    def __init__(self,tablepath):
        self.alltable_path = tablepath
        self.tablelist = operation_obj.read_file(self.alltable_path)

    def add_table(self):
        try:
            table =  0
            while True:
                add_table = input("Add Table: y/n")
                if add_table == "n":
                    break
                elif add_table == "y":
                    table += 1
                    tabledict = {}
                    tabledict["table_no"] = int(f"{table}")
                    tabledict["available_seats"] = 4  
                    self.tablelist.append(tabledict)
                    print("Table added to Restaurant Successfully...")
                else:
                    print("\nInvalid option")
            operation_obj.write_file(data=self.tablelist,path=self.alltable_path)
        except Exception as err:
            print("Try again after some time")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

table_obj = Table(alltable_path) 