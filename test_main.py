from main import kodolas, dekodolas, dekod2_auto, abc, index,  betu_szamra, szam_beture
import pytest
import random

@pytest.mark.parametrize("uzenet, kulcs, eredmeny", [
    ("helloworld", "abcdefgijkl","hfnosauzun"),
    ("asd","asd","ajg"),
    ("hello world","kvhuwvnwpds","rzsejuijfov"),
    ("hello world","kvhuw vnwpds","rzsejzqam g"),
    ("helloworld","kvhuw vnwpds","rzsejvidgs") 
])

def test_kodolas(uzenet, kulcs, eredmeny):
    assert kodolas(uzenet,kulcs) == eredmeny


@pytest.mark.parametrize("uzenet1, kulcs1, rejtett1", [
    ("helloworld", "abcdefgijkl","hfnosauzun"),
    ("asd","asd","ajg"),
    ("aello world","kvhuwvnwpds","kzsejuijfov"),
    ("aello world","kvhuw vnwpds","kzsejzqam g"),
    ("aelloworld","kvhuw vnwpds","kzsejvidgs") 
])
def test_dekodolas(uzenet1, kulcs1, rejtett1):
    assert dekodolas(rejtett1,kulcs1) == uzenet1

#dekod2 teszteléséhez adatok
#Adatok generálása
mind = []
with open("words.txt", "r", encoding="utf-8") as f:
    for sor in f:
        szo = sor.strip()
        if szo:
            mind.append(szo)

#print(mind)
hossz1 = 3
hossz2 = 3
if len(mind) >= hossz1 + hossz2:
        valasztott_szavak = random.sample(mind, hossz1 + hossz2)

uzenetl1 = valasztott_szavak[hossz1:]
uzenetl2 = valasztott_szavak[:hossz2]
#--------Üzenetek stringgé alakítása--------------
uzenet1 = ' '.join(uzenetl1)
print(f"{uzenet1=}")
uzenet2 = ' '.join(uzenetl2)
print(f"{uzenet2=}")


#----------Kulcs generálása-----------------
length = min(len(uzenet1),len(uzenet2))
kulcs2 = ''.join(random.choices(abc , k=length))
print(f"{kulcs2=}")
#Kódolom az üzeneteket
rejt_uzenet1 = kodolas(uzenet1,kulcs2)
rejt_uzenet2 = kodolas(uzenet2,kulcs2)
#print(f"{rejt_uzenet1=}")
#print(f"{rejt_uzenet2=}")

def test_dekod2_auto():
    assert dekod2_auto(rejt_uzenet1,rejt_uzenet2) == kulcs2


