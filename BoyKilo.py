kilo = float(input("Lütfen kilonuzu kg cinsinden giriniz: "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
 
vki = kilo / (boy ** 2) #Formülü uyguluyoruz.
 
print("VKİ değeriniz:", vki) #Değeri ekrana yazdırıp;
 
#Koşullara göre sonucu yazdırıryoruz.
if vki < 18.5:
    print("Zayıf")
elif vki >= 18.5 and vki < 25:
    print("Normal")
elif vki >= 25 and vki < 30:
    print("Fazla kilolu")
else:
    print("Obez")
