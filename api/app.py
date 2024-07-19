
from config import app,api
from models import User
from auth import UserSignUp, UserLogin
from resources import *

# Adding resources to the API
api.add_resource(UserSignUp, '/signup')
api.add_resource(UserLogin, '/login')


if __name__ == '__main__':
    app.run(debug=True)
