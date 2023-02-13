import Login
class ATM:
    @staticmethod
    def Atm_Kullan(hesap):
        print("Bankamıza Hoşgeldiniz....")
        print("*************************")
        print("Kullanıcı Girişi")
        print("*************************")
        hak=3
        while True:
            if Login.Login().login(hesap):
                print("Giriş Başarılı")
                break
            else:
                print("Giriş Başarısız")
            hak-=1
            print("Kalan Hak",hak)
            if hak==0:
                print("Hak Bitti")
                return
        print("*************************")
        print("""
        1. Bakiye Görüntüle
        2. Para Yatırma
        3. Para Çekme
        Çıkış için q'ya basın
        """)
        print("*************************")
        while True:
            islem=input("İşlem Seçiniz:")
            if islem=="q":
                break
            elif islem=="1":
                print("Bakiyeniz:",hesap.getbakiye())
            elif islem=="2":
                tutar = int(input("Yatırılacak Tutar Girin:"))
                hesap.parayatir(tutar)
            elif islem=="3":
                cekilecektutar = int(input("Çekilecek Tutar Girin:"))
                hesap.para_cek(cekilecektutar)
            else:
                print("Geçersiz İşlem...")


