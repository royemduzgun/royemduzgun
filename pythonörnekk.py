user="rn1478"
password="15236"

while True:
    kullanici=input("kullanıcı adınızı giriniz:")
    parola=input("şifrenizi giriniz:")
    if kullanici==user and parola==password:
        print("hosgeldiniz")
        break
    elif kullanici==user and parola!=password:
        print("şifreniz yanlış\n")
    elif kullanici!=user and parola==password:
        print("kullanıcı adınız yanlış\n")
    else:
        print("kullanıcı adı ve şifre hatalı\n")
