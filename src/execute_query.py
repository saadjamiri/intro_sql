# src/execute_queries.py

import sqlite3

def get_client_by_email(id):
    """Récupère les informations d'un client à partir de son id."""
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM clients WHERE id = ?', (id,))
    client = cursor.fetchone()
    
    conn.close()
    return client

def execute_query(query, params):
    try:
        conn = sqlite3.connect('store.db')  
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        print("Requête exécutée avec succès")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'exécution de la requête: {e}")
    finally:
        if conn:
            conn.close()

def update_email(user_id, nouveau_email):
    """
    Met à jour l'adresse e-mail d'un utilisateur dans la base de données.
    
    :param user_id: ID de l'utilisateur dont l'e-mail doit être mis à jour.
    :param nouveau_email: Nouvelle adresse e-mail à attribuer.
    :return: Confirmation de la mise à jour.
    """
    try:
        query = "UPDATE users SET email = ? WHERE user_id = ?"
        params = (nouveau_email, user_id)
        execute_query(query, params)
        print(f"L'adresse e-mail de l'utilisateur {user_id} a été mise à jour avec succès.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour de l'e-mail: {e}")

def delete_commande(commande_id):
    """
    Supprime une commande dans la base de données.
    
    :param commande_id: ID de la commande à supprimer.
    :return: Confirmation de la suppression.
    """
    try:
        query = "DELETE FROM commandes WHERE commande_id = ?"
        params = (commande_id,)
        execute_query(query, params)
        print(f"La commande {order_id} a été supprimée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de la commande: {e}")

def get_commandes_client_id(client_id):
    """Récupère toutes les commandes d'un client spécifique."""
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT produit FROM commandes WHERE client_id = ?', (client_id,))
    commandes = cursor.fetchall()
    
    conn.close()
    return commandes





if __name__ == "__main__":
    # Exemple d'utilisation des fonctions
    id = 1
    client = get_client_by_email(id)
    print(f"Client avec l'id {id} : {client}")
    
    client_id = 1
    commandes = get_commandes_client_id(client_id)
    print(f"Commandes pour le client ID {client_id} : {commandes}")
    
    
    id = 1
    new_mail = 'soso.sania@gmail.com'
    client_1 = update_email(id, new_mail)
    print(f"le nouveau mail pour le client {id} : {client_1}")


    
    
    
