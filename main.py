import random
import os

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
#print(dekodolas(rejtjelezett,uzenet))

#2

#Adatok generálása
mind = []
with open("words.txt", "r", encoding="utf-8") as f:
    for sor in f:
        szo = sor.strip()
        if szo:
            mind.append(szo)

hossz1 = 3
hossz2 = 3
if len(mind) >= hossz1 + hossz2:
        valasztott_szavak = random.sample(mind, hossz1 + hossz2)

uzenetl1 = valasztott_szavak[hossz1:]
uzenetl2 = valasztott_szavak[:hossz2]
#--------Üzenetek stringgé alakítása--------------
uzenet1 = ' '.join(uzenetl1)
uzenet2 = ' '.join(uzenetl2)
#----------Kulcs generálása-----------------
length = len(uzenet1)
kulcs = ''.join(random.choices(abc , k=length))

#Kódolom az üzeneteket
rejt_uzenet1 = kodolas(uzenet1,kulcs)
rejt_uzenet2 = kodolas(uzenet2,kulcs)
print(rejt_uzenet1)
print(rejt_uzenet2)
#binárisra lefordítom a stringeket
def binarisra(szoveg):
    return ''.join(format(ord(i), '08b') for i in szoveg)
kulcs_bin = binarisra(kulcs)
print(kulcs_bin)
rejt_uzenet1_bin = binarisra(rejt_uzenet1)
print(rejt_uzenet1_bin)
rejt_uzenet2_bin = binarisra(rejt_uzenet2)
print(rejt_uzenet2_bin)



#kulcs(rész) = titkositott1(resz) + eredeti1(resz)
