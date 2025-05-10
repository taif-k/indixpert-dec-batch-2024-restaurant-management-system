from .add_items import MenuItem
foodmenu_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\foodmenu.json"

class MenuDisplay(MenuItem):
    def __init__(self, foodmenu_path):
        super().__init__(foodmenu_path)

    def formatted_menu(self):
        separate_menu = {"breakfast": [], "lunch": [], "dinner": []}

        for item in self.foodmenu_list:
            if item["food_type"] == "breakfast":
                separate_menu["breakfast"].append(item)
            elif item["food_type"] == "lunch":
                separate_menu["lunch"].append(item)
            elif item["food_type"] == "dinner":
                separate_menu["dinner"].append(item)

        for food_type in ["breakfast", "lunch", "dinner"]:
            if separate_menu[food_type]:
                print(f"\n                {food_type.upper()}")
                print(f"{"Food ID":<10}{"Name":<20}{"Serving":<10}{"Price(Rs)":<6}")
                print("----------------------------------------------------------")
                for food in separate_menu[food_type]:
                    print(f"{food["food_id"]:<10}{food["food_item"]:<20}{"small":<10}{food["small_food_price"]:<6}")
                    print(f"{"":<10}{"":<20}{'medium':<10}{food["medium_food_price"]:<6}")
                    print(f"{"":<10}{"":<20}{"large":<10}{food["large_food_price"]:<6}")
                    print()

display_menu_obj = MenuDisplay(foodmenu_path)