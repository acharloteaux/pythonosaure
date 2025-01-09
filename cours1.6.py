import random
from colorama import Fore, Style, init

# Initialisation de colorama pour Windows et toutes plateformes
init(autoreset=True)

# Couleurs
VERT_FONCE = "\033[32m"
ROUGE = Fore.RED
JAUNE = Fore.YELLOW
ORANGE = Style.DIM + Fore.YELLOW
BLEU = Fore.BLUE
VERT_CLAIR = "\033[92m"
ROSE = Fore.MAGENTA
BLEU_CLAIR = Fore.CYAN

# Affichage initial
print("\nAlerte! À tous nos visiteurs, un animal s'est échappé de son enclos. Veuillez évacuer Jurassic Park.")
input("Appuyez sur Entrée pour continuer...")
print(VERT_FONCE + r"""
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

# Fonction principale du jeu
def jeudebase():
    vie = 50  # Vie initiale du joueur
    niveau_d = 1  # Niveau du dinosaure
    max_dino = 10  # Nombre maximum de dinosaures
    monstre = random.randint(30, 100)  # Points de vie du premier dinosaure
    degats_bonus = 0  # Bonus de dégâts si une arme est trouvée
    chance_loot = 5  # Pourcentage de chance initial pour looter une arme

    print("Un dinosaure se tient devant vous. Vous avez trois possibilités.")
    print("1. Vous échapper, 2. Attaquer, 3. Se soigner")

    while vie > 0 and niveau_d <= max_dino:
        choix = input("Choisissez une action (1, 2 ou 3) : ")
        
        if choix == "1":  # Fuite
            print("Vous tentez de vous échapper...")
            chance = random.randint(1, 20)
            if chance >= 15:  # 25% de chance de réussir
                print(f"Grâce à vos {VERT_CLAIR}{chance}{Fore.RESET} points de chance, vous avez réussi à vous échapper !")
                print("Un autre dinosaure apparaît...")
                niveau_d += 1
                if niveau_d > max_dino:
                    break
                monstre = random.randint(30, 100) + niveau_d * 10  # Nouveau dinosaure

                # Vérifier si une arme est trouvée
                if random.randint(1, 100) <= chance_loot:  # Probabilité actuelle
                    print(f"Incroyable ! Vous trouvez une arme ! Vos dégâts augmentent de {ROSE}10{Fore.RESET} points.")
                    print(f"Votre chance de trouver une arme repasse à {VERT_CLAIR}{chance_loot}%{Fore.RESET} au prochain niveau.")
                    degats_bonus += 10
                    chance_loot = 5  # Réinitialisation du pourcentage
                else:
                    chance_loot += 5  # Augmentation progressive
                    print(f"Vous n'avez pas trouvé d'arme. Au prochain niveau, vous avez {VERT_CLAIR}{chance_loot}%{Fore.RESET} de chance de trouver une arme.")
                continue
            elif chance == 20:
                print(f"Grâce à votre chance extraordinaire de {VERT_CLAIR}{chance}{Fore.RESET}, vous avez tué tous les dinosaures ! GG.")
                break
            else:
                print(f"A cause de vos {VERT_CLAIR}{chance}{Fore.RESET} points de chance, le dinosaure vous rattrape et vous attaque !")
                attaque_d = random.randint(5, 15)
                vie -= attaque_d
                print(f"Vous perdez {ROUGE}{attaque_d}{Fore.RESET} points de vie. Vie restante : {ROUGE}{vie}{Fore.RESET}")

        elif choix == "2":  # Attaque
            print("Vous attaquez le dinosaure !")
            attaque_h = random.randint(5, 15) + degats_bonus + 5 * (niveau_d - 1)
            attaque_d = random.randint(5, 15) + niveau_d
            monstre -= attaque_h
            vie -= attaque_d
            print(f"Vous infligez {ROSE}{attaque_h}{Fore.RESET} dégâts au dinosaure. Vie du monstre restante : {JAUNE}{monstre}{Fore.RESET}")
            print(f"Le dinosaure vous inflige {ORANGE}{attaque_d}{Fore.RESET} dégâts. Vie restante : {ROUGE}{vie}{Fore.RESET}")

            if monstre <= 0:
                print(f"{BLEU_CLAIR}Bravo ! Vous avez vaincu le dinosaure de niveau {JAUNE}{niveau_d}{Fore.RESET} !")
                niveau_d += 1
                if niveau_d > max_dino:
                    break
                monstre = random.randint(30, 100) + niveau_d * 10

                # Vérifier si une arme est trouvée
                if random.randint(1, 100) <= chance_loot:  # Probabilité actuelle
                    print(f"Incroyable ! Vous trouvez une arme ! Vos dégâts augmentent de {ROSE}10{Fore.RESET} points.")
                    degats_bonus += 10
                    chance_loot = 5  # Réinitialisation du pourcentage
                else:
                    chance_loot += 5  # Augmentation progressive
                    print(f"Vous n'avez pas trouvé d'arme. Au prochain niveau, vous avez {VERT_CLAIR}{chance_loot}%{Fore.RESET} de chance de trouver une arme.")
                print(f"Un nouveau dinosaure de niveau {JAUNE}{niveau_d}{Fore.RESET} apparaît avec {JAUNE}{monstre}{Fore.RESET} points de vie !")

        elif choix == "3":  # Se soigner
            print("Vous tentez de vous soigner.")
            soin = random.randint(10, 30)
            vie += soin
            if vie > 50:  # Vie maximale
                vie = 50
            print(f"Vous récupérez {ROUGE}{soin}{Fore.RESET} points de vie. Vie restante : {ROUGE}{vie}{Fore.RESET}")

            # Le dinosaure attaque pendant le soin
            attaque_d = random.randint(5, 15) + niveau_d
            vie -= attaque_d
            print(f"Pendant que vous vous soignez, le dinosaure vous attaque et inflige {ORANGE}{attaque_d}{Fore.RESET} dégâts. Vie restante : {ROUGE}{vie}{Fore.RESET}")

        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
        
        if vie <= 0:
            print(f"{BLEU}Vous avez perdu la bataille. Le dinosaure a gagné.{Fore.RESET}")
        elif niveau_d > max_dino:
            print(f"{BLEU_CLAIR}Félicitations ! Vous avez vaincu tous les dinosaures et gagné le jeu !{Fore.RESET}")
            break

    print("Fin du jeu.")

# Boucle pour rejouer
while True:
    jeudebase()

    rejouer = input("Voulez-vous rejouer ? (oui / non) : ").lower()
    if rejouer != "oui":
        print("Merci d'avoir joué ! À bientôt.")
        break
