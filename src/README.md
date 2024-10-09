# Gestion de Base de Données avec SQLite et Python

## Contexte du Projet

Ce projet consiste à créer, manipuler et interagir avec une base de données SQLite via des scripts Python. L'objectif est de créer des tables, insérer et manipuler des données, exécuter des requêtes, puis sauvegarder et exporter ces données sous forme de fichiers CSV.

## Fonctionnalités du Projet

### 1. Créer une base de données et des tables

Nous commençons par la création d'une base de données SQLite avec deux tables principales :

- **Table `Clients`** : Contient les informations des clients
  - `id` : identifiant unique (clé primaire)
  - `nom` : nom du client
  - `prenom` : prénom du client
  - `email` : adresse e-mail
  - `date_inscription` : date à laquelle le client s'est inscrit
  
- **Table `Commandes`** : Stocke les commandes effectuées par les clients
  - `id` : identifiant unique (clé primaire)
  - `client_id` : référence au client (clé étrangère liée à la table `Clients`)
  - `produit` : produit commandé
  - `date_commande` : date de la commande

Les tables peuvent être créées de deux manières :
1. Via la commande SQLite manuelle
2. Via un script Python automatisé

### 2. Insertion et manipulation des données

Une fois les tables créées, nous insérons des données dans les tables `Clients` et `Commandes` via des scripts Python.

#### Exemples d'opérations :
- **Insertion des clients** : Création de clients avec un nom, prénom, email, etc.
- **Insertion des commandes** : Attribution des commandes aux clients via la table `Commandes`.

### 3. Exécution de requêtes

Grâce aux scripts Python, nous pouvons interagir avec la base de données et exécuter différentes requêtes SQL :

- **Sélectionner tous les clients** : Obtenir une liste complète des clients.
- **Récupérer les commandes d'un client spécifique** : Filtrer les commandes selon un `client_id`.
- **Mettre à jour l'adresse e-mail d’un client** : Modifier les informations d'un client donné.
- **Supprimer une commande** : Effacer une commande spécifique de la base de données.

### 4. Sauvegarde et export des données

- **Sauvegarde de la base de données** : La base de données SQLite est sauvegardée dans un fichier `.db`.
- **Export des données vers un fichier CSV** : Les données sont exportées en fichiers CSV pour un usage externe, par exemple pour l'analyse ou l'archivage.

### 5. Création de données et insertion via script Python

- **Création et insertion de clients** : Le script Python crée et insère au moins deux clients.
- **Création et insertion de commandes** : Le script Python ajoute au moins deux commandes, liées aux clients créés.

## Prérequis

- **Python 3.x**
- **SQLite3**
- Bibliothèque **`csv`** (incluse dans Python)
- **VS Code** ou tout autre éditeur de texte compatible
