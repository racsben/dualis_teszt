import random
import os

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
index=[ 0 , 1 , 2 ,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# Betűk-számra, Számok-betűre váltásának kezelése
betu_szamra = {betu: szam for betu, szam in zip(abc,index)}
szam_beture = {szam: betu for betu, szam in zip(abc,index)}

def kodolas(uzenet, kulcs):
    
    # Kigyűjtöm a bekért adatok karaktereihez rendelt számot
    uzenet_szam = [betu_szamra.get(u, 0) for u in uzenet] 
    kulcs_szam = [betu_szamra.get(k, 0)for k in kulcs]

    # Kódolt üzenet kialakítása
    kodolt = ""  
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

def dekodolas(kodolt,kulcs): # 2 stringet kér be és stringet ad vissza
    
    # Kigyűjtöm a bekért adatok karaktereihez rendelt számot
    kodolt_szam = [betu_szamra.get(u, 0)for u in kodolt]
    kulcs_szam = [betu_szamra.get(k, 0)for k in kulcs]

    # Dekódolás
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

mind = []
with open("words.txt", "r", encoding="utf-8") as f:
    for sor in f:
        szo = sor.strip()
        if szo:
            mind.append(szo)

def dekod2_auto(c1: str,c2: str): # 2 stringet kér be és egy listát ad vissza
    
    kulcsok = []

    p1_uzenet = ""
    p2_uzenet = ""
    
    lista_hossza = len(index)
    
    # Változók, stringek könnyebb kezelése érdekében
    c1_levagott = c1
    c2_levagott = c2
    c1_kuka = ""
    c2_kuka = ""
        
    
    p_felteteles = ""
    kulcs_kesz = ""
    #brute-force
    while len(kulcs_kesz) != min(len(c1), len(c2)):
        for szo in mind:
            kulcs_reszlet_szamok = []
            
            p_felteteles = szo

            # A titkosított üzeneteket levágom ugyanolyan hosszúra mint a kitaláltat
            c1_reszlet = c1_levagott[:len(p_felteteles)]
                
            # Kigyűjtöm a feltételezett szóhoz rendelt számokat
            p1_kitalalt_szam = [betu_szamra.get(p1_szam, 0) for p1_szam in p_felteteles]  
            c1_reszlet_szam = [betu_szamra.get(c1_szam, 0) for c1_szam in c1_reszlet]
                
                
            # Kitalálom a kulcs részletet
            for c1_szam, p1_szam in zip(c1_reszlet_szam, p1_kitalalt_szam):
                kulcs_reszlet_szam = (c1_szam-p1_szam + lista_hossza) % lista_hossza
                kulcs_reszlet_szamok.append(kulcs_reszlet_szam)

            # Átalakítom a kulcs részlet számait betűkre
            kulcs = "".join(szam_beture.get(k,"?")for k in kulcs_reszlet_szamok)

            # Visszafejtem p2-őt
            c2_reszlet = c2_levagott[:len(p_felteteles)]
            c2_reszlet_szam = [betu_szamra.get(num2, 0) for num2 in c2_reszlet ]
                
            p2_reszlet_szamok = []

            for k_szam, c2_szam in zip(kulcs_reszlet_szamok, c2_reszlet_szam):
                p2_reszlet_szam = (c2_szam - k_szam + lista_hossza) % lista_hossza
                p2_reszlet_szamok.append(p2_reszlet_szam)

            p2_reszlet = "".join(szam_beture.get( num, "?") for num in p2_reszlet_szamok)
            
            # Kezeljük, hogy helyes-e a feltételezett szó
            if p2_reszlet in mind:
                p2_uzenet += p2_reszlet
                p1_uzenet += p_felteteles

                c1_levagott = c1_levagott[len(c1_reszlet):]
                c1_kuka += c1_reszlet

                kulcs_kesz += kulcs
                
                c2_levagott = c2_levagott[len(c2_reszlet):]
                c2_kuka += c2_reszlet
                continue
            
            p2_reszlet = ""
        if p2_reszlet not in mind:  
            print("Nem találtam megfelelő szegmenst. A megfejtés elakadt.")
            continue

    print(p1_uzenet)
    print(p2_uzenet)
    return kulcs_kesz