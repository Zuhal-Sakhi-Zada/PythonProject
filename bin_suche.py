import random

def liste():
    n=int(input("Länge der Liste: "))
    L=[]
    i=0
    while i<n:
        x=random.randint(1, 1000)
        if x not in L:
            L.append(x)
            i+=1
    L.sort()
    print(L)
    return L

def bin_suche(L, se, u, o):
    m = (u+o)//2
    print(u,m,o)
    input()
    if u==m or o==m:
        return("nicht enthalten")
    if se>L[m]:
        o=m
        return bin_suche(L,se,u,o)
    elif se<L[m]:
        u=m
        return bin_suche(L,se,u,o)
    elif se==L[m]:
        return m

print("Binäre Suche")
Liste=liste()
zahl=int(input("Welche Zahl soll gesucht werden? "))
print(bin_suche(liste, zahl, 0, len(Liste)-1))