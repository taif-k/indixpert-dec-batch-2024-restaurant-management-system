from .add_items import MenuItem
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Menu.display_items import display_menu_obj
from SRC.Domain.Path.all_paths import path_obj

class UpdateItem(MenuItem):

    def __init__(self):
        super().__init__()

    def update_item(self):
        try:
            self.foodmenu_list = operation_obj.read_file(path_obj.foodmenu_path)
            display_menu_obj.formatted_menu()
            food_id = input("Enter food id to update price : ")
            id_matched = 0

            for item in self.foodmenu_list:
                if item["food_id"] == food_id:
                    id_matched = 1
                    food_type = item["food_type"]
                    if food_type in self.categories_with_size:
                        for s in self.serve_size:
                            new_price = int(input(f"Update price for {s} size: "))
                            item[f"{s}_food_price"] = new_price

                    elif food_type in self.categories_without_size:
                        new_price = int(input("Update price : "))
                        item["nosize_food_price"] = new_price

                    operation_obj.write_file(data=self.foodmenu_list,path=path_obj.foodmenu_path)
                    print(f"\n{food_id} Id price updated")
                    break

            if id_matched == 0:
                print(print_obj.noid_msg)

        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a",isJson=0)

updateitem_obj = UpdateItem()