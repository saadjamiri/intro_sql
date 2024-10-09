# src/query_data.py

import sqlite3

def recup_clients():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()

    print("Clients dans la base de données :")
    for client in clients:
        print(client)

    conn.close()

def recup_commandes():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM commandes')
    commandes = cursor.fetchall()

    print("\nCommandes dans la base de données :")
    for commande in commandes:
        print(commande)

    conn.close()

if __name__ == "__main__":
    recup_clients()
    recup_commandes()
