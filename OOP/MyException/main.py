from MyExceptionClass import MyExceptionClass
def kontrol(yas):
    if yas<18:
        raise MyExceptionClass("Hata Oluştu",ArithmeticError)
    else:
        raise MyExceptionClass("Standart",ArithmeticError)
yas=int(input("Yaş Girin:"))
try:
    kontrol(yas)
except MyExceptionClass as e:
    print(e.with_traceback())
