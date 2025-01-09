import random

print("Alerte! A tous nos visiteurs, un animal s'est echappé de son enclos, veuillez evacuer Jurassic Park ")
input("Appuyez sur entrée pour continuer...")
print(r"""
                                / '.   .'\ 
                        .---.  <    > <    >  .---.
                        |    \  \ - ~ ~ - /  /    |
            _____          ..-~             ~-..-~
            |     |   \~~~\.'                    `./~~~/
        ---------   \__/                        \__/
        .'  O    \     /               /       \  
        _____,    `._.'               |         }  \/~~~/
        `----.          /            |        /    \__/
                `-.      |       /      |       /      `. ,~~|
                    ~-.__|      /_ - ~ ^|      /- _      `..-'   
                        |     /        |     /     ~-.     `-. _  _  _
                        |_____|        |_____|         ~ - . _ _ _ _ _> 
        """)
def jeudebase ():
    vie=50
    niveau_d=1
    max_dino=10
    monstre= random.randint(30,100)

    print("Un dinosaure se tient devant vous. Vous avez trois possibilités.")
    print("1. Vous échapper,2. Attaquer,3. Se soigner")

            
    while vie > 0 and niveau_d < max_dino:
            choix = int(input())
                    
            if choix == 1: #fuite
                print("Vous tentez de vous échapper...")
                chance = random.randint(1, 20)
                if chance >= 15:  # 25% de chance de réussir
                    print("Grace a vos",chance,"points de chance, vous avez réussi à vous échapper ! Tant mieux, puisqu'un autre dinosaure plus gros arrive. ")
                    niveau_d += 1
                    
                    print("Grace a votre chance extraordinaire, vous avez reussi a vous enfuir, et a tuer tous les dinosaures sur votre passage. GG")
                if niveau_d > max_dino:
                    break
                    break
                if chance ==20: 
                    print("Grace a votre chance extraordinaire, vous avez reussi a vous enfuir, et a tuer tous les dinosaures sur votre passage. GG")
                    break
                else:
                    print("A cause de vos",chance,"points de chance, le dinosaure vous rattrape et vous attaque !")
                #niveau 1
                if niveau_d ==1:         
                    attaque_d = random.randint(1,10)
                #niveau 2
                if niveau_d ==2:         
                    attaque_d = random.randint(2, 10)
                #niveau 3
                if niveau_d ==3:         
                    attaque_d = random.randint(3, 10)
                #niveau 4
                if niveau_d ==4:         
                    attaque_d = random.randint(4, 10)
                #niveau 5
                if niveau_d ==5:         
                    attaque_d = random.randint(5, 10)
                #niveau 6
                if niveau_d ==6:         
                    attaque_d = random.randint(6, 10)
                #niveau 7
                if niveau_d ==7:         
                    attaque_d = random.randint(7, 10)
                #niveau 8
                if niveau_d ==8:         
                    attaque_d = random.randint(8, 10)
                #niveau 9
                if niveau_d ==9:         
                    attaque_d = random.randint(9, 10)

                    vie -= attaque_d
                    print(f"Vous perdez {attaque_d} points de vie. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca devient urgent de vous soigner")
                    
            elif choix == 2: #Attaque
                #Niveau 1
                if niveau_d == 1:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)
                    attaque_d = random.randint(1, 10)
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                    
                #Niveau 2    
                if niveau_d == 2:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+5
                    attaque_d = random.randint(1, 10)+2
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                
                #Niveau 3    
                if niveau_d == 3:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+10
                    attaque_d = random.randint(1, 10)+3
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")

                #Niveau 4    
                if niveau_d == 4:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+15
                    attaque_d = random.randint(1, 10)+4
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")    
                
                #Niveau 5    
                if niveau_d == 5:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+20
                    attaque_d = random.randint(1, 10)+5
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                
                #Niveau 6    
                if niveau_d == 6:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+25
                    attaque_d = random.randint(1, 10)+6
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                
                #Niveau 7    
                if niveau_d == 7:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+30
                    attaque_d = random.randint(1, 10)+7
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                
                #Niveau 8    
                if niveau_d == 8:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+35
                    attaque_d = random.randint(1, 10)+8
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                
                #Niveau 9    
                if niveau_d == 9:
                    print("Vous attaquez le dinosaure !")
                    attaque_h = random.randint(1, 10)+40
                    attaque_d = random.randint(1, 10)+9
                    monstre -= attaque_h
                    vie -= attaque_d
                    print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre : {monstre}")
                    print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")
                    if vie <=10:
                        print("Attention, ca deviens urgent de vous soigner")
                
            elif choix == 3: #Soin
                print("Vous tentez de vous soigner.")
                soin = random.randint(5, 40)  
                vie += soin
                if vie > 50:  
                    vie = 50
                print(f"Vous récupérez {soin} points de vie. Vie restante : {vie}")
                #niveau 1
                if niveau_d ==1:         
                    attaque_d = random.randint(1,10)
                #niveau 2
                if niveau_d ==2:         
                    attaque_d = random.randint(2, 10)
                #niveau 3
                if niveau_d ==3:         
                    attaque_d = random.randint(3, 10)
                #niveau 4
                if niveau_d ==4:         
                    attaque_d = random.randint(4, 10)
                #niveau 5
                if niveau_d ==5:         
                    attaque_d = random.randint(5, 10)
                #niveau 6
                if niveau_d ==6:         
                    attaque_d = random.randint(6, 10)
                #niveau 7
                if niveau_d ==7:         
                    attaque_d = random.randint(7, 10)
                #niveau 8
                if niveau_d ==8:         
                    attaque_d = random.randint(8, 10)
                #niveau 9
                if niveau_d ==9:         
                    attaque_d = random.randint(9, 10)
                
                vie -= attaque_d
                print(f"Pendant que vous vous soignez, le dinosaure vous attaque et inflige {attaque_d} dégâts. Vie restante : {vie}")
                if vie <=10:
                    print("Attention, ca deviens urgent de vous soigner")
                    
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
            
    if vie <= 0:
        print("Vous avez perdu la bataille. Le dinosaure à gagné.")
    elif monstre <= 0:
        print("Bravo ! Vous avez vaincu le dinosaure !Vous avez gagné 5 d'XP,ce qui rajoute +5 a chacun de vos dégats")
        niveau_d += 1  # Passer au dinosaure suivant
        print("Tant mieux, puisqu'un autre apparait...")
    elif niveau_d > max_dino:
        print("Félicitations ! Vous avez vaincu tous les dinosaures et gagné le jeu !")
        print("Fin du jeu.")

jeudebase()