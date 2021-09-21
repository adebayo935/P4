# P4_Adebayo_Hounkpatin

## Description

Ce projet a pour but la création, sauvegarde, et consultation d'un tournoi d'échecs.

```Fichier controlers.py```

Contient l'ensemble des intructions invisibles du programme.

Les fonctions Serializing players, serializing games, serializing round, serializing first_round, serializing tournament assurent respectivement
la sauvagarde des joueurs, matchs, tour(2,3,4), premier tour et tournoi.

La fonction get_ranking assure la création du premier tour

La fonction create_tournament assure le déroulement de chaque étape de la création du tournoi


```Fichier models.py```

Contient l'emsemble des classes utilisées : Game, Tournament, Round, Player



### Dossier Views

Contient l'ensemble des affichages utilisateur du programme (Prints, inputs,..)

```Fichier asks.py```

Contient l'ensemble des affichages du programme

la fonction add_round récupère le nom du tour et crée une instance de Round

La fonction print_text affiche un texte donné

la fonction ask_input affiche un input donné

la fonction first_round crée les matchs du premier tour

la fonction next_round crée les mtachs du tour 3,4 et 5

la fonction set_ranking crée le classement du 1er tour

la fonction edit_ranking crée le classement des tours suivants

la fonction players_ranking modifie le classements des joueurs

la fonction create_players récupère les infos de chaque joueur

la fonction end_tournament termine le tournoi et crée une instance Tournament

la fonction menu affiche le menu principal du programme

la fonction reports renvoie vers le fichier reports


```Fichier reports.py```

Contient l'ensemble des affichages de la partie rapports du programme

la fonction list_players affiche tous les joueurs sauvegardés par le programme

la fonction list_players_tournament affiche tous les joueurs par tournoi

la fonction list_tournaments affiche tous les tournois

la fonction list_rounds_tournaments affiche tous les tours d'un tournoi

la fonction list_games_tournaments affiche tous les matchs d'un tournoi


























## Lancement du scrapping

Pour pouvoir utiliser le projet, il vous faudra au préalable récupérer l'intégralité du dossier OC_P2_Projet.

Dans un premier temps, vous devez cloner le projet puis installer les modules présents dans le fichier requirements.txt, dans votre environnement python.

### Creer un environnement virtuel

Windows

```bash
py -m venv venv
```

Linux/Mac

```bash
python3 -m venv venv
```

### Activer l'environnement virtuel

Windows

```bash
venv\Scripts\activate.bat
```

Linux/Mac

```bash
source venv/bin/activate
```

### Installer les dépendances

Tapez cette commande:

```bash
pip install -r requirements.txt
```

### Executer le projet

Ouvrez votre terminal et tapez:

Windows

```bash
python main.py
```

Linux/Mac

```bash
python main.py
```


