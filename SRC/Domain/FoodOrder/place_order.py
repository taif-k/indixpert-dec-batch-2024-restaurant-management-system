from SRC.Domain import foodmenu_obj,operation_obj,validation_obj,table_obj
import json
error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"
placedorder_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\orderplaced.json"
bill_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\order_bill.json"

class PlaceOrder:
    def __init__(self,err_path,ordered_path,bill_path):
        self.err_path = err_path
        self.ordered_path = ordered_path
        self.bill_path = bill_path
        self.placedorder_list =  operation_obj.read_file(self.ordered_path)
        self.bill_list = operation_obj.read_file(self.bill_path)

    def orders_list(self):
        self.orderlist = []
        self.total_price = 0
        while True:
            self.orderdict = {}
            self.orderdict["search_foodtype"] = input("Search Breakfast/Lunch/Dinner: ").lower()
            self.orderdict["search_fooditem"] = input("Search Food item: ").lower()
            self.orderdict["search_servesize"] = input("Search small/medium/large: ").lower()
            self.orderdict["item_quantity"] = int(input("Enter Food item quantity: "))
            
            food_available = 0
            for item in foodmenu_obj.foodmenu_list:
                if item["food_type"] == self.orderdict["search_foodtype"]  and item["food_item"] == self.orderdict["search_fooditem"]:
                    if self.orderdict["search_servesize"] in (item["small_food_size"],item["medium_food_size"],item["large_food_size"]):
                        food_available = 1
                        self.orderdict["item_price"] = item[f"{self.orderdict["search_servesize"]}_food_price"]
                        self.total_price += self.orderdict["item_price"] * self.orderdict["item_quantity"]
                        break

            if food_available == 1:
                self.orderlist.append(self.orderdict)
            else:
                print("Food Category/Item Not available...Search anything else")

            add_moreitem = input("Add Items: y/n")
            if add_moreitem != "y":
                break 

        return self.orderlist

    def bill_generate(self,order_id = None):
        for order in self.placedorder_list:
            if str(order["order_id"]) == str(f"{order_id}"):
                gst = 0.10
                billdict = {
                    "total_amount":order["total_price"]+(order["total_price"] * gst),
                    "customer_name":order["customer_name"],
                    "order_time": order["order_time"],
                    "order_id":order["order_id"],
                    }
                self.bill_list.append(billdict)
                break

        operation_obj.write_file(data=self.bill_list,path=self.bill_path)
                
    def select_table(self):
        table_available = 0
        while table_available != 1:
            print(f"Available seats: {json.dumps(table_obj.tablelist,indent=3)}")
            table_select = int(input("Enter table no. to book: ")) 
            seat_select = int(input("Enter no. of seats to book: "))
            
            for table in table_obj.tablelist:
                if table["table_no"] == table_select and seat_select <= table["available_seats"]:
                    table_available = 1
                    break   
            if table_available == 0:
                print("Choose Available Seats/Table")

            if table_available == 1:
                updated_seats = table["available_seats"]-seat_select
                updatetable = {"table_no":table_select,"available_seats":updated_seats}
                table_obj.tablelist.remove(table)
                table_obj.tablelist.append(updatetable)
                operation_obj.write_file(data=table_obj.tablelist,path=table_obj.alltable_path)
                print("Booking confirmed")  

    def book_order(self):
        table_book = input("Book Table first to place order: y/n: ").lower()
        if table_book == "y":
            orderplaceddict = {}
            self.select_table()
            orderplaceddict["customer_name"] = validation_obj.user_name()     
            orderplaceddict["order_placed"] = self.orders_list()
            orderplaceddict["order_id"] = validation_obj.id_unique()
            orderplaceddict["total_price"] = self.total_price
            orderplaceddict["order_time"] = operation_obj.get_errdetails(get_date=True)

            print(f"Order placed Sucessfully :)....Order id: {orderplaceddict["order_id"]}")
            self.placedorder_list.append(orderplaceddict)

            operation_obj.write_file(data=self.placedorder_list,path=self.ordered_path)
            self.bill_generate(order_id=orderplaceddict["order_id"])
        else:
            print("Cannot place order :(")
        
order_obj = PlaceOrder(error_path,placedorder_path,bill_path)


    