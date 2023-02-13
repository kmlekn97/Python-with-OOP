from Interface import implements
from  IUserCheckService import IUserCheckService
class AgeUserCheckService(implements(IUserCheckService)):
    def checkUser(self,user):
        if user.getage()>=18:
            return True
        else:
            return False
