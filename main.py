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
    
    #kigyűjtöm a bekért adatok karaktereihez rendelt számot
    uzenet_szam = [betu_szamra.get(u, 0) for u in uzenet] 
    kulcs_szam = [betu_szamra.get(k, 0)for k in kulcs]

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
    
    #kigyűjtöm a bekért adatok karaktereihez rendelt számot
    kodolt_szam = [betu_szamra.get(u, 0)for u in kodolt]
    kulcs_szam = [betu_szamra.get(k, 0)for k in kulcs]

    #dekódolás
    uzenet_szam = []   
    lista_hossza = len(index)
    for u, k in zip(kodolt_szam, kulcs_szam):
        uzenet_kar_szam = (u-k) % lista_hossza
        uzenet_szam.append(uzenet_kar_szam)
   

    visszafejtett_uzenet = "".join(szam_beture.get(szam, "?") for szam in uzenet_szam)

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
#print(f"{rejt_uzenet1=}")
#print(f"{rejt_uzenet2=}")

p1_szavak = []
p2_szavak = []

def dekod2(p1,p2,c1,c2):
    #brute-force/találgatás
    pl1 = p1.split()
    #print(f"{pl1=}")
    pl2 = p2.split()
    #print(f"{pl2=}")
    
    p1_uzenet = []
    p2_uzenet = []
    kulcs = ""
    kulcs_reszlet_szamok = []  
    kulcs_karakterek = ["?"] * max(len(c1), len(c2))
    kulcs = "".join(kulcs_karakterek)
    lista_hossza = len(index)


    while  "?" in kulcs:
        kulcs_reszlet_szamok = []
        p1_kitalalt = ""
        p2_kitalalt = ""
        talalat_uzenet = 0 
        test = input("Találja ki az üzenet egy részletét: ").lower()
        
        while True:

            if test in p1:
                talalat_uzenet = 1
                p1_kitalalt = test
                if test not in p1_uzenet:
                    p1_uzenet.append(test)
                print(f"A szó részlet ({test}) az első üzenetben található")
                break

            elif test in p2:
                talalat_uzenet = 2
                p2_kitalalt = test
                if test not in p2_uzenet:
                    p2_uzenet.append(test)
                print(f"A szó részlet ({test}) a második üzenetben található")
                break

            else:
                print(f"A szó egyik üzenetben sem található. ")
                break
        
        if talalat_uzenet == 1:
            #A titkosított üzeneteket levágom ugyan olyan hosszúra mint az erediket
            c1_reszlet = c1[:len(p1_kitalalt)]
            
            #Kigyűjtöm a kitalált üzenet részletéhez rendelt számokat
            p1_kitalalt_szam = [betu_szamra.get(p1_szam, 0) for p1_szam in p1_kitalalt]  
            c1_reszlet_szam = [betu_szamra.get(c1_szam, 0) for c1_szam in c1_reszlet]

            #Kitalálom a kulcs részletet
            for c1_szam, p1_szam in zip(c1_reszlet_szam, p1_kitalalt_szam):
                kulcs_reszlet_szam = (c1_szam-p1_szam + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)
                    
            #Átalakítom a kulcs részlet számait betűkre
            kulcs_reszlet = "".join(szam_beture.get(k, "?") for k in kulcs_reszlet_szamok)
            #print(f"{kulcs_reszlet=}, {type(kulcs_reszlet)}")
            
            kulcs += kulcs_reszlet   
            #print(f"{kulcs=}, {type(kulcs)}")
            
            #visszafejtem p2-őt
            c2_reszlet = c2[:len(kulcs)]
            c2_reszlet_szam = [betu_szamra.get(c2_szam, 0) for c2_szam in c2_reszlet ]
            p2_reszlet_szamok = []

            for k_szam, c2_szam in zip(kulcs_reszlet_szamok, c2_reszlet_szam):
                p2_reszlet_szam = (c2_szam - k_szam + lista_hossza) % lista_hossza
                p2_reszlet_szamok.append(p2_reszlet_szam)

            p2_reszlet = "".join(szam_beture.get( num, "?") for num in p2_reszlet_szamok)
            p2_uzenet.append(p2_reszlet)


        elif talalat_uzenet == 2: 
            #A titkosított üzeneteket levágom ugyan olyan hosszúra mint az erediket   
            c2_reszlet = c2[:len(p2_kitalalt)]

            #Kigyűjtöm a kitalált üzenet részletéhez rendelt számokat
            p2_kitalalt_szam = [betu_szamra.get(p2_szam, 0) for p2_szam in p2_kitalalt]
            c2_reszlet_szam = [betu_szamra.get(c2_szam, 0) for c2_szam in c2_reszlet ]

            #Kitalálom a kulcs részletet      
            for c2_szam, p2_szam in zip(c2_reszlet_szam, p2_kitalalt_szam):
                kulcs_reszlet_szam = (c2_szam-p2_szam + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)

            #Átalakítom a kulcs részlet számait betűkre
            kulcs_reszlet = "".join(szam_beture.get(k_szam, "?") for k_szam in kulcs_reszlet_szamok)
            #print(f"{kulcs_reszlet=}, {type(kulcs_reszlet)}")
            kulcs += kulcs_reszlet
            #print(f"{kulcs=}, {type(kulcs)}")
            
            #Visszafejtem p1-et
            c1_reszlet = c1[:len(kulcs)]
            c1_reszlet_szam = [betu_szamra.get(c1_szam, 0) for c1_szam in c1_reszlet ]
            p1_reszlet_szamok = []

            for k_szam, c1_szam in zip(kulcs_reszlet_szamok, c1_reszlet_szam):
                p1_reszlet_szam = (c1_szam - k_szam + lista_hossza) % lista_hossza
                p1_reszlet_szamok.append(p1_reszlet_szam)

            p1_reszlet = "".join(szam_beture.get( num, "?") for num in p1_reszlet_szamok)
            p1_uzenet.append(p1_reszlet)

        print(f"{kulcs=}")
        print(f"{p1_uzenet=}")
        print(f"{p2_uzenet=}")

    return kulcs

print(dekod2(uzenet1,uzenet2,rejt_uzenet1,rejt_uzenet2))
