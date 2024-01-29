oyun=input("hangi steam oyununu istiyorsunuz?")

if oyun==("cs:go"):
    version=int(input("hangi versiyonu istiyorsunuz?"))
    if(version==1 or version==2):
        print("cs:go",version,"versiyonunun ücreti 20tldir.")
    elif(version==3):
        print("cs:go",version,"versiyonunun ücreti 30tldir.")
    else:
        print("aradığınız versiyon bulunmamaktadır.")


elif oyun==("garrys mod"):
      print("garrys mod oyunun ücreti 10tldir.")
      
elif oyun==("euro truck"):
    version=int(input("hangi versiyonu istiyorsunuz?"))
    if(version==1 or version==2):
        print("euro truck",version,"versiyonunun ücreti 25tldir.")
        
    else:
        print("aradığınız versiyon bulunmamaktadır.")

        
else:
    print("sadece cs:go,garrys mod veya euro truck oyunları alabilirsiniz.")
        
         
  
