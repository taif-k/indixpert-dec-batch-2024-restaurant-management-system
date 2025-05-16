from SRC.Domain.Bill.generate_bill import bill_obj
from SRC.Domain.ReadFile import operation_obj
from SRC.Domain.Validation.print_variables import print_obj
import datetime

class ReportData:

    def time_range_menu(self):
        print()
        print("1 - Weekly")
        print("2 - Monthly")
        print("3 - 6 Months")
        print("4 - Yearly")

    def report_type(self):
        print()
        print("---------REPORT---------")
        print("1 - Orders")
        print("2 - Errors")
        print("0 - Exit")

    def timeline_range(self):
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
            
            self.date_differnce = time_compare
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

    def report_option(self):
        while True:
            self.report_type()
            report_option = int(input("\nEnter option: "))
            if report_option == 1:
                report_order.orders_type()
            elif report_option == 2:
                report_error.errors_type()
            elif report_option == 0:
                break
            else:
                print(print_obj.invalid_msg)

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
report_obj = ReportData()

class OrderReport(ReportData):
    def orders_timeline(self):
        try:
            self.timeline_range()    
            timelinelist = []
            for bill in bill_obj.bill_list:
                if bill["order_time"] >= self.date_differnce.strftime("%d/%m/%Y, %H:%M:%S"):
                    timelinelist.append(bill)

            self.display_mode(timelinelist)
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

    def mode_type(self):
        print()
        print("1- Cash")
        print("2- Card")
        print("3- Upi") 

        mode_option = int(input("Enter mode option: : "))
        if mode_option == 1:
            mode = "cash"
        elif mode_option == 2:
            mode = "upi"
        elif mode_option == 3:
            mode = "card"
        else:
            print(print_obj.invalid_msg)

        modelist = []
        for bill in bill_obj.bill_list:
            if bill["mode"] == mode:
                modelist.append(bill)
        self.display_mode(modelist)

    def orders_type(self):
        try:
            print("1 - pay mode Report")
            print("2 - TimeWise Report")
            choose_option = int(input("Enter option: : "))
            if choose_option == 1:
                self.mode_type()
            elif choose_option == 2:
                self.orders_timeline()
        except Exception as err:
            print(print_obj.err_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)

report_order = OrderReport()

class ErrorReport(ReportData):

    def errors_type(self):
        print("Errors report........")

report_error = ErrorReport()