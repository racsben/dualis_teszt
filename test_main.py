import main
import pytest

@pytest.mark.parametrize("uzenet, kulcs, eredmeny", [
    ("helloworld", "abcdefgijkl","hfnosauzun"),
    ("asd","asd","ajg"),
    ("hello world","kvhuwvnwpds","rzsejuijfov"),
    ("hello world","kvhuw vnwpds","rzsejzqam g"),
    ("helloworld","kvhuw vnwpds","rzsejvidgs") 
])

def test_kodolas(uzenet, kulcs, eredmeny):
    assert main.kodolas(uzenet,kulcs) == eredmeny


@pytest.mark.parametrize("uzenet1, kulcs1, rejtett1", [
    ("helloworld", "abcdefgijkl","hfnosauzun"),
    ("asd","asd","ajg"),
    ("aello world","kvhuwvnwpds","kzsejuijfov"),
    ("aello world","kvhuw vnwpds","kzsejzqam g"),
    ("aelloworld","kvhuw vnwpds","kzsejvidgs") 
])
def test_dekodolas(uzenet1, kulcs1, rejtett1):
    assert main.dekodolas(rejtett1,kulcs1) == uzenet1

#dekod2 teszteléséhez adatok
#Adatok generálása
mind = []
with open("words.txt", "r", encoding="utf-8") as f:
    for sor in f:
        szo = sor.strip()
        if szo:
            mind.append(szo)

#print(mind)
""" hossz1 = 3
hossz2 = 3
if len(mind) >= hossz1 + hossz2:
        valasztott_szavak = random.sample(mind, hossz1 + hossz2)

uzenetl1 = valasztott_szavak[hossz1:]
uzenetl2 = valasztott_szavak[:hossz2] """

#--------Üzenetek stringgé alakítása--------------
uzenet1 = "curiosity killed the cat" #' '.join(uzenetl1)
print(f"{uzenet1=}")
uzenet2 = "early bird catches the worm" #' '.join(uzenetl2)
print(f"{uzenet2=}")


#----------Kulcs generálása-----------------
length = min(len(uzenet1),len(uzenet2))
kulcs2 = "thisisaverysecretandlongkeyfortesting"#''.join(random.choices(abc , k=length))
print(f"{kulcs2=}")
#Kódolom az üzeneteket
rejt_uzenet1 = main.kodolas(uzenet1,kulcs2)
rejt_uzenet2 = main.kodolas(uzenet2,kulcs2)
#print(f"{rejt_uzenet1=}")
#print(f"{rejt_uzenet2=}")

'''
def test_dekod2_auto():
    assert kulcs2 in main.dekod2_auto(rejt_uzenet1,rejt_uzenet2)
'''

def test_dekod2_auto_ismert_esettel(monkeypatch): 
   
    # minimális szótár csak ehhez a teszthez.
    test_szavak = {"curiosity", "killed", "the", "cat", "early", "bird", "catches", "worm"}
    test_prefixek = {szo[:i] for szo in test_szavak for i in range(1, len(szo) + 1)}

    # 2. LÉPÉS: A monkeypatch segítségével cseréljük le a 'main' modulban lévő
    # globális szótárakat a mi kicsi, teszt szótárainkra a teszt futásának idejére.
    monkeypatch.setattr(main, "SZAVAK", test_szavak)
    monkeypatch.setattr(main, "DARAB_SZO", test_prefixek)

    # 3. LÉPÉS: A teszt többi része most már a kicsi szótárral fog futni.
    uzenet1 = "curiosity killed the cat"
    uzenet2 = "early bird catches the worm"
    ismert_kulcs = "thisisaverysecretandlongkeyfortesting"
    
    hossz = min(len(uzenet1), len(uzenet2))
    hasznalt_kulcs = ismert_kulcs[:hossz]

    # Mivel a szótár most már kicsi, egy hosszabb üzenetrészleten is gyorsan lefut a teszt.
    reszlet_hossz = 16 # Pl. "curiosity kille" és "early bird catch"
    
    reszlet_uzenet1 = uzenet1[:reszlet_hossz]
    reszlet_uzenet2 = uzenet2[:reszlet_hossz]
    reszlet_kulcs = hasznalt_kulcs[:reszlet_hossz]

    rejt_reszlet1 = main.kodolas(reszlet_uzenet1, reszlet_kulcs)
    rejt_reszlet2 = main.kodolas(reszlet_uzenet2, reszlet_kulcs)

    megoldasok = main.dekod2_auto(rejt_reszlet1, rejt_reszlet2)

    # Ellenőrizzük, hogy a megoldások között szerepel-e az általunk használt kulcsrészlet.
    assert reszlet_kulcs in megoldasok


