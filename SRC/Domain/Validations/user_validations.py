import uuid

class UserValidation:
    def user_name(self):
        while True:       
            ask_name = input("Enter name: ").lower()
            if ask_name.isalpha():
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
        
    def user_id(self,id_length = None):
        unique_id = self.unique_id = str(uuid.uuid4())[:id_length]
        return unique_id

    def user_address(self):
        ask_address = input("Enter address: ").lower()
        return ask_address
    
    def user_role(self):
        set_role = "staff"
        return set_role

    def user_password(self):
        while True:
            ask_password = input("Enter password: ")
            if len(ask_password) >= 8 and "@" in ask_password:
                return ask_password
            else:
                print("Password must be atleast 8 characters long and include @ also")
    
validation_obj = UserValidation()