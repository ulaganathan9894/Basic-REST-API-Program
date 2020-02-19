from werkzeug.security import safe_str_cmp
from Models.user import UserModel

#users = [User(1,"ulaga", "ulaga007")]


#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = UserModel.usernamefinding(username)

    if user and safe_str_cmp(user.password, password):
        return user



def identity(payload):
    user_id = payload['identity']
    return UserModel.firsttimeid(user_id)
    
