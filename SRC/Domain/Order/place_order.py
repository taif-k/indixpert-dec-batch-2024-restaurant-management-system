from SRC.Domain.Menu import foodmenu_obj,display_menu_obj
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import validation_obj,print_obj
from SRC.Domain.Table import display_table_obj,table_obj

class PlaceOrder:
    placedorder_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\orderplaced.json"
    bill_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\order_bill.json"

    def __init__(self):
        self.placedorder_list =  operation_obj.read_file(self.placedorder_path)
        self.bill_list = operation_obj.read_file(self.bill_path)

    def book_order(self):
        try:
            table_book = input("Book Table to place order: y/n: ").lower()
            if table_book == "y":
                orderplaceddict = {}
                print()
                self.select_table()
                orderplaceddict["customer_name"] = validation_obj.user_name()     
                orderplaceddict["order_placed"] = self.orders_list()
                if orderplaceddict["order_placed"] != []:
                    orderplaceddict["order_id"] = validation_obj.id_unique()
                    orderplaceddict["total_price"] = self.total_price
                    orderplaceddict["order_time"] = operation_obj.get_errdetails(get_date=True)
                    
                    print(f"Order placed Sucessfully :)....Order id: {orderplaceddict["order_id"]}")
                    self.placedorder_list.append(orderplaceddict)
                    operation_obj.write_file(data=self.placedorder_list,path=self.placedorder_path)
                else:
                    print(":(")
                    
            else:
                print(print_obj.no_order_msg)
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.error_path,mode="a",isJson=0)

    def select_table(self):
        try:
            table_available = 0
            while table_available != 1:
                display_table_obj.available_tables()
                self.table_select = int(input("Enter table no. to book: ")) 
                self.seat_select = int(input("Enter no. of seats to book: "))                          
                
                for table in table_obj.tablelist:
                    if table["table_no"] == self.table_select and self.seat_select <= table["available_seats"]:
                        table_available = 1
                        break   
                if table_available == 0:
                    print(print_obj.choose_validtable)

                if table_available == 1:
                    updated_seats = table["available_seats"]-self.seat_select
                    updatetable = {"table_no":self.table_select,"available_seats":updated_seats}
                    table_obj.tablelist.remove(table)
                    table["available_seats"] = updated_seats
                    table_obj.tablelist.append(updatetable)
                    operation_obj.write_file(data=table_obj.tablelist,path=table_obj.alltable_path)
                    print(print_obj.book_confirm_msg)  
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.error_path,mode="a",isJson=0)

    def display_item(self, searched_item):
        print("-------------------------------------")
        print(f"{"ID"}\t\t{"ITEM"}\t\t{"SERVING"}\t\t{"PRICE"}")
        print("-------------------------------------")
        
        if "nosize_food_price" in searched_item:
            print(f"{searched_item["food_id"]}\t\t{searched_item["food_item"]}\t\t{'-'}\t\t{searched_item["nosize_food_price"]}\t\t")
        else:
            print(f"{searched_item["food_id"]}\t\t{searched_item["food_item"]}\t\t{"1-Small"}\t\t{searched_item["small_food_price"]}\t\t")
            print(f"{""}\t\t{""}\t\t{"2-Medium"}\t{searched_item["medium_food_price"]}")
            print(f"{""}\t\t{""}\t\t{"3-Large"}\t\t{searched_item["large_food_price"]}\t\t")
            print("-")

    def orders_list(self):
        try:
            self.orderlist = []
            self.total_price = 0
            while True:
                self.orderdict = {}
                display_menu_obj.formatted_menu()
                self.orderdict["search_fooditem"] = input("Search Food item: ").lower()
                
                food_available = 0
                for item in foodmenu_obj.foodmenu_list:
                    if item["food_item"] == self.orderdict["search_fooditem"]:
                            found_item = item
                            food_available = 1
                            break

                if food_available == 1:
                    self.display_item(found_item)

                    if "nosize_food_price" in found_item:
                        self.orderdict["item_quantity"] = int(input("Enter Food item quantity: "))
                        self.orderdict["item_price"] = found_item["nosize_food_price"]
                    else:
                        while True:
                            choose_serving = int(input("Choose Serving Size: "))      
                            if choose_serving == 1:
                                serve = "small"
                                break
                            elif choose_serving == 2:
                                serve = "medium"
                                break
                            elif choose_serving == 3:
                                serve = "large"
                                break
                            else:
                                print(print_obj.invalid_msg)
                        
                        self.orderdict["item_quantity"] = int(input("Enter Food item quantity: "))
                        self.orderdict["item_price"] = found_item[f"{serve}_food_price"]
                    
                    self.orderdict["tableno_booked"] = self.table_select
                    self.orderdict["seats_booked"] = self.seat_select
                    self.total_price += self.orderdict["item_price"] * self.orderdict["item_quantity"]
                    self.orderlist.append(self.orderdict)

                else:
                    print(print_obj.noitem_msg)

                add_moreitem = input("Add another Item: y/n ")
                if add_moreitem != "y":
                    break 
            return self.orderlist
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.error_path,mode="a",isJson=0)            
                        
order_obj = PlaceOrder()


    