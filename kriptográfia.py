abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
index=[ 0 , 1 , 2 ,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

uzenet = input("Adjon meg egy Üzenetet: ")   #"helloworld" 

kulcs = input("Adjon meg egy kulcsot: ")    #"abcdefgijkl"
if len(kulcs) != len(uzenet):
    kulcs = input("Adjon meg egy kulcsot, egyenlő hossúságut az üzenettel: ")

uzenet_szam = [] 
kulcs_szam = []

def kodolas(uzenet, kulcs):
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

print(kodolas(uzenet,kulcs))