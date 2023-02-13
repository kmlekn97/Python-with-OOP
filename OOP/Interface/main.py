import MakineMuhendisi,PCMuhendis
import IMuhendis
muhendis1=PCMuhendis.PCMuhendis(False,False)
muhendis1.askerlik_durumu_sorgula()
muhendis1.adli_sicil_sorgula()
print(" ",muhendis1.mezuniyet_ortalamasi(3.85))
tecrube=["Vestel","Trendyol","Hugo Boss"]
muhendis1.is_tecrubesi(tecrube)
muhendis2=MakineMuhendisi.MakineMuhendisi(True,False)
muhendis2.askerlik_durumu_sorgula()
muhendis2.adli_sicil_sorgula()
tecrube2=[]
referans=["ddqdq","dad"]
print(" ",muhendis2.mezuniyet_ortalamasi(2.25))
muhendis2.is_tecrubesi()
muhendis2.calis()
muhendis2.referans_getir(referans)
