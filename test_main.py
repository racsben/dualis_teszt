from main import kodolas, dekodolas,dekod2, abc, index, uzenet, kulcs 
import pytest

# az üzenet az angol abc szerinti kisbetűkből (a-z) és szóközből (' ') állhat
for betu in uzenet:
    assert betu in abc
# a kulcs ugyanezeket a karaktereket tartalmazhatja
for betu in kulcs:
    assert betu in abc
# a kulcsnak legalább akkorának kell lennie mint az üzenetnek
assert len(kulcs) >= len(uzenet)
# a rejtjelezés minden karakterre a következő műveletből  áll:
# rendeljünk a karakterhez egy kódot: a = 0, b = 1, ... z = 25, ' ' (szóköz) = 26

# a rejtjelezett üzenet n. karaktere az üzenet n. karakter kódja + kulcs n. karakter kódja
kodolt = kodolas(uzenet,kulcs)
def test_kodolas():
    uzenet_szam = [] 
    kulcs_szam = []
    for u, k in zip(uzenet,kulcs):
        for betu,szam in zip(abc,index):
            if u == betu:
                uzenet_szam.append(szam)
            if k == betu:
                kulcs_szam.append(szam)
    
    kodolt = "" 
    kodolt_szam = [] 
    lista_hossza = len(index)
    for u, k in zip(uzenet_szam, kulcs_szam):
        # ha az eredmény nagyobb mint 26, akkor az eredmény a 27-el való osztás maradéka
        kodolt_kar_szam = (u+k) % lista_hossza
        if kodolt_kar_szam > 26:
            assert kodolt_kar_szam == (u+k) % lista_hossza
        kodolt_szam.append(kodolt_kar_szam)
        
    for k in kodolt_szam:
        for betu,szam in zip(abc,index):
            if k == szam:
                kodolt += betu
       
def test_kodolas_szokozzel():
    uzenet = "hello world"
    kulcs = "abcdefgijkl"
    rejtett = "hfnosebw vo"
    assert kodolas(uzenet, kulcs) == rejtett

# ha a kulcs hosszabb mint az üzenet, akkor a rejtjeles üzenet hossza az üzenet hossza lesz
def test_kodola_hossz_ellenorzes():
    if len(kulcs) > len(uzenet):
        assert len(kodolt) == len(uzenet)


def test_dekodolas():
    kod = "hfnosauzun"
    uzenet = "helloworld"
    kulcs = "abcdefgijk"
    kulcs1 = "abcdefgijkl"
    if len(kod) == len(uzenet):
        assert dekodolas(kod,kulcs) == uzenet