from .book_table import Table
alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"

class DisplayTable(Table):
    def __init__(self, tablepath):
        super().__init__(tablepath)

    def available_tables(self):
        print()
        print(f"{"Table No."}     {"Available Seats"}")
        print("------------------------------------")
        
        for table in self.tablelist:
            print(f"   {table["table_no"]}                     {table["available_seats"]}")

display_table_obj = DisplayTable(alltable_path)


