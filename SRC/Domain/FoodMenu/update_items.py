from SRC.Domain import foodmenu_obj,operation_obj

class UpdateItem:
    def update_item(self):
        try:
            food_id = input("Enter food id to update content: ")
            id_matched = 0
            
            for item in foodmenu_obj.foodmenu_list:
                if item["food_id"] == food_id:
                    id_matched = 1
                    for s in foodmenu_obj.serve_size:
                        item[f"{s}_food_price"] = int(input(f"Update {s} price: "))
                        
                    operation_obj.write_file(data=foodmenu_obj.foodmenu_list,path=foodmenu_obj.food_path)
                    break

            if id_matched == 0:
                print("Food item not found ")

        except Exception as err:
            print(foodmenu_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

updateitem_obj = UpdateItem()