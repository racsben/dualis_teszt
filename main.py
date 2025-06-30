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

def szotar_betoltese(fajlnev="words.txt"):
    with open("words.txt", "r", encoding="utf-8") as f:
        szavak = {sor.strip() for sor in f if sor.strip()}

        darab_szo = {szo[:i] for szo in szavak for i in range(1, len(szo) + 1)}
    return szavak, darab_szo


SZAVAK, DARAB_SZO = szotar_betoltese()

def dekod2_auto(c1: str,c2: str): # 2 stringet kér be és egy listát ad vissza
    
    kulcsok = []        
    keres(c1, c2, "",kulcsok)
    print(kulcsok)
    return kulcsok

# Segéd függvény    
def keres(maradek_c1, maradek_c2, akt_kulcs, kulcsok):
        
    # Ha a végére értünk a szövegnek találtunk egy megoldást
    if len(maradek_c1) == 0 and len(maradek_c2) == 0:
        kulcsok.append(akt_kulcs)
        return   
        
    # Első feltétel
    for szo in SZAVAK:
        for p1_tipp in [szo + ' ', szo]:
            
            # Ha a szo kisebb a maradék üzenetben akkor visszafejtjük.
            if len(p1_tipp) <= len(maradek_c1):

                # Visszafejtjük a kulcs egy darabját
                c1_reszlet = maradek_c1[:len(p1_tipp)]
                kulcs_reszlet = dekodolas(c1_reszlet, p1_tipp)

                # A kapott kulcsdarabbal visszafejtjük a c2 egy darabját.
                c2_reszlet = maradek_c2[:len(p1_tipp)]
                p2_reszlet = dekodolas(c2_reszlet, kulcs_reszlet)

                
                # Ellenőrzés
                p2_utolso_szo = p2_reszlet.split(' ')[-1]
                
                jo_prefix = True
                if p2_reszlet.endswith(' '):
                    # Ha szóköz van a végén, a szónak benne kell lennie a szótárban.
                    if p2_utolso_szo not in SZAVAK:
                        jo_prefix = False
                else:
                    # Ha nincs szóköz, akkor egy létező szó elejének kell lennie.
                    if p2_utolso_szo not in DARAB_SZO:
                        jo_prefix = False


                if jo_prefix:
                    # Ha a szó jó, akkor halad tovább a függvény
                    keres(
                        maradek_c1[len(p1_tipp):],
                        maradek_c2[len(p1_tipp):],
                        akt_kulcs + kulcs_reszlet,
                        kulcsok
                        )
        