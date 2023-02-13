import Dragon
import Dranza
import Drayga
import Draciel
class BeybladeFabrikasi():

    @classmethod
    def beybladeUret(cls,beyblade_turu):
        if beyblade_turu=="Dragon":
            return Dragon.Dragon("Takao", 800, 300,"Mavi Ejderha","Kutsal Canavarla Konuşma")
        elif beyblade_turu=="Dranza":
            return Dranza.Dranza("Kai",600,400,"Kırmızı Anka Kuşu")
        elif beyblade_turu=="Drayga":
            return Drayga.Drayga("Rei",800,250,"Beyaz Kaplan")
        elif beyblade_turu=="Draciel":
            return Draciel.Draciel("Max",400,1000,"Kara Kaplumbağa")
        else:
            return ""