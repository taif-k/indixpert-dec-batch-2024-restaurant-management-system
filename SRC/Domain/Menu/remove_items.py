from .add_items import MenuItem
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj

class RemoveFood(MenuItem):

    def __init__(self):
        super().__init__()

    def remove_menu(self):
        try:
            while True:
                food_id = input("Enter food item id to remove from menu: ")
                id_matched = 0
                for item in self.foodmenu_list:
                    if item["food_id"] == food_id:
                        self.foodmenu_list.remove(item)
                        id_matched = 1
                        break
                if id_matched == 0:
                    print(print_obj.noid_msg)

                remove_item = input("Remove item y/n: ")
                if remove_item != "y":
                    break

            operation_obj.write_file(data=self.foodmenu_list,path=self.foodmenu_path)
            print("Item Removed from Menu")
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.error_path,mode="a",isJson=0)

removemenu_obj = RemoveFood()