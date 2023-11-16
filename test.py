from models.models import *


userInfo = ('admin','admin@gmail.com',8086689923,'hanna','admin')
user = User()
userLoginInfo = ('admin@gmail.com','admin')




if user.register(userInfo):
    print("Successfully registered user")
else:
    print("Failed to register user")

if user.login(userLoginInfo):
    print("Successfully logged in")
else:
    print("Check login info and try again")
