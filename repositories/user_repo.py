class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self,user):
        self.users[user.email] = user

    def get_user(self,email):
        return self.users.get(email)
    
    def list_users(self):
        return list(self.users.values())