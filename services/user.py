from Models.User_model import Users
from repositories.user_repo import UserRepository
from utils.helper import HelperFunctions as HF

class UserManager:

    email_list = []
    
    def __init__(self, user_repo : UserRepository):
        self.user_repo = user_repo
    
    @HF.safe_action_decorator
    def create_user(self):
        name = input("Enter Your Name: ")
        email = input("Enter Email Id: ")
        phone_number = input("Enter Phone Number: ")
        role_input = input("Enter Number 1.Driver  2.Rider: ")
        password = input("Enter Your Password: ")
        verify_password = input("Enter Password Again: ")

        # Validate unique email
        if email in UserManager.email_list:
            print("Email already exists! Please try again or login.")
            return self.create_user()

        # Validate password match
        if password != verify_password:
            print("Passwords do not match! Please try again.")
            return self.create_user()

        # Validate role input
        if role_input == "1":
            role = "Driver"
        elif role_input == "2":
            role = "Rider"
        else:
            print("Invalid role selected! Please try again.")
            return self.create_user()

        # Create user instance
        user = Users(name, email, phone_number, role, password)

        # Add user to repository
        # repo = UserRepository()
        # repo.add_user(user)
        self.user_repo.add_user(user)
        UserManager.email_list.append(email)
        print(f"{role} successfully created!")
        return user

    @HF.safe_action_decorator
    def login_user(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")

        if email not in UserManager.email_list:
            print("Email not found! Please create an account first.")
            return None

        # repo = UserRepository()
        # user = repo.get_user(email)
        
        user = self.user_repo.get_user_by_email(email)


        if user and user.password == password:
            print(f"{user.name} successfully logged in!")
            return user
        else:
            print("Incorrect password! Please try again.")
            return self.login_user()
