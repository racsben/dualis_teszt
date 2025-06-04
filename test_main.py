from main import kodolas,dekodolas,abc,uzenet,kulcs, kodolt
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

# ha az eredmény nagyobb mint 26, akkor az eredmény a 27-el való osztás maradéka

# ha a kulcs hosszabb mint az üzenet, akkor a rejtjeles üzenet hossza az üzenet hossza lesz
def test_kodolas():
    if len(kulcs) > len(uzenet):
        assert len(kodolt) == len(uzenet)



def test_kodolas():
    uzenet = "helloworld"
    kulcs = "abcdefgijkl"
    rejtett = "hfnosauzun"
    assert kodolas(uzenet, kulcs) == rejtett

def test_dekodolas():
    kod = "hfnosauzun"
    uzenet = "helloworld"
    kulcs = "abcdefgijk"
    kulcs1 = "abcdefgijkl"
    if len(kod) == len(uzenet):
        assert dekodolas(kod,uzenet) == kulcs