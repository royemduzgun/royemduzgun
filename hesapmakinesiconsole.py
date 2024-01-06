def hmmenu():
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-Çarpma           ║")
    print("║  4-Bölme            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    # 201 ╔
    # 205 ═
    # 187 ╗
    # 186 ║
    # 200 ╚
    # 188 ╝
secim = input("İşlem yapmak istediğiniz numarayı girin (1/2/3/4): ")

sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

if secim == '1':
   print(sayi1,"+",sayi2,"=", sayi1+sayi2)

elif secim == '2':
   print(sayi1,"-",sayi2,"=", sayi1-sayi2)

elif secim == '3':
   print(sayi1,"*",sayi2,"=", sayi1*sayi2)

elif secim == '4':
   print(sayi1,"/",sayi2,"=", sayi1/sayi2)

else:
   print("Geçersiz işlem seçtiniz.")

    
    
