from SRC.Domain import foodmenu_obj,operation_obj,validation_obj
import json

error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"
placedorder_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\orderplaced.json"

class PlaceOrder:
    def __init__(self,err_path,ordered_path):
        self.err_path = err_path
        self.ordered_path = ordered_path
        self.placedorder_list =  operation_obj.read_file(self.ordered_path)

    def multiple_orders(self):
        self.orderlist = []
        while True:
            orderdict = {}
            orderdict["search_foodtype"] = input("Search Breakfast/Lunch/Dinner: ")
            orderdict["search_fooditem"] = input("Search Food item: ")
            orderdict["search_servesize"] = input("Search small/medium/large: ")
            orderdict["order_id"] = validation_obj.user_id()
            orderdict["Customer_Name"] = input("Enter Customer name: ")

            food_available = 0
            for item in foodmenu_obj.foodmenu_list:
                if item["food_type"] == orderdict["search_foodtype"]  and item["food_item"] == orderdict["search_fooditem"]:
                    if orderdict["search_servesize"] in (item["small_food_size"],item["medium_food_size"],item["large_food_size"]):
                        food_available = 1
                        break

            if food_available == 1:
                self.orderlist.append(orderdict)
            else:
                print("Food Category/Item Not available...Search anything else")
              
            return self.orderlist
                
    def book_order(self):
        while True:
            orderplaceddict = {}        
            orderplaceddict["item_booked"] = self.multiple_orders()
            orderplaceddict["item_quantity"] = int(input("Enter Food item quantity: "))
            orderplaceddict["total_price"] = 100 * orderplaceddict["item_quantity"]
            orderplaceddict["order_time"] = operation_obj.get_errdetails(get_date=True)
            print(f"Order placed Sucessfully :)....Order id: {validation_obj.user_id()}")
            self.placedorder_list.append(orderplaceddict)

            add_moreitem = input("Add Items: y/n")
            if add_moreitem != "y":
                break  

        operation_obj.write_file(data=self.placedorder_list,path=self.ordered_path)
        
        
order_obj = PlaceOrder(error_path,placedorder_path)

    