from SRC.Domain import operation_obj,Foodvalid_obj
foodmenu_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\foodmenu.json"

class MenuItem:
    def __init__(self,foodmenu_path):
        self.food_path = foodmenu_path
        self.foodmenu_list = operation_obj.read_file(self.food_path)
        self.err_msg = "Resolving issue...Try again after some time"

    def add_menu(self):
        try:
            serve_size = ("small","medium","large")
            while True:
                foodmenu_dict = {}
                foodmenu_dict["food_item"] = input("Enter Food item to add: ").lower()
                foodmenu_dict["food_type"] = input("Enter Food category: ").lower()
                foodmenu_dict["food_id"] = foodmenu_dict["food_type"][0] +"_"+ Foodvalid_obj.id_unique() #ex: b_12
                already_present = 0
                for item in self.foodmenu_list:
                    if item["food_item"] == foodmenu_dict["food_item"] and item["food_type"] == foodmenu_dict["food_type"]:
                        already_present = 1
                        print("Food item already present in specific category")
                        break

                if already_present == 0:
                    for s in range(0,3):
                        foodmenu_dict[f"{serve_size[s]}_food_size"] = input(f"is serving size {serve_size[s]}/NA: ").lower()
                        foodmenu_dict[f"{serve_size[s]}_food_price"] = int(input("Enter item price: "))
                    self.foodmenu_list.append(foodmenu_dict)
                    print("\nFood item added to Menu")

                add_item = input("Enter more items: y/n").lower()
                if add_item != "y":
                    break
                
            operation_obj.write_file(data=self.foodmenu_list,path=self.food_path)
        except Exception as err:
            print(self.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
        
foodmenu_obj = MenuItem(foodmenu_path)
