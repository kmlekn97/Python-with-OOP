class Sign_up_Manager:
    __IUserCheckService = None

    def __init__(self, UserCheckService):
        self.__IUserCheckService = UserCheckService

    def Signup(self, user):
        if self.__IUserCheckService.checkUser(user):
            print("Kullanıcı Adı " + user.getname())
        else:
            print("Kullanıcı Kayıt Olamadı...")
