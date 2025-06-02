uzenet = 'helloworld'
abc = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

betu_indexre = dict(zip(abc, range(len(abc))))
index_beture = dict(zip(range(len(abc)), abc))

karakterek = []
for i in range(26):
    kod = chr(ord('a')+i)
    karakterek.append(kod)
#for karakter in karakterek:
    #print(karakter, end=",")

def rejtjelezes(uzenet, kulcs):
    #kulcsnak legalább akkorának kell lennie mint az üzenetnek
    #rejtjelezett üzenet n. karaktere az üzenet n. karakter kódja + kulcs n. karakter kódja
    #ha az eredmény nagyobb mint 26, akkor az eredmény a 27-el való osztás maradéka
    #ha a kulcs hosszabb mint az üzenet, akkor a rejtjeles üzenet hossza az üzenet hossza lesz
    kodolt = ""

    darabolas_uzenet = [uzenet[i:i + len(kulcs)] for i in range(0,len(uzenet), len(kulcs))]
    for darab in darabolas_uzenet:
        i = 0
        for betu in darab:
            szam = (betu_indexre[betu] + betu_indexre[kulcs[i]]) % len(abc)
            kodolt += index_beture[szam]
            i += 1
    
    return kodolt

print(rejtjelezes('helloworld', "abcdefgijkl"))