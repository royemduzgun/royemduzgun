import random

# Film adlarını içeren bir liste
films = [
    "Yüzüklerin Efendisi: Yüzük Kardeşliği",
    "Harry Potter ve Felsefe Taşı",
    "Matrix",
    "Star Wars: Yeni Umut",
    "Pulp Fiction",
    "Başlangıç",
    "Yeşil Yol",
    "Gladyatör",
    "Yedi",
    "Forrest Gump",
    "Interstellar",
    "Kara Şövalye",
    "Sonsuzluk Taşı",
    "Avengers: Endgame",
    "Titanic",
    "Schindler'in Listesi",
    "Cennetin Krallığı",
    "Django Özgür Bırakıldı",
    "Örümcek Adam: Eve Dönüş",
    "Sessizlik",
    "Akıl Oyunları",
    "Kaptan Amerika: İlk Yenilmez",
    "İçimizdeki Şeytan",
    "Se7en",
    "Fargo"
]

def rastgele_film_öner():
    """Filmlerden rastgele birini öneren fonksiyon"""
    return random.choice(films)

if __name__ == "__main__":
    print("Rastgele bir film önerisi için 'enter' tuşuna basın.")
    input()
    print("Önerilen Film:", rastgele_film_öner())
