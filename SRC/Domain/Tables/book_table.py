from SRC.Domain import operation_obj
alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"

class Table:
    def __init__(self,tablepath):
        self.alltable_path = tablepath
        self.tablelist = operation_obj.read_file(self.alltable_path)

    def add_table(self):
        try:
            add_newtable = input("Add Table to Restaurant y/n: ").lower()
            if add_newtable != "y":
                print("New Table not added")
                return None
            
            largest_table_no = 0
            for table in self.tablelist:
                if table["table_no"] > largest_table_no:
                    largest_table_no = table["table_no"]

            tabledict = {"table_no":largest_table_no + 1,"available_seats":4}
            self.tablelist.append(tabledict)

            print(f"Table no {largest_table_no + 1} added to Restaurant Successfully...")
            operation_obj.write_file(data=self.tablelist,path=self.alltable_path)
        except Exception as err:
            print("Try again after some time")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

table_obj = Table(alltable_path)