from database.users_dao import UsersDAO
from fastapi import HTTPException

def only_for(attr,value):
    def wrapper1(func):
        def wrapper(self):
            print("token",self.request.state.token) 
            user = UsersDAO().get_user_by_username(self.request.state.token.get("username")) 
            if user:
                if getattr(user,attr) == value:
                    return func( self )
            raise HTTPException(403)
        return wrapper
    return wrapper1
