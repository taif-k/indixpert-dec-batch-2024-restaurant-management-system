import uuid
import sys,os
import pwinput
sys.path.append(os.getcwd())
from abc import ABC,abstractmethod
from SRC.Domain.ReadFile import file_operation_obj
from SRC.Domain.Validation.print_variables import print_obj
from SRC.Domain.Path.all_paths import path_obj

# abtarction is used for unique id for user id(len= 5), food id(len= 2) and card txn no (len= 16)
class Validation(ABC):
    @abstractmethod
    def id_unique(self):
        pass

class UserValidation(Validation):
    def user_name(self):
        while True:
            try:       
                ask_name = input("Enter name: ").lower()
                if all(word.isalpha() for word in ask_name.split()):
                    return ask_name
                else:
                    print(print_obj.namenot_aplha)
            except Exception as err:
                print(print_obj.err_msg)
                file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")

    def user_contact(self):
        while True:
            ask_contact = input("Enter contact: ")
            if ask_contact.isnumeric() and len(ask_contact) == 10:
                ask_contact = int(ask_contact)
                break
            else:
                print(print_obj.invalid_contact)
        return ask_contact
    
    def user_email(self):
        while True:
            ask_email = input("Enter email: ").lower()
            if "@" in ask_email and "." in ask_email.split("@")[1]:
                return ask_email
            else:
                print(print_obj.invalid_email)
        
    def user_address(self):
        ask_address = input("Enter address: ").lower()
        return ask_address
    
    def id_unique(self):
        try:
            user_id = self.unique_id = str(uuid.uuid4())[:4]
            return user_id
        except Exception as err:
            print(print_obj.err_msg)
            file_operation_obj.write_file(data=file_operation_obj.get_errdetails(err),path=path_obj.error_path,mode="a")
    
    def user_role(self,role = None):
        if role == None:
            set_role = "admin"
                
        set_role = role
        return set_role

    def user_password(self):
        while True:
            ask_password = pwinput.pwinput(prompt="Enter password: ",mask="#")
            if len(ask_password) >= 8 and "@" in ask_password:
                return ask_password
            else:
                print(print_obj.password_demo)

validation_obj = UserValidation()

class FoodValidation(Validation):
    def id_unique(self):
        try:
            food_id = self.unique_id = str(uuid.uuid4())[:2]
            return food_id
        except Exception as err:
            print(print_obj.err_msg)

Foodvalid_obj = FoodValidation()

class PaymentValidation(Validation):
    def id_unique(self):
        try:
            card_upi_no = self.unique_id = str(uuid.uuid4())[:16]
            return card_upi_no
        except:
            print(print_obj.err_msg)
    
paymentid_obj = PaymentValidation()

        
