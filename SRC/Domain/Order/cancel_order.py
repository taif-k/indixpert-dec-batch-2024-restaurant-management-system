from .place_order import PlaceOrder
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Payment import pay_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj
import json

class CancelOrder(PlaceOrder):

    def __init__(self):
        super().__init__()

    def orders_taken(self):
        try:
            self.placedorder_list = operation_obj.read_file(path=path_obj.placedorder_path)    
            for order in self.placedorder_list:
                for order_detail in order["order_placed"]:
                    print("ORDER ID      CUSTOMER NAME      ITEM      QTY      AMOUNT")
                    print("----------------------------------------------------------")
                    print(f"{order['order_id']}\t\t{order['customer_name']}\t\t{order_detail['search_fooditem']}\t\t{order_detail['item_quantity']}\t\t{order_detail['tableno_booked']}")
                    print()

        except Exception as err:
            print(print_obj.invalid_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a",isJson=0)

            
    # when order is cancelled by admin, seats are reset
    def order_cancel(self):
        try:
            self.placedorder_list = operation_obj.read_file(path=path_obj.placedorder_path)   
            self.orders_taken() 
            order_id = input("Enter order id to cancel: ")
            id_matched = 0 
            for order in self.placedorder_list:
                if order["order_id"] == order_id:
                    id_matched = 1
                    break

            if id_matched == 1:
                self.placedorder_list.remove(order)
                operation_obj.write_file(data=self.placedorder_list,path=path_obj.placedorder_path) 

                pay_obj.order_id = order_id
                pay_obj.seat_deallocate()
                print(print_obj.cancelled_msg)
            else:
                print(print_obj.noid_msg)
        except Exception as err:
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a",isJson=0)


cancel_obj = CancelOrder()


        
            
                
