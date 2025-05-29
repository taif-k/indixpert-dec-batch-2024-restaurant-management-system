from .table_add import Table
from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj

# available updated seats are shown when staff press 4 or 2 for advance booking and order plac respectively
class DisplayTable(Table):

    def __init__(self):
        super().__init__()
    
    def available_tables(self):
        try:
            self.tablelist = file_operation_obj.read_file(path_obj.alltable_path)

            print()
            print(f"{print_obj.tableno:<15}{'slot 1 (11:00 AM - 01:00 PM)':<35}{'slot 2 (02:00 PM - 04:00 PM)':<35}{'slot 3 (05:00 PM - 07:00 PM)':<35}{'slot 4 (08:00 PM - 10:00 PM)'}")
            print("-" * 160)
            for table in self.tablelist:
                print(f"{table['table_no']:<25}{table['slot1']:<35}{table['slot2']:<35}{table['slot3']:<35}{table['slot4']}")
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

display_table_obj = DisplayTable()