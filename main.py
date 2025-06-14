import random
import os

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
index=[ 0 , 1 , 2 ,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

betu_szamra = {betu: szam for betu, szam in zip(abc,index)}
szam_beture = {szam: betu for betu, szam in zip(abc,index)}

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
   
    visszafejtett_uzenet = ""
    for k in uzenet_szam:
        for betu,szam in zip(abc,index):
            if k == szam:
                visszafejtett_uzenet += betu

    return visszafejtett_uzenet

#2

def dekod2(c1,c2):
    #brute-force/találgatás
    p1_uzenet = []
    p2_uzenet = []
    
    kulcs = []
    kulcs_reszlet_szamok = []  
    kulcs_karakterek = ["?"] * max(len(c1), len(c2))
    kulcs = "".join(kulcs_karakterek)
    
    lista_hossza = len(index)
    
    c1_levagott = c1
    c2_levagott = c2
    c1_kuka = ""
    c2_kuka = ""

    while  "?" in kulcs_karakterek:
        
        p_felteteles = ""
        talalat_uzenet = 0 
        
        print(f"{c1_kuka=}")
        print(f"{c2_kuka=}")
        try:
            melyik = int(input("Melyik üzenetben szeretne találgatni?: (1-es: első üzenet/2-es: második üzenet) "))
        except ValueError:
            print("1-est vagy 2-est adjon meg!")
            continue
        
        #elso uzenet
        kulcs_reszlet_szamok = []
        if melyik == 1:  

            test = input("Találja ki az üzenet egy részletét: ").lower()
            p_felteteles = test

            #A titkosított üzeneteket levágom ugyan olyan hosszúra mint a kitaláltat
            c1_reszlet = c1_levagott[:len(p_felteteles)]
                
            #Kigyűjtöm a kitalált üzenet részletéhez rendelt számokat
            p1_kitalalt_szam = [betu_szamra.get(p1_szam, 0) for p1_szam in p_felteteles]  
            c1_reszlet_szam = [betu_szamra.get(c1_szam, 0) for c1_szam in c1_reszlet]
            
            
            #Kitalálom a kulcs részletet
            for c1_szam, p1_szam in zip(c1_reszlet_szam, p1_kitalalt_szam):
                kulcs_reszlet_szam = (c1_szam-p1_szam + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)
                        

            #----?-ek cseréje
            for i , num in enumerate(kulcs_reszlet_szamok):
                if i < max(len(c1),len(c2)):
                    kar = kulcs_karakterek[i]
                    uj_kar = szam_beture.get(num, "?")
                    if kar == "?" or uj_kar != "?":
                        kulcs_karakterek[i] = uj_kar

            #Átalakítom a kulcs részlet számait betűkre
            kulcs = "".join(kulcs_karakterek)
            #print(f"{kulcs_reszlet=}, {type(kulcs_reszlet)}")
            
            #visszafejtem p2-őt
            c2_reszlet = c2[:len(p_felteteles)]
            c2_reszlet_szam = [betu_szamra.get(c2_szam, 0) for c2_szam in c2_reszlet ]
            
            p2_reszlet_szamok = []

            for k_szam, c2_szam in zip(kulcs_reszlet_szamok, c2_reszlet_szam):
                p2_reszlet_szam = (c2_szam - k_szam + lista_hossza) % lista_hossza
                p2_reszlet_szamok.append(p2_reszlet_szam)

            p2_reszlet = "".join(szam_beture.get( num, "?") for num in p2_reszlet_szamok)
            p2_uzenet.append(p2_reszlet)
            
            print(f"{p2_uzenet=}")
            print(f"{kulcs=}")
            
            #kezeljük a valódiságát a szövegnek
            ertelmes = input("Elégedett vagy az üzenet szövegével? (nem/igen) ").lower()
            if ertelmes == "igen":
                c1_levagott = c1[len(p_felteteles):]
                print(f"{c1_levagott=}")
                c1_kuka += c1_reszlet

                c2_levagott = c2[len(p2_reszlet):]
                print(f"{c2_levagott=}")
                c2_kuka += c2_reszlet
                continue

            if ertelmes == "nem":
                c1_kuka= ""
                print(f"{c1_kuka}")
                c1_levagott = c1
                print(f"{c1_levagott}")

                c2_kuka = ""
                print(f"{c2_kuka}")
                c2_levagott = c2
                print(f"{c2_levagott}")
                
                p_felteteles = ""
                p2_uzenet = []
                kulcs = []
                kulcs_reszlet_szamok = []  
                kulcs_karakterek = ["?"] * max(len(c1), len(c2))
                kulcs = "".join(kulcs_karakterek)
                continue
        
        
        #masodik uzenet
        if melyik == 2:
            test = input("Találja ki az üzenet egy részletét: ").lower()
            p_felteteles = test
            #A titkosított üzeneteket levágom ugyan olyan hosszúra mint az erediket   
            c2_reszlet = c2_levagott[:len(p_felteteles)]

            #Kigyűjtöm a kitalált üzenet részletéhez rendelt számokat
            p2_kitalalt_szam = [betu_szamra.get(p2_szam, 0) for p2_szam in p_felteteles]
            c2_reszlet_szam = [betu_szamra.get(c2_szam, 0) for c2_szam in c2_reszlet ]

            
            #Kitalálom a kulcs részletet      
            for c2_szam, p2_szam in zip(c2_reszlet_szam, p2_kitalalt_szam):
                kulcs_reszlet_szam = (c2_szam-p2_szam + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)

            #Átalakítom a kulcs részlet számait betűkre
            for i , num in enumerate(kulcs_reszlet_szamok):
                if i < max(len(c1),len(c2)):
                    kar = kulcs_karakterek[i]
                    uj_kar = szam_beture.get(num, "?")
                    if kar == "?" or uj_kar != "?":
                        kulcs_karakterek[i] = uj_kar

            #Átalakítom a kulcs részlet számait betűkre
            kulcs = "".join(kulcs_karakterek)
                
            #Visszafejtem p1-et
            c1_reszlet = c1[:len(kulcs)]
            c1_reszlet_szam = [betu_szamra.get(c1_szam, 0) for c1_szam in c1_reszlet ]
            
            p1_reszlet_szamok = []

            for k_szam, c1_szam in zip(kulcs_reszlet_szamok, c1_reszlet_szam):
                p1_reszlet_szam = (c1_szam - k_szam + lista_hossza) % lista_hossza
                p1_reszlet_szamok.append(p1_reszlet_szam)

            p1_reszlet = "".join(szam_beture.get( num, "?") for num in p1_reszlet_szamok)
            p1_uzenet.append(p1_reszlet)

            print(f"{p1_uzenet=}")
            print(f"{kulcs=}")
            #kezeljük a valódiságát a szövegnek
            ertelmes = input("Elégedett vagy az üzenet szövegével? (nem/igen) ").lower()
            if ertelmes == "igen":
                c2_levagott = c2[len(p_felteteles):]
                print(f"{c2_levagott=}")
                c2_kuka += c2_reszlet

                c1_levagott = c1[len(p_felteteles):]
                print(f"{c1_levagott}")
                c1_kuka += c1_reszlet
                continue

            if ertelmes == "nem":
                c2_levagott = c2
                print(f"{c2_levagott=}")
                c2_kuka =""

                c1_levagott = c1
                print(f"{c1_levagott=}")
                c1_kuka = "" 
                
                p_felteteles = ""
                p1_uzenet = []
                kulcs = []
                kulcs_reszlet_szamok = []  
                kulcs_karakterek = ["?"] * max(len(c1), len(c2))
                kulcs = "".join(kulcs_karakterek)
                continue

    return kulcs

