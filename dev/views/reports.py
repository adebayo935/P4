import json
from tinydb import TinyDB

file = json.load(open("dev/db_tournaments.json"))


def list_players():
    print("--- Liste des joueurs ---\n")
    print("1. Par classement\n")
    print("2. Par ordre alphabétique\n")
    choice = input("Votre choix : ")

    db = TinyDB('dev/db_tournaments.json')
    players_table = db.table('players')
    players = players_table.all()

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

    i = 1
    while file['tournaments'][str(i)]:
        if file['tournaments'][str(i)]['name'] == choice:
            o = 1
            for player in file['tournaments'][str(i)]['players']:
                print('Player ' + str(o) + '\n' +
                      'Prenom : ' + player['forename'] + '\n' +
                      'Nom : ' + player['name'] + '\n' +
                      'Date de naissance : ' + str(player['date']) + '\n' +
                      'Sexe : ' + str(player['sex']) + '\n' +
                      'Classement : ' + str(player['rank']) + '\n')
                o += 1
            break
        else:
            i += 1


def list_tournaments():
    print("--- Liste de tous les tournois ---\n")

    i = 1
    while file['tournaments'][str(i)]:
        print('Tournoi ' + str(i) + '\n' +
              'Nom : ' + str(file['tournaments'][str(i)]['name']) + '\n' +
              'Lieu : ' + str(file['tournaments'][str(i)]['place']) + '\n' +
              'Temps : ' + str(file['tournaments'][str(i)]['time']) + '\n' +
              'Description: ' + str(file['tournaments'][str(i)]['description']) + '\n\n' +
              'Liste des Joueurs :')
        o = 1
        for player in file['tournaments'][str(i)]['players']:
            print('Player ' + str(o) + '\n' +
                  'Prenom : ' + str(player['forename']) + '\n' +
                  'Nom : ' + str(player['name']) + '\n' +
                  'Date de naissance : ' + str(player['date']) + '\n' +
                  'Sexe : ' + str(player['sex']) + '\n' +
                  'Classement : ' + str(player['rank']) + '\n')
            o += 1
        print('Liste des tours :')
        o = 1
        for tour in file['tournaments'][str(i)]['rounds']:
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
        break


def list_rounds_tournament():
    print("--- Liste des tours d'un tournoi ---\n")
    choice = input("Entrez le nom du tournoi : ")

    i = 1
    while file['tournaments'][str(i)]:
        if file['tournaments'][str(i)]['name'] == choice:
            print('Liste des tours :')
            o = 1
            for tour in file['tournaments'][str(i)]['rounds']:
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
            break
        else:
            i += 1


def list_games_tournament():
    print("--- Liste des matchs d'un tournoi ---\n")
    choice = input("Entrez le nom du tournoi : ")

    i = 1
    while file['tournaments'][str(i)]:
        if file['tournaments'][str(i)]['name'] == choice:
            o = 1
            for tour in file['tournaments'][str(i)]['rounds']:
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
            break
        else:
            i += 1
