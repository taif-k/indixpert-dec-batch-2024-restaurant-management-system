from SRC.Domain.Order.place_order import PlaceOrder
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Payment import pay_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj

class CancelOrder(PlaceOrder):

    def __init__(self):
        super().__init__()

    def orders_taken(self):
        try:
            self.placedorder_list = operation_obj.read_file(path=path_obj.placedorder_path)    
            print(f"\n{'ORDER ID':<15}{'CUSTOMER NAME':<20}{'ITEM':<15}{'QTY':<15}{'AMOUNT':<15}")
            for order in self.placedorder_list:
                print("-" * 75)
                print(f"{order['order_id']:<15}{order['customer_name']:<20}{" -":<15}")
                for order_detail in order["order_placed"]:
                    item_total = order_detail['item_quantity'] * order_detail['item_price']
                    print(f"{'':<20}{'':<15}{order_detail['search_fooditem']:<15}{order_detail['item_quantity']:<15}{item_total:<15}")
                    print()

        except Exception as err:
            print(print_obj.invalid_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")
    
    # when order is cancelled by admin, seats are reset
    def order_cancel(self):
        try:
            self.bill_list = operation_obj.read_file(path_obj.bill_path)
            self.placedorder_list = operation_obj.read_file(path=path_obj.placedorder_path)   
            self.orders_taken()
            paid_bills_id = {bill["order_id"] for bill in self.bill_list} # bills generated after payment

            order_id = input("Enter order id to cancel: ")

            order_to_cancel = None 
            id_available = 0
            for order in self.placedorder_list: # orders before payment
                if order["order_id"] == order_id:
                    id_available = 1
                    order_to_cancel = order
                    break

            if id_available == 0:
                print(print_obj.noid_msg)    
                    
            if order_to_cancel and id_available == 1:
                if order["order_id"] in paid_bills_id:
                    print("\nPaid orders cannot be cancelled")
                else:
                    self.placedorder_list.remove(order_to_cancel)
                    operation_obj.write_file(data=self.placedorder_list,path=path_obj.placedorder_path) 
                    pay_obj.order_id = order_id
                    pay_obj.seat_deallocate()
                    print(print_obj.cancelled_msg)
        except Exception as err:
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

cancel_obj = CancelOrder()


        
            
                
