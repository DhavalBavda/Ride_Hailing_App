class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self,user):
        self.users[user.email] = user

    def get_user_by_id(self, user_id):
        return self.users.get(user_id, None)

    def get_user_by_email(self, email):
        for user in self.users.values():
            if user.email == email:
                return user
        return None
    
    def list_users(self):
        return list(self.users.values())