
class UserValidation:
    def user_name(self): 
        while True:       
            ask_name = input("Enter name: ")
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
        ask_email = input("Enter email.com")
        return ask_email
        
    def user_id(self):
        pass

    def user_address(self):
        ask_address = input("Enter Address")
        return ask_address

    def user_role(self):
        pass

    def user_password(self):
        ask_password = input("Enter password")
        return ask_password
    
validation_obj = UserValidation()