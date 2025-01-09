import random

def jeu ():
    print("Je vais choisir un nombre entre 1 et 50. À vous de deviner !")

nombre_a_deviner = random.randint(1, 1000)
essais = 0


while essais <= 9:
            proposition = int(input("Entrez votre proposition : "))
            essais += 1
            
            if proposition < nombre_a_deviner:
                print("Le nombre à deviner est plus grand.")
            elif proposition > nombre_a_deviner:
                print("Le nombre à deviner est plus petit.")
            else:
                print(f"Bravo ! Vous avez trouvé le juste prix en {essais} essais.")
                break

if essais > 9:
    print("Vous avez fait 10 essais, perdu, le nombre a trouvé été",nombre_a_deviner)