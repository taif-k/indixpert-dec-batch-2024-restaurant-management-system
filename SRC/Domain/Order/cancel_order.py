from .place_order import PlaceOrder
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Payment import pay_obj

error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"
placedorder_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\orderplaced.json"
bill_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\order_bill.json"

class CancelOrder(PlaceOrder):
    def __init__(self, err_path, ordered_path, bill_path):
        super().__init__(err_path, ordered_path, bill_path)

    def order_cancel(self):
        try:
            order_id = input("Enter order id to cancel: ")
            id_matched = 0 
            for order in self.placedorder_list:
                if order["order_id"] == order_id:
                    id_matched = 1
                    break

            if id_matched == 1:
                self.placedorder_list.remove(order)
                operation_obj.write_file(data=self.placedorder_list,path=self.ordered_path) 

                pay_obj.order_id = order_id
                pay_obj.seat_deallocate()
                print("\nOrder Cancelled")
            else:
                print("\nOrder not found")
        except Exception as err:
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=self.err_path,mode="a",isJson=0)


cancel_obj = CancelOrder(error_path,placedorder_path,bill_path)


        
            
                
                
    