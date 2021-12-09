from model.user import *
from werkzeug.security import safe_str_cmp
 
def authenticate(name,password):
       user=UserModel.find_by_name(name)

       if user and safe_str_cmp(user.password,password):
              return user
 
def identity(payload):
       userid = payload['identity']
       return UserModel.find_by_id(userid)