import uuid
from abc import ABC,abstractmethod
from SRC.Domain import operation_obj

class Validation(ABC):
    def __init__(self):
        self.error_msg = "Resolving issue with assigning unique id"

    @abstractmethod
    def id_unique(self):
        pass

class UserValidation(Validation):
    def user_name(self):
        while True:       
            ask_name = input("Enter name: ").lower()
            if all(word.isalpha() for word in ask_name.split()):
                return ask_name
            else:
                print("Name should be in Alphabets")

    def user_contact(self):
        while True:
            ask_contact = input("Enter contact: ")
            if ask_contact.isnumeric() and len(ask_contact) == 10:
                ask_contact = int(ask_contact)
                break
            else:
                print("Contact should be of 10 digits")
        return ask_contact
    
    def user_email(self):
        while True:
            ask_email = input("Enter email: ").lower()
            if "@" in ask_email and "." in ask_email.split("@")[1]:
                return ask_email
            else:
                print("Enter valid Email....Ex: taif@mail.com")
        
    def user_address(self):
        ask_address = input("Enter address: ").lower()
        return ask_address
    
    def id_unique(self):
        try:
            user_id = self.unique_id = str(uuid.uuid4())[:4]
            return user_id
        except Exception as err:
            print(self.error_msg)
            operation_obj.write_file(data=operation_obj.get_errdetails(err),path=operation_obj.err_path,mode="a",isJson=0)
    
    def user_role(self,role = None):
        if role == None:
            set_role = "admin"
                
        set_role = role
        return set_role

    def user_password(self):
        while True:
            ask_password = input("Enter password: ")
            if len(ask_password) >= 8 and "@" in ask_password:
                return ask_password
            else:
                print("Password must be atleast 8 characters long and include @ also")

validation_obj = UserValidation()

class FoodValidation(Validation):
    def id_unique(self):
        try:
            food_id = self.unique_id = str(uuid.uuid4())[:2]
            return food_id
        except Exception as err:
            print(self.error_msg)

Foodvalid_obj = FoodValidation()

class PaymentValidation(Validation):
    def id_unique(self):
        try:
            card_upi_no = self.unique_id = str(uuid.uuid4())[:16]
            return card_upi_no
        except:
            print(self.error_msg)
    
paymentid_obj = PaymentValidation()

        
