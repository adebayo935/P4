import json
from tinydb import TinyDB

file = json.load(open("dev/db_tournaments.json"))
db = TinyDB('dev/db_tournaments.json')
tournaments_table = db.table('tournaments')
tournaments = tournaments_table.all()
players_table = db.table('players')
players = players_table.all()


def list_players():

    print("--- Liste des joueurs ---\n")
    print("1. Par classement\n")
    print("2. Par ordre alphabétique\n")
    choice = input("Votre choix : ")

    if int(choice) == 1:
        sorted_players = sorted(players, key=lambda k: k['rank'])
        for player in sorted_players:
            print('Prenom : ' + str(player['forename']) + '\n' +
                  'Nom : ' + str(player['name']) + '\n' +
                  'Date de naissance : ' + str(player['date']) + '\n' +
                  'Sexe : ' + str(player['sex']) + '\n' +
                  'Classement : ' + str(player['rank']) + '\n')
    elif int(choice) == 2:
        sorted_players = sorted(players, key=lambda k: k['forename'])
        for player in sorted_players:
            print('Prenom : ' + str(player['forename']) + '\n' +
                  'Nom : ' + str(player['name']) + '\n' +
                  'Date de naissance : ' + str(player['date']) + '\n' +
                  'Sexe : ' + str(player['sex']) + '\n' +
                  'Classement : ' + str(player['rank']) + '\n')


def list_players_tournament():

    print("--- Liste des joueurs par tournoi ---\n")
    choice = input("Entrez le nom du tournoi : ")
    print("1. Par classement\n")
    print("2. Par ordre alphabétique\n")
    second_choice = input("Votre choix : ")

    for tournament in tournaments:
        if choice == str(tournament['name']):
            if int(second_choice) == 1:
                sorted_players = sorted(tournament['players'], key=lambda k: k['rank'])
                for player in sorted_players:
                    print('Prenom : ' + str(player['forename']) + '\n' +
                          'Nom : ' + str(player['name']) + '\n' +
                          'Date de naissance : ' + str(player['date']) + '\n' +
                          'Sexe : ' + str(player['sex']) + '\n' +
                          'Classement : ' + str(player['rank']) + '\n')
            elif int(second_choice) == 2:
                sorted_players = sorted(tournament['players'], key=lambda k: k['forename'])
                for player in sorted_players:
                    print('Prenom : ' + str(player['forename']) + '\n' +
                          'Nom : ' + str(player['name']) + '\n' +
                          'Date de naissance : ' + str(player['date']) + '\n' +
                          'Sexe : ' + str(player['sex']) + '\n' +
                          'Classement : ' + str(player['rank']) + '\n')


def list_tournaments():
    print("--- Liste de tous les tournois ---\n")
    i = 1
    for tournament in tournaments:
        print('Tournoi ' + str(i) + '\n' +
              'Nom : ' + str(tournament['name']) + '\n' +
              'Lieu : ' + str(tournament['place']) + '\n' +
              'Temps : ' + str(tournament['time']) + '\n' +
              'Description: ' + str(tournament['description']) + '\n\n' +
              'Liste des Joueurs :')
        o = 1
        for player in tournament['players']:
            print('Player ' + str(o) + '\n' +
                  'Prénom : ' + str(player['forename']) + '\n' +
                  'Nom : ' + str(player['name']) + '\n' +
                  'Date de naissance : ' + str(player['date']) + '\n' +
                  'Sexe : ' + str(player['sex']) + '\n' +
                  'Classement : ' + str(player['rank']) + '\n')
            o += 1
        print('Liste des tours :')
        o = 1
        for tour in tournament['rounds']:
            print('Tour  ' + str(o) + '\n' +
                  'Date de début : ' + str(tour['date debut']) + '\n' +
                  'Date de fin : ' + str(tour['date fin']) + '\n' +
                  'Nom : ' + str(tour['Nom']) + '\n' +
                  'Liste des matchs :\n')
            s = 1
            for game in tour['Liste matchs']:
                print('Match ' + str(s) + '\n' +
                      'Joueur 1 : ' + str(game['Player 1']) + '\n' +
                      'Joueur 2 : ' + str(game['Player 2']) + '\n' +
                      'Score 1 : ' + str(game['Score P1']) + '\n' +
                      'Score 2 : ' + str(game['Score P2']) + '\n')
                s += 1
            o += 1
        i += 1


def list_rounds_tournament():
    print("--- Liste des tours d'un tournoi ---\n")
    choice = input("Entrez le nom du tournoi : ")

    for tournament in tournaments:
        if choice == str(tournament['name']):
            print('Liste des tours :')
            o = 1
            for tour in tournament['rounds']:
                print('Tour  ' + str(o) + '\n' +
                      'Date de début : ' + str(tour['date debut']) + '\n' +
                      'Date de fin : ' + str(tour['date fin']) + '\n' +
                      'Nom : ' + str(tour['Nom']) + '\n' +
                      'Liste des matchs :\n')
                o += 1
                s = 1
                for game in tour['Liste matchs']:
                    print('Match ' + str(s) + '\n' +
                          'Joueur 1 : ' + str(game['Player 1']) + '\n' +
                          'Joueur 2 : ' + str(game['Player 2']) + '\n' +
                          'Score 1 : ' + str(game['Score P1']) + '\n' +
                          'Score 2 : ' + str(game['Score P2']) + '\n')
                    s += 1


def list_games_tournament():
    print("--- Liste des matchs d'un tournoi ---\n")
    choice = input("Entrez le nom du tournoi : ")

    for tournament in tournaments:
        if choice == str(tournament['name']):
            o = 1
            for tour in tournament['rounds']:
                print('Tour  ' + str(o) + '\n')
                o += 1
                s = 1
                for game in tour['Liste matchs']:
                    print('Match ' + str(s) + '\n' +
                          'Joueur 1 : ' + str(game['Player 1']) + '\n' +
                          'Joueur 2 : ' + str(game['Player 2']) + '\n' +
                          'Score 1 : ' + str(game['Score P1']) + '\n' +
                          'Score 2 : ' + str(game['Score P2']) + '\n')
                    s += 1
