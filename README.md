# P4_Adebayo_Hounkpatin

## Description

Ce projet a pour but la création, sauvegarde, et consultation d'un tournoi d'échecs.

L'ensemble des choix se fait via 1 pour "oui" et 2 pour "non" ( sauf précisions )

```Fichier main.py```

affiche l'interface principale du programme et redirige vers les deux sous-programmes "nouveau tournoi" et "rapports"

```Fichier controlers.py```

Contient l'ensemble des intructions invisibles du programme.

```Fichier models.py```

Contient l'emsemble des classes utilisées : Game, Tournament, Round, Player



### Dossier Views

Contient l'ensemble des affichages utilisateur du programme (Prints, inputs,..)

```Fichier asks.py```

Contient l'ensemble des affichages du programme

```Fichier reports.py```

Contient l'ensemble des affichages de la partie rapports du programme



























## Lancement du programme

Pour pouvoir utiliser le projet, il vous faudra au préalable récupérer l'intégralité du dossier OC_P4_Projet.

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

### Générer le rapport flake8

tapez cette commande :

```bash
pip install flake8-html
```

puis :

```bash
flake8 --format=html --htmldir=flake-report
```
