class Login():
    __kullaniciadi=""
    __parola=""
    @classmethod
    def login(cls,hesap):
        cls.__kullaniciadi=input("Kullanıcı Adı Giriniz...")
        cls.__parola = input("Parola Giriniz...")
        if cls.__kullaniciadi==hesap.getKullanici_adi() and cls.__parola==hesap.getparola():
            return True
        else:
            return False
