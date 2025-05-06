from SRC.Domain import operation_obj,Foodvalid_obj
foodmenu_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\foodmenu.json"

class MenuItem:
    def __init__(self,foodmenu_path):
        self.food_path = foodmenu_path
        self.foodmenu_list = operation_obj.read_file(self.food_path)

    def add_menu(self):
        while True:
            foodmenu_dict = {}
            foodmenu_dict["food_item"] = input("Enter Food item to add: ").lower()
            foodmenu_dict["food_type"] = input("Enter Food category: ").lower()
            foodmenu_dict["food_id"] = foodmenu_dict["food_type"][0] +"_"+ Foodvalid_obj.id_unique() #ex: b_12
            for s in range(0,3):
                size = ["small","medium","large"]

                foodmenu_dict[f"{size[s]}_food_size"] = input(f"is serving size {size[s]}/NA: ").lower()
                foodmenu_dict[f"{size[s]}_food_price"] = int(input("Enter item price: "))

            add_item = input("Enter more items: y/n").lower()
            if add_item != "y":
                break

        self.foodmenu_list.append(foodmenu_dict)        
        operation_obj.write_file(data=self.foodmenu_list,path=self.food_path)
        print("\nFood item added to Menu")


foodmenu_obj = MenuItem(foodmenu_path)
