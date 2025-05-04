import sys,os
sys.path.append(os.getcwd())
from SRC.Domain import operation_obj
alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"

class Table:
    def __init__(self,tablepath):
        self.alltable_path = tablepath
        self.tablelist = operation_obj.read_file(self.alltable_path)

    def add_table(self):
        table =  0
        while True:
            add_table = input("Add Table: y/n")
            if add_table == "n":
                break
            elif add_table == "y":
                table += 1
                tabledict = {}
                tabledict["table_no"] = f"Table {table}"
                tabledict["total_seat"] = 4  
                self.tablelist.append(tabledict)
                print("Table added to Restaurant Successfully...")

        operation_obj.write_file(data=self.tablelist,path=self.alltable_path)

    def table_book(self):
        pass

table_obj = Table(alltable_path) 