import random
import os

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
index=[ 0 , 1 , 2 ,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

betu_szamra = {betu: szam for betu, szam in zip(abc,index)}
szam_beture = {szam: betu for betu, szam in zip(abc,index)}
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
print(f"{uzenet1=}")
uzenet2 = ' '.join(uzenetl2)
print(f"{uzenet2=}")


#----------Kulcs generálása-----------------
length = len(uzenet1)
kulcs2 = ''.join(random.choices(abc , k=length))
print(f"{kulcs2=}")
#Kódolom az üzeneteket
rejt_uzenet1 = kodolas(uzenet1,kulcs2)
rejt_uzenet2 = kodolas(uzenet2,kulcs2)
print(f"{rejt_uzenet1=}")
print(f"{rejt_uzenet2=}")

p1_szavak = []
p2_szavak = []

def dekod2(p1,p2,c1,c2):
    #brute-force/találgatás
    pl1 = p1.split()
    #print(f"{pl1=}")
    pl2 = p2.split()
    #print(f"{pl2=}")
    
    p1_kitalalt = ""
    p2_kitalalt = ""
    p1_uzenet = []
    p2_uzenet = []
    talalat_uzenet = 0 
    if talalat_uzenet == 1:
        kulcs = dekod_p1()
    if talalat_uzenet == 2:
        kulcs = dekod_p2()
    kulcs_reszlet_szamok = []  
    lista_hossza = len(index)

    while True:
        test = input("Találja ki az üzenet egy részletét: ")

        if test in pl1:
            talalat_uzenet = 1
            p1_kitalalt = test
            print(f"A szó részlet ({test}) az első üzenetben található")
            break

        if test in pl2:
            talalat_uzenet = 2
            p2_kitalalt = test
            print(f"A szó részlet ({test}) a második üzenetben található")
            break

        if test not in pl1 and test not in pl2:
            print(f"A szó egyik üzenetben sem található. ")
    if talalat_uzenet == 1:
        def dekod_p1():
            #A titkosított üzeneteket levágom ugyan olyan hosszúra mint az erediket
            c1_reszlet = c1[:len(p1_kitalalt)]
            
            #Kigyűjtöm a kitalált üzenet részletéhez rendelt számokat
            p1_kitalalt_szam = [betu_szamra.get(p1, 0) for p1 in p1_kitalalt]  
            c1_reszlet_szam = [betu_szamra.get(c1, 0) for c1 in c1_reszlet]

            #Kitalálom a kulcs részletet
            for c1, p1 in zip(c1_reszlet_szam, p1_kitalalt_szam):
                kulcs_reszlet_szam = (c1-p1 + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)
                
            #Átalakítom a kulcs részlet számait betűkre
            kulcs_reszlet = "".join(szam_beture.get(k, 0) for k in kulcs_reszlet_szamok)
            

            #visszafejtem p2-őt
            c2_reszlet = c2[:len(kulcs)]
            c2_reszlet_szam = [betu_szamra.get(c2,0) for c2 in c2_reszlet ]
            p2_reszlet_szamok = []

            for k, c2 in zip(kulcs_reszlet_szamok, c2_reszlet_szam):
                p2_reszlet_szam = (c2 - k + lista_hossza) % lista_hossza
                p2_reszlet_szamok.append(p2_reszlet_szam)

            p2_reszlet = "".join(szam_beture.get( num, "?") for num in p2_reszlet_szamok)
            p2_uzenet.append(p2_reszlet)

            return kulcs_reszlet

    if talalat_uzenet == 2: 
        def dekod_p2():
            #A titkosított üzeneteket levágom ugyan olyan hosszúra mint az erediket   
            c2_reszlet = c2[:len(p2_kitalalt)]

            #Kigyűjtöm a kitalált üzenet részletéhez rendelt számokat
            p2_kitalalt_szam = [betu_szamra.get(p2, 0) for p2 in p2_kitalalt]
            c2_reszlet_szam = [betu_szamra.get(c2,0) for c2 in c2_reszlet ]

            #Kitalálom a kulcs részletet      
            for c2, p2 in zip(c2_reszlet_szam, p2_kitalalt_szam):
                kulcs_reszlet_szam = (c2-p2 + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)

            #Átalakítom a kulcs részlet számait betűkre
            kulcs_reszlet = "".join(szam_beture.get(k, 0) for k in kulcs_reszlet_szamok)
            

            #Visszafejtem p1-et
            c1_reszlet = c1[:len(kulcs)]
            c1_reszlet_szam = [betu_szamra.get(c1,0) for c1 in c1_reszlet ]
            p1_reszlet_szamok = []

            for k, c1 in zip(kulcs_reszlet_szamok, c1_reszlet_szam):
                p1_reszlet_szam = (c1 - k + lista_hossza) % lista_hossza
                p1_reszlet_szamok.append(p1_reszlet_szam)

            p1_reszlet = "".join(szam_beture.get( num, "?") for num in p1_reszlet_szamok)
            p1_uzenet.append(p1_reszlet)
            return kulcs_reszlet
        
    dekod_p2()
    if kulcs:
        while len(''.join(p1_uzenet)) != len(p1):
            print(" ".join(p1_uzenet))
            tipp = input("Találja ki az üzenet egy további részletét:")
            p1_kitalalt = tipp
    return ' '.join(p1_uzenet)
    
print(dekod2(uzenet1,uzenet2,rejt_uzenet1,rejt_uzenet2))
