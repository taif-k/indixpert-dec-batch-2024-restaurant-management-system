from SRC.Domain.Menu import foodmenu_obj,display_menu_obj
from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Validation import validation_obj,print_obj
from SRC.Domain.Table import display_table_obj,table_obj
from datetime import datetime,timedelta
from SRC.Domain.Path.all_paths import path_obj

class PlaceOrder:
    def __init__(self):
        self.placedorder_list =  file_operation_obj.read_file(path_obj.placedorder_path)
        self.bill_list = file_operation_obj.read_file(path_obj.bill_path)

    # stores details of customer along with orders
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
                    orderplaceddict["order_time"] = self.start_datetime
                    
                    print(f"Order placed Sucessfully :)....Order id: {orderplaceddict["order_id"]}")
                    self.placedorder_list.append(orderplaceddict)
                    file_operation_obj.write_file(data=self.placedorder_list,path=path_obj.placedorder_path)
                else:
                    print(":(")
                    
            else:
                print(print_obj.no_order_msg)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

    def slot_range(self):
        print()
        print("1 - 11:00 AM - 1:00 PM")
        print("2 - 1:15 PM - 3:15 PM")
        print("3 - 5:00 PM - 7:00 PM")
        print("4 - 8:00 PM - 10:00 PM")

    # user can book  4 slots using option 1,2...
    def select_table(self):
        try:
            table_available = 0
            while table_available != 1:
                today = datetime.today().strftime("%Y-%m-%d")
                one_month_date = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
                display_table_obj.available_tables()

                self.table_select = int(input("Enter table number to book: "))
                self.seat_select = int(input("Enter number of seats to book: "))
                input_booking_date = input(f"Enter booking date (y-m-d)").strip()
                
                if (input_booking_date < today) or (input_booking_date > one_month_date):
                    print(f"Booking date must be between {today} and {one_month_date}")
                    continue

                self.booking_date = input_booking_date
                self.slot_range()
                
                slot_option = int(input("Enter slot no : "))
                
                slot_time = {}
                slot_time[1] = ("slot1", "11:00", "13:00")
                slot_time[2] = ("slot2", "13:15", "15:15")
                slot_time[3] = ("slot3", "17:00", "19:00")
                slot_time[4] = ("slot4", "20:00", "22:00")


                if slot_option in slot_time:
                    selected_slot = slot_time[slot_option]
                    
                    self.slot_selected = selected_slot[0]
                    start_time = selected_slot[1]
                    end_time = selected_slot[2]
                else:
                    print(print_obj.invalid_msg)
                    continue

                for table in table_obj.tablelist:
                    if table["table_no"] == self.table_select and self.seat_select <= table[self.slot_selected]:
                        table_available = 1
                        break

                if table_available != 1:
                    print(print_obj.choose_validtable)
                else:
                    start_dt_str = f"{self.booking_date} {start_time}:00"
                    end_dt_str = f"{self.booking_date} {end_time}:00"

                    self.start_datetime = datetime.strptime(start_dt_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    self.end_datetime = datetime.strptime(end_dt_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

                    updated_seats = table[self.slot_selected] - self.seat_select
                    table[self.slot_selected] = updated_seats

                    file_operation_obj.write_file(data=table_obj.tablelist, path=path_obj.alltable_path)
                    print(print_obj.book_confirm_msg)

        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err), path=path_obj.error_path, mode="a")

    # searched item is displayed 
    def display_item(self, searched_item):
        print("---------------------------------------------------")
        print(f"{'ID':<10}{'ITEM':<20}{'SERVING':<15}\t{'PRICE':<10}")
        print("---------------------------------------------------")

        if "nosize_food_price" in searched_item:
            print(f"{searched_item['food_id']:<10}{searched_item['food_item']:<20}{"-":<15}\t{searched_item["nosize_food_price"]:<10}")
        else:
            print(f"{searched_item["food_id"]:<10}{searched_item["food_item"]:<20}{"1-Small":<15}\t{searched_item["small_food_price"]:<10}")
            print(f"{'':<10}{'':<20}{"2-Medium":<15}\t{searched_item["medium_food_price"]:<10}")
            print(f"{'':<10}{'':<20}{"3-Large":<15}\t{searched_item["large_food_price"]:<10}")

        print("-------------------------------------")

    # "order_placed" key in order placed.json
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
                    self.orderdict["slot_booked"] = self.slot_selected

                    self.orderdict["start_datetime"] = self.start_datetime
                    self.orderdict["end_datetime"] = self.end_datetime

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
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")            
                        
order_obj = PlaceOrder()


    
