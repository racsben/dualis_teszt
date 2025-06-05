import random

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
index=[ 0 , 1 , 2 ,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

"""uzenet = input("Adjon meg egy Üzenetet: ")   #"helloworld" 
kulcs = input("Adjon meg egy kulcsot: ")    #"abcdefgijkl"
while len(kulcs) < len(uzenet):
   kulcs = input("Adjon meg egy kulcsot, egyenlő hossúságut az üzenettel: ")"""    

uzenet = "helloworld"
kulcs = "abcdefgijkl"

def kodolas(uzenet, kulcs):
    uzenet_szam = [] 
    kulcs_szam = []
    #kigyűjtöm a bekért adatok karaktereihez rendelt számot
    for u, k in zip(uzenet,kulcs):
        for betu,szam in zip(abc,index):
            if u == betu:
                uzenet_szam.append(szam)
            if k == betu:
                kulcs_szam.append(szam)

    #kód kialakítása
    kodolt = "" #hfnosauzun 
    kodolt_szam = [] 
    lista_hossza = len(index)
    for u, k in zip(uzenet_szam, kulcs_szam):
        kodolt_kar_szam = (u+k) % lista_hossza
        kodolt_szam.append(kodolt_kar_szam)

    for k in kodolt_szam:
        for betu,szam in zip(abc,index):
            if k == szam:
                kodolt += betu
    
    return kodolt
rejtjelezett = kodolas(uzenet,kulcs)
#print(rejtjelezett)

#DEKÓDOLÁS

def dekodolas(kodolt,uzenet):
    uzi_szam = []
    kod_szam = []
    #kigyűjtöm a bekért adatok karaktereihez rendelt számot
    for k, u in zip(kodolt,uzenet):
        for betu,szam in zip(abc,index):
            if k == betu:
                kod_szam.append(szam)
            if u == betu:
                uzi_szam.append(szam)

    #dekódolás
    kulcs_szam = []   
    lista_hossza = len(index)
    for u, k in zip(uzi_szam, kod_szam):
        kulcs_kar_szam = (k-u) % lista_hossza
        kulcs_szam.append(kulcs_kar_szam)
   
    kulcs = ""
    for k in kulcs_szam:
        for betu,szam in zip(abc,index):
            if k == szam:
                kulcs += betu

    return kulcs
print(dekodolas(rejtjelezett,uzenet))


#2


uzenet1 = "" #early  4 0 17 11 24 
uzenet2 = "" #curios 2 20 17 8 14 18
kulcs = "" #
with open("words.txt", "r", encoding="utf-8") as f:
    mind = f.read()
    szavak = list(map(str, mind.split()))

    uzenet1 = random.choice(szavak)
