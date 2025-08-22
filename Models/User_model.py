import time
import uuid  

class Users:
    def __init__(self, name, email, phone_no, role, password, user_id=None):
       
        self.id = user_id or str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.role = role
        self.password = password 
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __str__(self):
        return (f"User({self.id}, Name: {self.name}, Email: {self.email}, "
                f"Role: {self.role}, Created At: {self.created_at})")
    
    def get_role(self):
        return self.role
