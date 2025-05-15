from SRC.Domain.Bill.generate_bill import bill_obj
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation.print_variables import print_obj

class ReportData:
    def display_mode(self, modelist):

        print("------------------------------------------------------------------------")
        print("Order ID      Customer Name      Total Amount      Order Time")
        print("------------------------------------------------------------------------")

        total = 0
        for bill in modelist:
            print(f"{bill["order_id"]}\t\t{bill["customer_name"]}\t\t{bill["total"]}\t\t{bill["order_time"]}")
            total += bill["total"]

        print("------------------------------------------------------------------------")
        print(f"Transactions: {len(modelist)}")
        print(f"Total : Rs {total}")
    
    def report_type(self):
        print("1 - pay Mode")
        print("2 - Total Orders")

    def mode_menu(self):
        print("1- Cash")
        print("2- Card")
        print("3- Upi")     

    def report_option(self):
        self.report_type()
        report_option = int(input("Enter option: "))
        if report_option == 1:
            self.mode_report()
        elif report_option == 2:
            self.total_orders()
            

    def mode_report(self):
        try:
            self.mode_menu()
            pay_mode = int(input("Enter option: : "))
            if pay_mode == 1:
                mode = "cash"
            elif pay_mode == 2:
                mode = "upi"
            elif pay_mode == 3:
                mode = "card"
            else:
                print(print_obj.invalid_msg)

            modelist = []
            for bill in bill_obj.bill_list:
                if bill["mode"] == mode:
                    modelist.append(bill)
            self.display_mode(modelist)
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

    def total_orders(self):
        print("working..Total orders no.")    


report_obj = ReportData()

