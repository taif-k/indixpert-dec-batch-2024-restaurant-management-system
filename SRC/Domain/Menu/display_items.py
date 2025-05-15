from .add_items import MenuItem
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj
foodmenu_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\foodmenu.json"

class MenuDisplay(MenuItem):
    def __init__(self, foodmenu_path):
        super().__init__(foodmenu_path)

    def formatted_menu(self):
        try:
            self.foodmenu_list = operation_obj.read_file(foodmenu_path)
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
                    print(f"\n                {food_type.upper()}")
                    print(f"{'Food ID':<10}{'Name':<20}{'Serving':<10}{'Price(Rs)':<6}")
                    print("----------------------------------------------------------")
                    for food in separate_menu[food_type]:
                        if food_type in ("breakfast", "lunch", "dinner"):
                            print(f"{food['food_id']:<10}{food['food_item']:<20}{'small':<10}{food['small_food_price']:<6}")
                            print(f"{'':<10}{'':<20}{'medium':<10}{food['medium_food_price']:<6}")
                            print(f"{'':<10}{'':<20}{'large':<10}{food['large_food_price']:<6}")
                        elif food_type == "beverages":
                            print(f"{food['food_id']:<10}{food['food_item']:<20}{'NA':<10}{food['nosize_food_price']:<6}")
                    print()
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)


display_menu_obj = MenuDisplay(foodmenu_path)