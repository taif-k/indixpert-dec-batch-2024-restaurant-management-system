from .book_table import Table
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj

class DisplayTable(Table):

    def __init__(self):
        super().__init__()

    def available_tables(self):
        self.tablelist = operation_obj.read_file(path_obj.alltable_path)

        print()
        print(f"{print_obj.tableno}     {'slot 1 (11:00 AM - 01:00 PM)'}     {'slot 2 (02:00 PM - 04:00 PM)'}     {'slot 3 (05:00 PM - 07:00 PM)'}     {'slot 4 (08:00 PM - 10:00 PM)'}")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

        for table in self.tablelist:
            print(f"   {table['table_no']}\t\t\t\t  {table['slot1']}\t\t\t  {table['slot2']}\t\t\t    {table['slot3']}\t\t\t    {table['slot4']}")

display_table_obj = DisplayTable()