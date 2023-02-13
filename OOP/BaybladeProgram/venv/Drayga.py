import Beyblade
class Drayga(Beyblade.Beyblade):
    __kutsalCanavar=""
    def __init__(self, beybladeci, donusHizi, saldiriGucu,kutsalcanavar):
        super().__init__(beybladeci, donusHizi,saldiriGucu)
        self.__kutsalCanavar=kutsalcanavar

    def KutsalCanavarOrtayaCikar(self):
        print(self.getbeybladeci()+" "+self.__kutsalCanavar+" ı ortaya çıkıyor")
        print(self.getbeybladeci() + " ın Savunması  : Kaplan Pençesi")

    def bilgileriGoster(self):
        super().bilgileriGoster()
        print("Kutsal Canavar Adı :", self.__kutsalCanavar)
