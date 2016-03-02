import  os
def bul(yol):

 if os.path.isdir(yol):
     print("klasördür")
 elif os.path.isfile(yol):
     print("dosyadır")
 else:
     print("boyle bir yolda birsey yok")

a=input("path giriniz")
bul(a)