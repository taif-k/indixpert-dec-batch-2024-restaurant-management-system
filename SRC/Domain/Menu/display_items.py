from .add_items import MenuItem
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj

class MenuDisplay(MenuItem):
  
    def __init__(self):
        super().__init__()

    def formatted_menu(self):
        try:
            self.foodmenu_list = operation_obj.read_file(path_obj.foodmenu_path)
            separate_menu = {"breakfast": [], "lunch": [], "dinner": [], "beverages": []}

            for item in self.foodmenu_list:
                if item["food_type"] == "breakfast":
                    separate_menu["breakfast"].append(item)
                elif item["food_type"] == "lunch":
                    separate_menu["lunch"].append(item)
                elif item["food_type"] == "dinner":
                    separate_menu["dinner"].append(item)
                elif item["food_type"] == "beverages":
                    separate_menu["beverages"].append(item)

            for food_type in ["breakfast", "lunch", "dinner", "beverages"]:
                if separate_menu[food_type]:
                    print(f"\n\t\t\t{food_type.upper()}")
                    print(f"{"Food ID":<10}{"Name":<25}{"Serving":<15}{"Price(Rs)":<10}")
                    print("------------------------------------------------------------")
                    for food in separate_menu[food_type]:
                        if food_type in ("breakfast", "lunch", "dinner"):
                            print(f"{food["food_id"]:<10}{food["food_item"]:<25}{"small":<15}{food["small_food_price"]:<10}")
                            print(f"{"":<35}{"medium":<15}{food["medium_food_price"]:<10}")
                            print(f"{"":<35}{"large":<15}{food["large_food_price"]:<10}")
                            print()
                        elif food_type == "beverages":
                            print(f"{food["food_id"]:<10}{food["food_item"]:<25}{"NA":<15}{food["nosize_food_price"]:<10}")
                    print()

        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a",isJson=0)


display_menu_obj = MenuDisplay()
