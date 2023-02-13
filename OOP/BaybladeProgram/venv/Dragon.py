import Beyblade
class Dragon(Beyblade.Beyblade):
    __kutsalCanavar = ""
    __gizliYetenek=""

    def __init__(self, beybladeci, donusHizi, saldiriGucu, kutsalcanavar,gizliYetenek):
        super().__init__(beybladeci, donusHizi, saldiriGucu)
        self.__kutsalCanavar = kutsalcanavar
        self.__gizliYetenek=gizliYetenek

    def KutsalCanavarOrtayaCikar(self):
        print(self.getbeybladeci() + " " + self.__kutsalCanavar + " ı ortaya çıkıyor")
        print(self.getbeybladeci() + " ın Savunması  : Hayalet Kasırgası")

    def bilgileriGoster(self):
        super().bilgileriGoster()
        print("Kutsal Canavar Adı :", self.__kutsalCanavar)