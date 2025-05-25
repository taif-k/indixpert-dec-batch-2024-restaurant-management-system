from SRC.Domain.Bill.generate_bill import bill_obj
from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Validation.print_variables import print_obj
import datetime
from SRC.Domain.Path.all_paths import path_obj

class ReportData:

    def time_range_menu(self):
        print()
        print("1 - Today")
        print("2 - Weekly")
        print("3 - Monthly")
        print("4 - 6 Months")
        print("5 - Yearly")

    def report_type(self):
        print()
        print("---------REPORT---------")
        print("1 - Orders")
        print("2 - Errors")
        print("0 - Exit")

    # getting data for today, weekly, current month, 6 months and yearly
    def timeline_range(self):
        try:
            self.time_range_menu()
            range_option = int(input("Enter option: ")) 
            now = datetime.datetime.now()
            today_date = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)

            if range_option == 1:
                time_compare = today_date
            elif range_option == 2:
                time_compare = today_date + datetime.timedelta(-7)
            elif range_option == 3:
                time_compare = today_date + datetime.timedelta(-30)
            elif range_option == 4:
                time_compare = today_date + datetime.timedelta(-180)
            elif range_option == 5:
                time_compare = today_date + datetime.timedelta(-365)
            else:
                print(print_obj.invalid_msg)
            
            self.date_differnce = time_compare
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

    # Report  A. Orders B. Errors 
    def report_option(self):
        while True:
            try:
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
            except Exception as err:
                print(print_obj.err_msg)
                file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

report_obj = ReportData()

# Order Report has two types, A. Payment mode B. Timewise report(weekly etc) 
class OrderReport(ReportData):
    def orders_timeline(self):
        try:
            self.timeline_range()    
            timelinelist = []
            for bill in bill_obj.bill_list:
                if bill["order_time"]  >= self.date_differnce.strftime("%Y-%m-%d %H:%M:%S"):
                    timelinelist.append(bill)

            report_display_obj.display_mode(timelinelist)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

    def mode_type(self):
        try:
            print()
            print("1- Cash")
            print("2- Card")
            print("3- Upi") 

            mode_option = int(input("Enter mode option: : "))
            if mode_option == 1:
                mode = "cash"
            elif mode_option == 2:
                mode = "card"
            elif mode_option == 3:
                mode = "upi"
            else:
                print(print_obj.invalid_msg)
                return None

            modelist = []
            for bill in bill_obj.bill_list:
                if bill["mode"] == mode:
                    modelist.append(bill)
            report_display_obj.display_mode(modelist)
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

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
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

report_order = OrderReport()

# Error Report has timewise option 
class ErrorReport(ReportData):
    def errors_type(self):            
        try:
            self.timeline_range()
            errors = file_operation_obj.read_file(path_obj.error_path)
            sortederrors = []
            for err in errors:
                if err["date"] >= self.date_differnce.strftime("%Y-%m-%d %H:%M:%S"):
                    sortederrors.append(err)
            report_display_obj.formated_err_display(sortederrors)

        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

report_error = ErrorReport()

class ReportDisplay:
    def display_mode(self, modelist):
        print("------------------------------------------------------------------------")
        print("Order ID      Customer Name      Total Amount      Order Time")
        print("------------------------------------------------------------------------")

        total = 0
        for bill in modelist:
            print(f"{bill['order_id']}\t\t{bill['customer_name']}\t\t{bill['total']}\t\t{bill['order_time']}")
            total += bill["total"]

        print("------------------------------------------------------------------------")
        print(f"Total orders: {len(modelist)}")
        print(f"Total : Rs {total}")

    def formated_err_display(self, sortederrors):
        print("------------------------------------------------------------------------------------------------------")
        print("MODULE               FUNCTION                 ERROR                        LINE        ERROR TIME")
        print("------------------------------------------------------------------------------------------------------")

        for err in sortederrors:
            print(f"{err['module']:<20} {err['function']:<20}  {err['error'][:30]:<32}  {str(err['line']):<8}  {err['date']:<8}")

        print("\n------------------")
        print(f"Total Errors  {len(sortederrors)}")
        print("------------------")

report_display_obj = ReportDisplay()
