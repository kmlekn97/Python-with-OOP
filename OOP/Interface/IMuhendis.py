from interface import implements, Interface
class IMuhendis(Interface):
    def askerlik_durumu_sorgula(self):
        pass
    def mezuniyet_ortalamasi(self,derece):
        pass

    def adli_sicil_sorgula(self):
        pass

    def is_tecrubesi(self,array=[]):
        pass