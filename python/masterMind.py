import random


tableau =['A','B','C','D','E','F']
lettres_melangees = ''.join(random.sample(tableau, 4))
list(lettres_melangees)

print(lettres_melangees)

bp=0;
mp=0;
inv=0;
tour=12;
win=True;


while tour!=12 and win==False:
    player=input("Saisir votre combinaison ")
    if len(player) == 4 and player.isalpha():
        list(player)
        print(player.upper())
        for i in range(0, len(lettres_melangees)):
            for player[i] in lettres_melangees:
                if lettres_melangees[i]==player[i]:
                    bp+=1
                elif lettres_melangees[i] in player:
                    mp+=1
                    print(mp)     

                elif lettres_melangees[i] != player[i]:  
                    inv+=1      
    
    

    else:
     print("votre combinaison doit conetnir que 4 lettres")

print(bp)
print(inv)









                     
                     


      


         






        

        

  











