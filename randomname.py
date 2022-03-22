import random
 
def isimOlusturucu():
    isim = ["Ali","Ufuk","Mert","Hayrettin","Murat", "Hulusi", "Nazlı", "Veli", "İbrahim", "Elif", "Zehra"]
    soyisim = ["Şahin", "Akın", "Koç", "Türk", "Kaya", "Yıldız", "Zeki"]
    return "{} {}".format(random.choice(isim), random.choice(soyisim))
 
for i in range(5):
    print(isimOlusturucu())
