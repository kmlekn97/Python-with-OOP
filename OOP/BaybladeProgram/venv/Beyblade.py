class Beyblade():
    __beybladeci=""
    __donusHizi=0
    __saldiriGucu=0

    def __init__(self, beybladeci, donusHizi, saldiriGucu):
        self.__beybladeci = beybladeci
        self.__donusHizi = donusHizi
        self.__saldiriGucu = saldiriGucu

    def setbeybladeci(self, beybladeci):
        self.__beybladeci = beybladeci

    def setdonusHizi(self, donusHizi):
        self.__donusHizi = donusHizi

    def setsaldiriGucu(self, saldiriGucu):
        self.__saldiriGucu = saldiriGucu

    def getbeybladeci(self):
        return self.__beybladeci;

    def getdonusHizi(self):
        return self.__donusHizi;

    def getsaldiriGucu(self):
        return self.__saldiriGucu;

    def saldir(self):
        print("{} {} ve {} ile saldırıyor... ".format(self.__beybladeci,self.__saldiriGucu,self.__donusHizi))

    def KutsalCanavarOrtayaCikar(self):
        print("Bu beyblade'in kutsal canavarı bulunmuyor...")

    def bilgileriGoster(self):
        print("Beybladeci İsmi :",self.__beybladeci)
        print("Saldırı Gücü  :", self.__saldiriGucu)
        print("Dönüş Hızı : ", self.__donusHizi)