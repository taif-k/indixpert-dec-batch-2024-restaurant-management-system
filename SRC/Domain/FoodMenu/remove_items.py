from SRC.Domain import foodmenu_obj,operation_obj

class RemoveFood:
    def remove_menu(self):
        try:
            while True:
                food_id = input("Enter food item id to remove from menu: ")
                id_matched = 0
                for item in foodmenu_obj.foodmenu_list:
                    if item["food_id"] == food_id:
                        foodmenu_obj.foodmenu_list.remove(item)
                        id_matched = 1
                        break
                if id_matched == 0:
                    print("\nOrder id not found")

                remove_item = input("Remove item y/n: ")
                if remove_item != "y":
                    break

            operation_obj.write_file(data=foodmenu_obj.foodmenu_list,path=foodmenu_obj.food_path)
        except Exception as err:
            print(foodmenu_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

removemenu_obj = RemoveFood()