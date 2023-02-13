from Sign_up_Manager import Sign_up_Manager
from User import User
from AgeUserCheckService import AgeUserCheckService
from ComplexUserCheckService import ComplexUserCheckService
service=ComplexUserCheckService()
signUpManager=Sign_up_Manager(service)
signUpManager.Signup(User(1,"Kemal",25))