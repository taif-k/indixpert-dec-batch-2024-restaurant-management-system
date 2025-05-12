from SRC.Domain.ReadFile import operation_obj

error_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Log\error_log.txt"
placedorder_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\orderplaced.json"
bill_path = r"D:\Repositories\indixpert-dec-batch-2024-restaurant-management-system\SRC\Database\order_bill.json"

class Bill:
    def __init__(self,err_path,ordered_path,bill_path):
        self.err_path = err_path
        self.ordered_path = ordered_path
        self.bill_path = bill_path
        self.bill_list = operation_obj.read_file(self.bill_path)

    def bill_generate(self,order_id = None,txn_no = None):
        try:
            if txn_no == None:
                txn_no = "cash"

            self.placedorder_list = operation_obj.read_file(self.ordered_path)
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
                        "status":"paid"
                        }
                    self.bill_list.append(billdict)
                    break

            operation_obj.write_file(data=self.bill_list,path=self.bill_path)
        except Exception as err:
            print("Resolving issue..Try again after some time")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0) 

bill_obj = Bill(error_path,placedorder_path,bill_path)   