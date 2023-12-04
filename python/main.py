import random

def generation_combinaison(longueur_combinaison, lettres_disponibles):
     return random.sample(lettres_disponibles, longueur_combinaison)

def verifier_combinaison(solution, tentative):
    bien_places = mal_places = invalide= 0
    for i in range(len(solution)):
        if solution[i] == tentative[i]:
            bien_places += 1
    
        elif solution[i] != tentative[i]:
            mal_places +=1  
        
        elif solution[i]  not in tentative:
            invalide += 1  
    return bien_places, mal_places, invalide

def afficher_resultat( bien_places, mal_places, invalide):
    print(f"Lettes bien placées : {bien_places}, Lettres mal placées : {mal_places}")
    print(f"Lettres invalides: {invalide}")

               

def masterMind():
    longueur_combinaison=4
    lettres_disponibles=['A','B','C','D','E','F']
    solution=generation_combinaison(longueur_combinaison, lettres_disponibles)


    tour_max = 12
    print("Bienvenue dans le Mastermind!")
    print(f"Vous avez {tour_max} tentatives pour deviner la combinaison.")
    print(f"La combinaison contient {longueur_combinaison} lettres parmi {lettres_disponibles}")
    print(solution)


    for nbr_tour in range(1, tour_max + 1):
        print(f"\nTentative {nbr_tour}/{tour_max}")
        tentative = input("Entrez votre combinaison : ").upper()
        if tentative.isalpha():

            if len(tentative) != longueur_combinaison or any(l not in lettres_disponibles for l in tentative):
                print("Veuillez entrer une combinaison valide.")
                continue

            bien_places = mal_places = invalide= 0
            for i in range(len(solution)):
                if solution[i] == tentative[i]:
                    bien_places += 1
            
                elif solution[i] != tentative[i]:
                    mal_places +=1  
                
                elif solution[i]  not in tentative:
                    invalide += 1  
        
            afficher_resultat(mal_places, bien_places, invalide)        
            if bien_places == longueur_combinaison:
                print("Félicitations! Vous avez trouvé la combinaison.")
                break
        else:
            print("Veuillez entrer que des lettres")
    else:
        print(f"Désolé, vous avez atteint le nombre maximal de tentatives. La combinaison était {solution}.")

if __name__ == "__main__":
    masterMind()        
