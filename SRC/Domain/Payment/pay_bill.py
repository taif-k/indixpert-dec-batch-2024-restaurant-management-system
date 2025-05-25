from SRC.Domain.Order import order_obj 
from SRC.Domain.Validation import paymentid_obj,print_obj
from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Table.table_add import table_obj
from SRC.Domain.Bill.generate_bill import bill_obj
from SRC.Domain.Path.all_paths import path_obj
import datetime

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment_type(self):
        pass

    # seats are reset if staff does payment or admin cancels the order
    def seat_deallocate(self,txn_no=None,mode = None):
        try:
            id_matched = 0
            for id in order_obj.placedorder_list:
                if id["order_id"] == pay_obj.order_id:
                    id_matched = 1
                    for item in id["order_placed"]:
                        if all(key in item for key in ["tableno_booked", "seats_booked", "slot_booked"]):
                            table_no = item["tableno_booked"]
                            slot_booked = item["slot_booked"]
                            seats = item["seats_booked"]
                            break
                    break    

            if id_matched == 1 and table_no is not None and slot_booked is not None:
                for table in table_obj.tablelist:
                    if table["table_no"] == table_no and table[slot_booked] < 4:
                        table[slot_booked] += seats
                        break

            file_operation_obj.write_file(data=table_obj.tablelist,path=path_obj.alltable_path)
            if txn_no != None:
                bill_obj.bill_generate(order_id=id["order_id"],txn_no=txn_no,mode= mode)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")
    
class Upi(Payment):
    def payment_type(self):
        try:
            self.__pin = input("Enter 4/6 digits upi pin: ")
            if (len(self.__pin) == 4 or len(self.__pin) == 6) and self.__pin.isdigit():
                self.transaction_id = paymentid_obj.id_unique()
                print(f"\nBill paid Transaction id is {self.transaction_id}")
                self.seat_deallocate(txn_no = self.transaction_id, mode = "upi")
            else:
                print(print_obj.invalid_msg)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")
Upi_obj = Upi()

class Cash(Payment):
    def payment_type(self,cash_amount):
        try:
            return_cash = cash_amount - pay_obj.total
            print(print_obj.billpaid)
            print(f"{print_obj.amountreturned}: {return_cash}")
            self.seat_deallocate(txn_no="cash",mode = "cash")
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")  
cash_obj = Cash()

class Card(Payment):
    def payment_type(self):
        try:
            swipe_card = int(input("Enter 1 to Swipe Card: "))
            self.__card_num = paymentid_obj.id_unique()
            if swipe_card == 1 and len(self.__card_num) == 16:
                print(print_obj.billpaid)
                self.seat_deallocate(txn_no = self.__card_num, mode = "card")
            else:
                print(print_obj.card_declined)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")
card_obj = Card()

class PaymentSelect(Card):

    def payment_menu(self):
        print()
        print("1 - Cash")
        print("2 - Upi")
        print("3 - Card")

    def bill_display(self,bill):
        try:
            gst = 0.10
            subtotal = bill["total_price"]
            gst_amount = subtotal * gst
            self.total = subtotal + gst_amount

            print("\n--------------------------------------------")
            print(f"Order ID      : {bill['order_id']}")
            print(f"Customer Name : {bill['customer_name']}")
            print(f"Order Time    : {bill['order_time']}")
            print("--------------------------------------------")
            print(f"{"Item"}    {"Qty"}    {"Price"}    {"Amount"}")
            print("--------------------------------------------")

            for order in bill["order_placed"]:
                item = order["search_fooditem"]
                qty = order["item_quantity"]
                price = order["item_price"]
                amount = qty * price
                print(f"{item}     {qty}      {price}       {amount}")

            print("\n--------------------------------------------")
            print(f"{print_obj.subtotal}           Rs. {subtotal}")
            print(f"{"GST (10%)"}          Rs. {gst_amount}")
            print(f"{print_obj.totalbill}         Rs. {self.total}")
        except Exception as err:
            print(print_obj.invalid_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

    def payment_option(self):
        try:
            today_str = datetime.datetime.now().strftime("%Y-%m-%d")
            order_obj.bill_list = file_operation_obj.read_file(path=path_obj.bill_path)

            print("\nToday's Orders:")
            print("------------------------------------------------------------")
            print("Order ID      Customer Name      Order Time")
            print("------------------------------------------------------------")

            for order in order_obj.placedorder_list:
                if "order_time" in order and order["order_time"] is not None:
                    order_time = order["order_time"]
                    if len(order_time) >= 10:
                        order_date_part = order_time[:10]
                        if order_date_part == today_str:
                            print(f"{order['order_id']:<13} {order['customer_name']:<18} {order_time}")
            print("------------------------------------------------------------")

            self.order_id = input("\nEnter order id: ")
            orderid_matched = 0
            for id in order_obj.placedorder_list:
                if id["order_id"] == self.order_id:
                    orderid_matched = 1
                    individual_bill = id
                    break

            if orderid_matched == 1:
                self.bill_display(individual_bill) 
                cash_amount = int(input("\nEnter amount to pay: "))
                valid_amount = 0
                for amount in order_obj.placedorder_list:
                    if cash_amount >= pay_obj.total:
                        valid_amount = 1
                        break

                for bill in order_obj.bill_list:
                    if bill["order_id"] == self.order_id:
                        print(f"\nPayment for Order id {self.order_id} already done")
                        return None
                    
                if valid_amount == 1:
                    self.payment_menu()
                    pay_bill = int(input(print_obj.enter_option))

                    if pay_bill == 1:
                        cash_obj.payment_type(cash_amount)
                    elif pay_bill == 2:
                        Upi_obj.payment_type()
                    elif pay_bill == 3:
                        card_obj.payment_type()
                    else:
                        print(print_obj.invalid_msg) 
                else:
                    print(print_obj.invalidamount_msg)   
            else:
                print(print_obj.noid_msg)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

pay_obj = PaymentSelect()
