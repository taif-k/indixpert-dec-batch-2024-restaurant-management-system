from SRC.Domain import operation_obj,validation_obj
foodmenu_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\foodmenu.json"

class MenuItem:
    def __init__(self,foodmenu_path):
        self.food_path = foodmenu_path
        self.foodmenu_list = operation_obj.read_file(self.food_path)

    def add_menu(self):
        foodmenu_dict = {}
        while True:
            foodmenu_dict["food_item"] = input("Enter Food item to add: ")
            foodmenu_dict["food_type"] = input("Enter Food category: ")
            foodmenu_dict["food_id"] = foodmenu_dict["food_type"] +"_"+ validation_obj.user_id() #ex: lunch_c123
            for s in range(0,3):
                size = ["small","medium","large"]

                foodmenu_dict[f"{size[s]}_food_size"] = input(f"is serving size {size[s]}/NA: ")
                foodmenu_dict[f"{size[s]}_food_price"] = int(input("Enter item price: "))

            add_item = input("Enter more items: y/n")
            if add_item != "y":
                break

        self.foodmenu_list.append(foodmenu_dict)        
        operation_obj.write_file(self.foodmenu_list,self.food_path)


foodmenu_obj = MenuItem(foodmenu_path)
