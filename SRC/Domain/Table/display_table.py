from .book_table import Table
alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj

class DisplayTable(Table):
    def __init__(self, tablepath):
        super().__init__(tablepath)

    def available_tables(self):
        self.tablelist = operation_obj.read_file(self.alltable_path)
        print()
        print(f"{print_obj.tableno}     {print_obj.availableseat}")
        print("------------------------------------")
        
        for table in self.tablelist:
            print(f"   {table["table_no"]}                     {table["available_seats"]}")

display_table_obj = DisplayTable(alltable_path)


