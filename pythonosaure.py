import sqlite3
import random
from colorama import Fore, Style, init

# Connexion à la base de données
connection = sqlite3.connect("jeu_pythonosaure.db")
cursor = connection.cursor()

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
prenom = input("Entrez votre prénom : ")
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
def jeudebase(prenom):
    vie = 50
    niveau_d = 1
    max_dino = 10
    monstre = random.randint(30, 100)
    degats_bonus = 0
    arme_equipé = []
    arme = [
        {"nom": "Épée", "degats": 10},
        {"nom": "Hache", "degats": 15},
        {"nom": "Arc", "degats": 8},
        {"nom": "Lance", "degats": 7},
        {"nom": "Bâton", "degats": 1},
        {"nom": "Doudou", "degats": -2}
    ]
    chance_loot = 5

    print("Un dinosaure se tient devant vous. Vous avez trois possibilités.")
    print("1. Vous échapper, 2. Attaquer, 3. Se soigner")

    while vie > 0 and niveau_d <= max_dino:
        if niveau_d >= 2:
            print("i pour ouvrir l'inventaire")

        choix = input("Choisissez une action (1, 2, 3) : ")

        if choix == "1":
            print("Vous tentez de vous échapper...")
            chance = random.randint(1, 20)
            if chance >= 15:
                print(f"Grâce à vos {VERT_CLAIR}{chance}{Fore.RESET} points de chance, vous avez réussi à vous échapper !")
                print("Un autre dinosaure apparaît...")
                niveau_d += 1
                if niveau_d > max_dino:
                    break
                monstre = random.randint(30, 100) + niveau_d * 10
            elif chance == 20:
                print(f"Grâce à votre chance extraordinaire de {VERT_CLAIR}{chance}{Fore.RESET}, vous avez tué tous les dinosaures ! GG.")
                break
            else:
                print(f"A cause de vos {VERT_CLAIR}{chance}{Fore.RESET} points de chance, le dinosaure vous rattrape et vous attaque !")
                attaque_d = random.randint(5, 15)
                vie -= attaque_d
                print(f"Vous perdez {ROUGE}{attaque_d}{Fore.RESET} points de vie. Vie restante : {ROUGE}{vie}{Fore.RESET}/50")

        elif choix == "2":
            print("Vous attaquez le dinosaure !")
            attaque_h = random.randint(5, 15) + degats_bonus + 5 * (niveau_d - 1)
            attaque_d = random.randint(5, 15) + niveau_d
            monstre -= attaque_h
            vie -= attaque_d
            print(f"Vous infligez {ROSE}{attaque_h}{Fore.RESET} dégâts au dinosaure. Vie du monstre restante : {JAUNE}{monstre}{Fore.RESET}")
            print(f"Le dinosaure vous inflige {ORANGE}{attaque_d}{Fore.RESET} dégâts. Vie restante : {ROUGE}{vie}{Fore.RESET}/50")

            if monstre <= 0:
                print(f"{BLEU_CLAIR}Bravo ! Vous avez vaincu le dinosaure de niveau {JAUNE}{niveau_d}{Fore.RESET} !")
                niveau_d += 1
                if niveau_d > max_dino:
                    break
                monstre = random.randint(30, 100) + niveau_d * 10

        elif choix == "3":
            print("Vous tentez de vous soigner.")
            soin = random.randint(10, 30)
            vie += soin
            if vie > 50:
                vie = 50
            print(f"Vous récupérez {ROUGE}{soin}{Fore.RESET} points de vie. Vie restante : {ROUGE}{vie}{Fore.RESET}")

        elif choix == "i" and niveau_d >= 2:
            print(f"Inventaire :")
            if arme_equipé:
                for arme in arme_equipé:
                    print(f" - {ROSE}{arme}{Fore.RESET}")
            if random.randint(1, 100) <= chance_loot:
                nouvelle_arme = random.choice(arme)
                arme_equipé.append(nouvelle_arme["nom"])
                degats_bonus += nouvelle_arme["degats"]
                print(f"Incroyable ! Vous trouvez une arme : {ROSE}{nouvelle_arme['nom']}{Fore.RESET} ! Vos dégâts augmentent de {ROSE}{nouvelle_arme['degats']}{Fore.RESET} points.")
                chance_loot = 5
            else:
                chance_loot += 5
                print(f"Vous n'avez pas trouvé de nouvelle arme. Au prochain niveau, vous avez {VERT_CLAIR}{chance_loot}%{Fore.RESET} de chance de trouver une arme.")
            continue

        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3 ")

        if vie <= 0:
            print(f"{BLEU}Vous avez perdu la bataille. Le dinosaure a gagné.{Fore.RESET}")
            armes_str = ", ".join(arme_equipé) if arme_equipé else "Aucune"
            cursor.execute('''
                INSERT INTO joueurs (nom, niveau_perdu, armes)
                VALUES (?, ?, ?)
            ''', (prenom, niveau_d, armes_str))
            connection.commit()
            print(f"Les données de {prenom} ont été sauvegardées.")
            break

        elif niveau_d > max_dino:
            print(f"{BLEU_CLAIR}Félicitations ! Vous avez vaincu tous les dinosaures et gagné le jeu !{Fore.RESET}")
            armes_str = ", ".join(arme_equipé) if arme_equipé else "Aucune"
            cursor.execute('''
                INSERT INTO joueurs (nom, niveau_perdu, armes)
                VALUES (?, ?, ?)
            ''', (prenom, niveau_d, armes_str))
            connection.commit()
            print(f"Les données de {prenom} ont été sauvegardées.")
            break

    print("Fin du jeu")

while True:
    jeudebase(prenom)
    rejouer = input("Voulez-vous rejouer ? (oui / non) : ").lower()
    if rejouer != "oui":
        print("Merci d'avoir joué ! À bientôt.")
        break
