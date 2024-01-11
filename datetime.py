from datetime import date

today1=date.today()

print("yıl:", today1.year)
print("ay:",  today1.month)
print("gün:", today1.day)

yil=int(input("doğum yılı nedir?"))
print("sen:", today1.year-yil,"yaşındasın.")
print("sen:",(today1.year-yil)*12,"ay yaşamıssın.")
print("sen:",(today1.year-yil)*365,"gün yaşamışsın.")
