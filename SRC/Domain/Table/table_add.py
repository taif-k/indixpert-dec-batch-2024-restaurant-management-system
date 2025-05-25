from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj

# admin can add new table to restaurant
class Table:
    alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"

    def __init__(self):
        self.tablelist = file_operation_obj.read_file(path_obj.alltable_path)

    def add_table(self):
        try:
            add_newtable = input("Add Table to Restaurant y/n: ").lower()
            if add_newtable != "y":
                print(print_obj.notable_msg)
                return None

            largest_table_no = 0
            for table in self.tablelist:
                if table["table_no"] > largest_table_no:
                    largest_table_no = table["table_no"]

            tabledict = {"table_no": largest_table_no + 1,"slot1": 4,  "slot2": 4,  "slot3": 4, "slot4":4}

            self.tablelist.append(tabledict)

            print(f"Table no {largest_table_no + 1} added to Restaurant Successfully...")
            file_operation_obj.write_file(data=self.tablelist,path=path_obj.alltable_path)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

table_obj = Table()