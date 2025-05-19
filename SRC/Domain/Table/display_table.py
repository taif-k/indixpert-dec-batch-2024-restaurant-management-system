from .book_table import Table
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj

class DisplayTable(Table):

    def __init__(self):
        super().__init__()

    def available_tables(self):
        self.tablelist = operation_obj.read_file(self.alltable_path)

        print()
        print(f"{print_obj.tableno}     {"slot 1 (11:00 Am - 02:00 Pm)"}     {"slot 2 (03:00 pm - 05:00 Pm)"}     {"slot 3 (08:00 Pm - 10:00 Pm)"}")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        
        for table in self.tablelist:
            print(f"   {table["table_no"]}\t\t\t\t  {table["slot1"]}\t\t\t  {table["slot2"]}\t\t\t    {table["slot3"]}")

display_table_obj = DisplayTable()





















# from .book_table import Table
# alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"
# from SRC.Domain.ReadFile import operation_obj
# from SRC.Domain.Validation import print_obj

# class DisplayTable(Table):
#     def __init__(self, tablepath):
#         super().__init__(tablepath)

#     def available_tables(self):
#         self.tablelist = operation_obj.read_file(self.alltable_path)
#         print()
#         print(f"{print_obj.tableno}     {"slot 1 (11:00 am - 1:00 pm)"}     {"slot 2 (01:00 pm - 3:00 pm)"}     {"slot 3 (3:00 pm - 5:00 pm)"}")
#         print("----------------------------------------------------------------------------------------------------------")
        
#         for table in self.tablelist:
#             print(f"   {table["table_no"]}\t\t\t\t{table["slot1"]}\t\t\t\t{table["slot2"]}\t\t\t\t{table["slot3"]}")

# display_table_obj = DisplayTable(alltable_path)


