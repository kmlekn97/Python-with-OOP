import BeybladeFabrikasi
import Beyblade
print("""
Beyblade Programına Hoşgeldiniz...
Çıkış için q'ya basın...
""")

while True:
    islem=input("Hangi Beyblade'i üretmek istiyorsunuz ? ")
    if islem=="q":
        break
    else:
        beyblade=BeybladeFabrikasi.BeybladeFabrikasi().beybladeUret(islem)
        if beyblade=="":
            print("Lütfen geçerli bir beyblade ismi girin...")
        else:
            beyblade.bilgileriGoster()
            beyblade.saldir()
            beyblade.KutsalCanavarOrtayaCikar()


