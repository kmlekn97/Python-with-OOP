import IMuhendis
from interface import implements, Interface
class PCMuhendis(implements(IMuhendis.IMuhendis)):

    __askerlik=None
    __adli_sicil=None

    def __init__(self, askerlik, adli_sicil):
        self.__askerlik = askerlik
        self.__adli_sicil = adli_sicil

    def askerlik_durumu_sorgula(self):
        if self.__askerlik:
            print("Askerliğimi Yaptım.")
        else:
            print("Askerliğimi henüz yapmadım.")

    def mezuniyet_ortalamasi(self, derece):
        return "Ortalama: "+str(derece)

    def adli_sicil_sorgula(self):
        if self.__adli_sicil:
            print("Adli Sicil Kaydım Bulunuyor.")
        else:
            print("Herhangi bir adli sicil kaydım bulunmuyor.")

    def is_tecrubesi(self, array=[]):
        if len(array) > 0:
            print("Bilgisayar Mühendisi Olarak Şu Şirketlerde Çalıştım...")
            for i in array:
                print(i, end=" ")
        else:
            print("Herhangi bir iş tecrübem bulunmuyor...")
