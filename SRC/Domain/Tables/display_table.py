from .book_table import Table
alltable_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\alltables.json"

class DisplayTable(Table):
    def __init__(self, tablepath):
        super().__init__(tablepath)

    def available_tables(self):
        print("\n         Available Tables")
        print(f"{"Table No.":<15}{"Available Seats":<15}")
        print("-------------------------------------------")
        
        for table in self.tablelist:
            print(f"{table["table_no"]:<15}{table["available_seats"]:<15}")

display_table_obj = DisplayTable(alltable_path)

