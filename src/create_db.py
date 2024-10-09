# src/create_db.py

import sqlite3

def create_database():
    # Connexion à la base de données SQLite 
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Création de la table "clients"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            date_inscription TEXT NOT NULL
        )
    ''')

    # Création de la table "commandes"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            date_commande TEXT NOT NULL,
            produit TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )
    ''')

    # Validation des changements et fermeture de la connexion
    conn.commit()
    conn.close()
    print("Base de données et tables créées avec succès.")

if __name__ == "__main__":
    create_database()
