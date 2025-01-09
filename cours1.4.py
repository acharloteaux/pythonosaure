import random

print("Alerte! À tous nos visiteurs, un animal s'est échappé de son enclos. Veuillez évacuer Jurassic Park.")
input("Appuyez sur Entrée pour continuer...")
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

def jeudebase():
    vie = 50  # Vie initiale du joueur
    niveau_d = 1  # Niveau du dinosaure
    max_dino = 10  # Nombre maximum de dinosaures
    monstre = random.randint(30, 100)  # Points de vie du premier dinosaure

    print("Un dinosaure se tient devant vous. Vous avez trois possibilités.")
    print("1. Vous échapper, 2. Attaquer, 3. Se soigner")

    while vie > 0 and niveau_d <= max_dino:
        choix = input("Choisissez une action (1, 2 ou 3) : ")
        
        if choix == "1":  # Fuite
            print("Vous tentez de vous échapper...")
            chance = random.randint(-15, 5)
            if chance >= 0:  # 25% de chance de réussir
                print(f"Grâce à vos {chance} points de chance, vous avez réussi à vous échapper !")
                print("Un autre dinosaure apparaît...")
                niveau_d += 1
                monstre = random.randint(30, 100) + niveau_d * 10
                continue
            elif chance == 5:
                print("Grâce à votre chance extraordinaire, vous vous êtes enfuis tellement vite que vous avez effrayé tous les dinosaures qui se sont ranger tout seul dans leurs enclos ! GG.")
                break
            else:
                print(f"A cause de vos {chance} points de chance, le dinosaure vous rattrape et vous attaque !")
                attaque_d = random.randint(5, 15)
                vie -= attaque_d
                print(f"Vous perdez {attaque_d} points de vie. Vie restante : {vie}")

        elif choix == "2":  # Attaque
            print("Vous attaquez le dinosaure !")
            attaque_h = random.randint(5, 15) + 5 * (niveau_d - 1)
            attaque_d = random.randint(5, 15) + niveau_d
            monstre -= attaque_h
            vie -= attaque_d
            print(f"Vous infligez {attaque_h} dégâts au dinosaure. Vie du monstre restante : {monstre}")
            print(f"Le dinosaure vous inflige {attaque_d} dégâts. Vie restante : {vie}")

            if monstre <= 0:
                print(f"Bravo ! Vous avez vaincu le dinosaure de niveau {niveau_d} !")
                print("Vous gagnez 5 points d'XP et augmentez vos dégâts.")
                niveau_d += 1
                monstre = random.randint(30, 100) + niveau_d * 10
                print(f"Tant mieux, puisqu'un nouveau dinosaure de niveau {niveau_d} apparaît avec {monstre} points de vie !")

        elif choix == "3":  # Se soigner
            print("Vous tentez de vous soigner.")
            soin = random.randint(10, 30)
            vie += soin
            if vie > 50:  # Vie maximale
                vie = 50
            print(f"Vous récupérez {soin} points de vie. Vie restante : {vie}")

            # Le dinosaure attaque pendant le soin
            attaque_d = random.randint(5, 15) + niveau_d
            vie -= attaque_d
            print(f"Pendant que vous vous soignez, le dinosaure vous attaque et inflige {attaque_d} dégâts. Vie restante : {vie}")

        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
        
        if vie <= 0:
            print("Vous avez perdu la bataille. Les dinosaures ont gagnés.")
        elif niveau_d > max_dino:
            print("Félicitations ! Vous avez vaincu tous les dinosaures et gagné le jeu !")
            break

    print("Fin du jeu.")

jeudebase()
