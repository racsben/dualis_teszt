import random
import os
from operator import xor

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

def dekodolas(kodolt,kulcs):
    uzi_szam = []
    kulcs_szam = []
    #kigyűjtöm a bekért adatok karaktereihez rendelt számot
    for k, u in zip(kodolt,kulcs):
        for betu,szam in zip(abc,index):
            if k == betu:
                kulcs_szam.append(szam)
            if u == betu:
                uzi_szam.append(szam)

    #dekódolás
    uzenet_szam = []   
    lista_hossza = len(index)
    for u, k in zip(uzi_szam, kulcs_szam):
        uzenet_kar_szam = (k-u) % lista_hossza
        uzenet_szam.append(uzenet_kar_szam)
   
    visszafejtett_uzenet = ""
    for k in uzenet_szam:
        for betu,szam in zip(abc,index):
            if k == szam:
                visszafejtett_uzenet += betu

    return visszafejtett_uzenet

#print(dekodolas(rejtjelezett,kulcs))

#2

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
print(f"uzenet1: {uzenet1}")
uzenet2 = ' '.join(uzenetl2)


#----------Kulcs generálása-----------------
length = len(uzenet1)
kulcs2 = ''.join(random.choices(abc , k=length))
print(f"kulcs2: {kulcs2}")
#Kódolom az üzeneteket
rejt_uzenet1 = kodolas(uzenet1,kulcs2)
rejt_uzenet2 = kodolas(uzenet2,kulcs2)
print(rejt_uzenet1)
#binárisra lefordítom a stringeket
""" 
def binarisra(szoveg):
    return ''.join(format(ord(i), '08b') for i in szoveg)

def stringge(szoveg):
    return ''.join(chr(int(szoveg[i:i+8], 2)) for i in range(0, len(szoveg), 8)) """
""" 
kulcs2_bin = binarisra(kulcs2)
print(f"Kulcs2_bin: {kulcs2_bin}")
rejt_uzenet1_bin = binarisra(rejt_uzenet1)
#print(rejt_uzenet1_bin)
rejt_uzenet2_bin = binarisra(rejt_uzenet2)
#print(rejt_uzenet2_bin) """

p1_szavak = []
p2_szavak = []
kitalalt_kulcs = ""

def dekod2(p1,p2,c1,c2):
    #brute-force/találgatás
    pl1 = p1.split()
    pl2 = p2.split()
    #már itt átalakítom binárisra hhogy a xor muveletnél lehessen számolni
    """ p1_szavak_bin = list(binarisra(szo) for szo in pl1)
    p2_szavak_bin = list(binarisra(szo) for szo in pl2) """
    #print(p1_szavak_bin)
    #print(p2_szavak_bin)
    
    p1_kitalalt = ""
    p2_kitalalt = ""
    talalat = False
    
    kulcs = ""

    while not talalat:
        test = input("Találja ki az üzenet egy részletét: ")
        #test_bin = binarisra(test)

        """ for reszlet1,reszlet2 in zip(p1_szavak_bin,p2_szavak_bin):
            if test_bin == reszlet1:
                print(f"Első üzenet részlete: {test}")
                talalat = True
                p1_kitalalt = test
            if test_bin == reszlet2:
                print(f"Második üzenet részlete: {test}")
                talalat = True   
                p2_kitalalt = test
    
    print(f"kitalalt: {p1_kitalalt}")
    p1_kitalalt_bin = binarisra(p1_kitalalt)
    print(f"kitalalt_bin: {len(p1_kitalalt_bin)}")
    c1_bin = binarisra(c1)
    print(len(c1_bin))
    c1_bin_len_as_p1 = c1_bin[:len(p1_kitalalt_bin)] """
    """ 
    for c1,p1 in zip(c1_bin_len_as_p1,p1_kitalalt_bin):
        if c1 == p1 or p1 == c1:
            kulcs += '0'
        if c1 != p1 or p1 != c1:
            kulcs += '1' """

    
    return kulcs
#print(dekod2(uzenet1,uzenet2,rejt_uzenet1,rejt_uzenet2))


#kulcs(rész) = titkositott1(resz) + eredeti1(resz)
