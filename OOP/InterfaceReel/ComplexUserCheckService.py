from IUserCheckService import IUserCheckService
from Interface import implements
class ComplexUserCheckService(implements(IUserCheckService)):

    def checkUser(self, user):
        if user.getage() >= 18 and str(user.getname()).startswith("Ke"):
            return True
        else:
            return False