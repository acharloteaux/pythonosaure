import sqlite3

# Connexion à la base de données
connection = sqlite3.connect("jeu_pythonosaure.db")
cursor = connection.cursor()

# Supprimer l'ancienne table (facultatif si elle existe déjà)
cursor.execute('DROP TABLE IF EXISTS joueurs')

# Créer la table `joueurs`
cursor.execute('''
    CREATE TABLE IF NOT EXISTS joueurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        niveau_perdu INTEGER NOT NULL,
        armes TEXT  -- Liste des armes trouvées, séparées par des virgules
    )
''')

connection.commit()
connection.close()

print("Base de données initialisée avec succès !")