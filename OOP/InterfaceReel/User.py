class User:
    __id=None
    __name=None
    __age=None

    def __init__(self,id,name,age):
        self.__id=id
        self.__name=name
        self.__age=age

    def setid(self,id):
        self.__id=id
    def getid(self):
        return self.__id

    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
