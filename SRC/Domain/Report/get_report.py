from SRC.Domain.Bill.generate_bill import bill_obj
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation.print_variables import print_obj
import datetime

class ReportData:

    def time_range_menu(self):
        print("1 - Weekly")
        print("2 - Monthly")
        print("3 - 6 Months")
        print("4 - Yearly")

    def time_report(self):
        try:
            self.time_range_menu()
            range_option = int(input("Enter option: "))
            today = datetime.datetime.now()

            if range_option == 1:
                time_compare = today + datetime.timedelta(-7)
            elif range_option == 2:
                time_compare = today + datetime.timedelta(-30)
            elif range_option == 3:
                time_compare = today + datetime.timedelta(-180)
            elif range_option == 4:
                time_compare = today + datetime.timedelta(-365)
            else:
                print(print_obj.invalid_msg)

            timelist = []
            for bill in bill_obj.bill_list:
                if bill["order_time"] >= time_compare.strftime("%d/%m/%Y, %H:%M:%S"):
                    timelist.append(bill)

            self.display_mode(timelist)

        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

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
        print("2 - Time wise")

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
            self.time_report()
            
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
 

report_obj = ReportData()

