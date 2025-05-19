from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation import print_obj
from SRC.Domain.Path.all_paths import path_obj

class Bill:

    def __init__(self):
        self.bill_list = operation_obj.read_file(path_obj.bill_path)

    def bill_generate(self,order_id = None,txn_no = None, mode = None):
        try:
            if txn_no == None:
                txn_no = "cash"

            self.placedorder_list = operation_obj.read_file(path_obj.placedorder_path)
            for order in self.placedorder_list:
                if order["order_id"] == order_id:
                    gst = 0.10
                    billdict = {
                        "customer_name":order["customer_name"],
                        "order_id":order["order_id"],
                        "food_amount":order["total_price"],
                        "gst":f"{gst * 100}%",
                        "total":order["total_price"]+(order["total_price"] * gst),
                        "order_time": order["order_time"],
                        "card/transaction_no": txn_no,
                        "mode":mode
                        }
                    self.bill_list.append(billdict)
                    break

            operation_obj.write_file(data=self.bill_list,path=path_obj.bill_path)
        except Exception as err:
            print(print_obj.invalid_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a",isJson=0) 

bill_obj = Bill()