from SRC.Domain import order_obj,validation_obj

class Bill:
    def __init__(self):
        pass

    def cash_pay(self):
        cash_amount = int(input("Enter cash amount: "))
        valid_amount = 0
        for amount in order_obj.bill_list:
            if cash_amount >= amount["total_amount"]:
                valid_amount = 1
                break

        if valid_amount == 1:
            return_cash = cash_amount - amount["total_amount"]
            print("Bill paid :)")
            print(f"Amount returned {return_cash}")

        if valid_amount == 0:
            print("Paying Amount should be Non-Negative/Greater than bill amount")    
    
    def card_pay(self):
        swipe_card = int(input("Enter 1 to Swipe Card: "))
        self.__card_num = validation_obj.user_id(id_length=16)
        if swipe_card == 1 and len(self.__card_num) == 16:
            print("Bill paid")
        else:
            print("Card Declined")

    def upi_menu(self):
        print("1 - paytm")
        print("2- phonepe")
        print("3- gpay")

    def upi_pay(self):
        self.upi_menu()
        upi_option = int(input("Enter upi option: "))
        self.__pin = input("Enter upi pin: ")
        if upi_option in [1,2,3] and len(self.__pin) == 4 and self.__pin.isdigit():
            print(f"\nBill paid Transaction id is {validation_obj.user_id(id_length=16)}")
        else:
            print("\nIncorrect pin/Invalid option")
            

    def payment_menu(self):
        print()
        print("1 - Cash")
        print("2 - Upi")
        print("3 - Card")

    def payment_option(self):
        order_id = input("\nEnter order id: ")
        orderid_matched = 0
        for id in order_obj.bill_list:
            if id["order_id"] == order_id:
                orderid_matched = 1
                self.billamount= id["total_amount"]
                break

        if orderid_matched == 1:
            print(f"Bill amount for above order id: {self.billamount}")
            self.payment_menu()
            pay_bill = int(input("Enter payment option: "))
            if pay_bill == 1:
                self.cash_pay()
            elif pay_bill == 2:
                self.upi_pay()
            elif pay_bill == 3:
                self.card_pay()
            else:
                print("Invalid payment option")    
        else:
            print("Order id not found")
                
bill_obj = Bill()