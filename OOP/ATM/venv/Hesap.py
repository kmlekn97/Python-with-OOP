class Hesap():
    __kullanici_adi=""
    __parola=""
    __bakiye=""
    def __init__(self,kullanici_adi,parola,bakiye):
        self.__kullanici_adi = kullanici_adi
        self.__parola = parola
        self.__bakiye = bakiye

    def setKullanici_adi(self, kullanici_adi):
        self.__kullanici_adi = kullanici_adi

    def setparola(self, parola):
        self.__parola = __parola

    def setbakiye(self, bakiye):
        self.__bakiye = __bakiye

    def getKullanici_adi(self):
        return self.__kullanici_adi;

    def getparola(self):
        return self.__parola;

    def getbakiye(self):
        return self.__bakiye
    def parayatir(self,tutar):
        self.__bakiye+=tutar
        print("Yeni Bakiyeniz:",self.__bakiye)
    def para_cek(self,tutar):
        if (self.__bakiye-tutar)<0:
            print("Yetersiz Bakiye")
        else:
            self.__bakiye -= tutar
            print("Yeni Bakiyeniz:", self.__bakiye)