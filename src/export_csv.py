import sqlite3
import csv

def execute_query(query, params=()):
    """
    Exécute une requête SQL et retourne les résultats.
    
    :param query: La requête SQL à exécuter.
    :param params: Les paramètres pour la requête SQL.
    :return: Les résultats de la requête SQL.
    """
    try:
        # Connexion à la base de données
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        
        # Exécution de la requête
        cursor.execute(query, params)
        
        # Récupérer les résultats de la requête
        results = cursor.fetchall()
        
        return results
    except sqlite3.Error as e:
        print(f"Erreur lors de l'exécution de la requête: {e}")
        return None
    finally:
        # Fermer la connexion
        if conn:
            conn.close()

def export_to_csv(data, filename):
    """
    Exporte les données vers un fichier CSV.
    
    :param data: Les données à exporter (liste de tuples).
    :param filename: Le nom du fichier CSV à générer.
    """
    try:
        # Ouvrir le fichier CSV en mode écriture
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Écrire l'en-tête (si nécessaire)
            header = ['id', 'nom', 'prenom', 'email', 'date_inscription']  # Remplace par tes propres colonnes
            writer.writerow(header)
            
            # Écrire les données
            writer.writerows(data)
            
        print(f"Les données ont été exportées avec succès dans {filename}")
    except Exception as e:
        print(f"Erreur lors de l'exportation des données vers le fichier CSV: {e}")

# Récupérer les données de la table 'users'
query = "SELECT * FROM commandes"
users_data = execute_query(query)

# Exporter les données dans un fichier CSV
if users_data:
    export_to_csv(users_data, 'commandes_data.csv')
