import sqlite3

# Connexion à la base de données
connection = sqlite3.connect("jeu_pythonosaure.db")
cursor = connection.cursor()

# Afficher les données des joueurs
print("Données des joueurs enregistrés :")
cursor.execute('SELECT * FROM joueurs')
joueurs = cursor.fetchall()

for joueur in joueurs:
    print(f"ID : {joueur[0]}, Nom : {joueur[1]}, Niveau atteint : {joueur[2]}, Armes : {joueur[3]}")

connection.close()