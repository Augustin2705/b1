
def mediane (liste, a):
    if sorted(liste):
        a = sorted(liste)
        print(a)
        if len(a)%2 ==0:
            moitie = len(a)/2
            a1 =a[:moitie] 
            a2= a[moitie:]
            milieu= (a1[max]/2) + (a2[max]/2)
            return milieu
        

       
    elif (liste):
        print("trie la liste")
            



l1=[1,2,3,4,]
mediane(l1)
# l2=[2,7,9,10,3]


# mediane(l2)