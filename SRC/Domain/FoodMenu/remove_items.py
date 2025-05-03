from SRC.Domain import foodmenu_obj,operation_obj

class RemoveFood:
    def remove_menu(self):
        while True:
            food_id = input("Enter food item id to remove from menu: ")
            for item in foodmenu_obj.foodmenu_list:
                if item["food_id"] == food_id:
                    foodmenu_obj.foodmenu_list.remove(item)
                    break

            remove_item = input("Remove more items: ")
            if remove_item != "y":
                break

        operation_obj.write_file(data=foodmenu_obj.foodmenu_list,path=foodmenu_obj.food_path)

removemenu_obj = RemoveFood()