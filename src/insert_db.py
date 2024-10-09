# src/insert_data.py

import sqlite3

def insert_client(id,nom, prenom, email, date_inscription):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO clients (id,nom, prenom, email, date_inscription)
            VALUES (?, ?, ?, ?,?)
        ''', (id,nom, prenom, email, date_inscription))
        conn.commit()
        print(f"Client {nom} {prenom} ajouté avec succès.")
    except sqlite3.IntegrityError as e:
        print(f"Erreur d'intégrité : {e}")
    finally:
        conn.close()

def insert_commande(id, client_id, date_commande, produit):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO commandes (id, client_id, date_commande, produit)
            VALUES (?, ?, ?,?,?)
        ''', (id,client_id, date_commande, produit))
        conn.commit()
        print(f"Commande pour le client ID {client_id} ajoutée avec succès.")
    except sqlite3.IntegrityError as e:
        print(f"Erreur d'intégrité : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Insertion de clients
    insert_client(1,"Dupont", "Jean", "jean.dupont@gmail.com", "2023-10-08")
    insert_client(2,"Martin", "Marie", "marie.martin@gmail.com","2023-06-08")
    insert_client(3,"Jam", "saad", "saad.jam@gmail.com","2023-05-08")

    # Insertion de commandes (en utilisant les ID des clients)
    insert_commande(1, 3,"2024-10-08", "Souris")
    insert_commande(2, 1,"2024-10-07", "Ordianteur")
