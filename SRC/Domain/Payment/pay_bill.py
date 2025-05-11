from SRC.Domain.Order import order_obj
from SRC.Domain.Validation import paymentid_obj
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Menu import foodmenu_obj
from SRC.Domain.Table.book_table import table_obj
from SRC.Domain.Bill.generate_bill import bill_obj

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment_type(self):
        pass

    def seat_deallocate(self,txn_no):
        try:
            id_matched = 0
            for id in order_obj.placedorder_list:
                if id["order_id"] == pay_obj.order_id:
                    id_matched = 1
                    for item in id["order_placed"]:
                        if "tableno_booked" in item and "seats_booked" in item:
                            table_no = item["tableno_booked"]
                            seats = item["seats_booked"]
                            break

            if id_matched == 1:
                for table in table_obj.tablelist:
                    if table["table_no"] == table_no and table["available_seats"] < 4:
                        table["available_seats"] = table["available_seats"] + seats
                        break

            operation_obj.write_file(data=table_obj.tablelist,path=table_obj.alltable_path)
            bill_obj.bill_generate(order_id=id["order_id"],txn_no=txn_no)
        except Exception as err:
            print("Resolving issue...Try again :)")
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
    
class Upi(Payment):
    def payment_type(self):
        try:
            self.__pin = input("Enter upi pin: ")
            if (len(self.__pin) == 4 or len(self.__pin) == 6) and self.__pin.isdigit():
                self.transaction_id = paymentid_obj.id_unique()
                print(f"\nBill paid Transaction id is {self.transaction_id}")
                self.seat_deallocate(txn_no = self.transaction_id)
            else:
                print("\nInvalid pin/option")
        except Exception as err:
            print(foodmenu_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
Upi_obj = Upi()

class Cash(Payment):
    def payment_type(self):
        try:
            cash_amount = int(input("Enter cash amount: "))
            valid_amount = 0
            for amount in order_obj.bill_list:
                if cash_amount >= amount["total"]:
                    valid_amount = 1
                    break

            if valid_amount == 1:
                return_cash = cash_amount - amount["total"]
                print("Bill paid :)")
                print(f"Amount returned {return_cash}")
                self.seat_deallocate(txn_no="cash")
            else:
                print("Paying Amount should be Non-Negative/Greater than bill amount")
        except Exception as err:
            print(foodmenu_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)  
cash_obj = Cash()

class Card(Payment):
    def payment_type(self):
        try:
            swipe_card = int(input("Enter 1 to Swipe Card: "))
            self.__card_num = paymentid_obj.id_unique()
            if swipe_card == 1 and len(self.__card_num) == 16:
                print("Bill paid :)")
                self.seat_deallocate(txn_no = self.__card_num)
            else:
                print("Card Declined")
        except Exception as err:
            print(foodmenu_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
card_obj = Card()

class PaymentSelect(Upi,Cash,Card):

    def payment_menu(self):
        print()
        print("1 - Cash")
        print("2 - Upi")
        print("3 - Card")

    def payment_option(self):
        try:
            self.order_id = input("\nEnter order id: ")
            orderid_matched = 0
            for id in order_obj.placedorder_list:
                if id["order_id"] == self.order_id:
                    orderid_matched = 1
                    gst = 0.10
                    self.billamount= id["total_price"] + (id["total_price"] * gst)
                    break

            if orderid_matched == 1:
                print(f"Bill amount for above order id: {self.billamount}")
                self.payment_menu()
                pay_bill = int(input("Enter payment option: "))
                if pay_bill == 1:
                    cash_obj.payment_type()
                elif pay_bill == 2:
                    Upi_obj.payment_type()
                elif pay_bill == 3:
                    card_obj.payment_type()
                else:
                    print("Invalid payment option")    
            else:
                print("Order id not found")
        except Exception as err:
            print(foodmenu_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

pay_obj = PaymentSelect()