from .add_items import MenuItem
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj
foodmenu_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\foodmenu.json"

class UpdateItem(MenuItem):
    def __init__(self, foodmenu_path):
        super().__init__(foodmenu_path)

    def update_item(self):
        try:
            food_id = input("Enter food id to update content: ")
            id_matched = 0
            
            for item in self.foodmenu_list:
                if item["food_id"] == food_id:
                    id_matched = 1
                    for s in self.serve_size:
                        item[f"{s}_food_price"] = int(input(f"Update {s} price: "))
                        
                    operation_obj.write_file(data=self.foodmenu_list,path=self.food_path)
                    break

            if id_matched == 0:
                print(print_obj.noid_msg)

        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

updateitem_obj = UpdateItem(foodmenu_path)