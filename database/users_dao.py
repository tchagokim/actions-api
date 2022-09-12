from database.dao import DAO
from database.data import users_data
from schemas.user_schema import UserSchema


class UsersDAO(DAO):
    def __init__(self):
        super().__init__(users_data)

    def get_user(self, id_):
        return self.read_id(id_)

    def get_user_by_username(self,username):
        for user in users_data:
            if user.username == username:
                return user
        return None

    def get_users(self):
        return self.read()
