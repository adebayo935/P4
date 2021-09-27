from game.models import Player, Round, Game
from game.views.reports import list_players, list_players_tournament, \
    list_tournaments, list_rounds_tournament, \
    list_games_tournament
import datetime


def add_round(rounds, list_games):
    name = input("Entrez le nom du tour : ")
    rounds.append(Round(list_games, name))


def ask_input(text):
    ask = input(text)
    return ask


def print_text(text):
    print(text)


def first_round(players):
    players_sup = []
    players_inf = []

    for i in range(0, 4):
        players_sup.append(players[i])
    for i in range(4, 8):
        players_inf.append(players[i])

    names_games = []
    games = []
    for i in range(0, 4):
        names_games.append(players_sup[i].forename + " Versus " +
                           players_inf[i].forename)
    print(names_games)
    k = 0
    n = 0
    for i in range(0, 4):
        print("Match " + str(i + 1) + " " + str(names_games[i]))
        score_p1 = input("Score J1: ")
        score_p2 = input("Score J2: ")
        games.append(Game(players_sup[n], players_inf[k],
                          score_p1, score_p2))
        k += 1
        n += 1
    return games


def first_option(ranking, games):
    print("Match " + str(1) + " : " +
          str(ranking[0][0].forename)
          + ' VS ' + str(ranking[2][0].forename))
    score_p1 = input("Score J1: ")
    score_p2 = input("Score J2: ")
    games.append(Game(ranking[0][0], ranking[2][0], score_p1, score_p2))
    print("Match " + str(2) + " : " +
          str(ranking[1][0].forename)
          + ' VS ' + str(ranking[3][0].forename))
    score_p1 = input("Score J1: ")
    score_p2 = input("Score J2: ")
    games.append(Game(ranking[1][0], ranking[3][0], score_p1, score_p2))
    print("Match " + str(3) + " : " +
          str(ranking[4][0].forename)
          + ' VS ' + str(ranking[5][0].forename))
    score_p1 = input("Score J1: ")
    score_p2 = input("Score J2: ")
    games.append(Game(ranking[4][0], ranking[5][0], score_p1, score_p2))
    print("Match " + str(4) + " : " +
          str(ranking[6][0].forename)
          + ' VS ' + str(ranking[7][0].forename))
    score_p1 = input("Score J1: ")
    score_p2 = input("Score J2: ")
    games.append(Game(ranking[6][0], ranking[7][0], score_p1, score_p2))


def next_round(ranking):
    games = []
    print(ranking[0][0].forename + " Versus " + ranking[1][0].forename +
          '\n' +
          ranking[2][0].forename + " Versus " + ranking[3][0].forename +
          '\n' +
          ranking[4][0].forename + " Versus " + ranking[5][0].forename +
          '\n' +
          ranking[6][0].forename + " Versus " + ranking[7][0].forename)
    print("Matchs du prochain tour : ")
    n = 0
    k = 1
    for game_index in range(0, 4):
        print("Match " + str(game_index + 1) + " : " +
              str(ranking[n][0].forename)
              + ' VS ' + str(ranking[k][0].forename))
        score_p1 = input("Score J1: ")
        score_p2 = input("Score J2: ")
        games.append(Game(ranking[n][0], ranking[k][0],
                          score_p1, score_p2))
        k += 2
        n += 2
    return games


def final_round(ranking, previous_ranking):
    games = []
    if previous_ranking[0][0].forename == ranking[0][0].forename \
            and previous_ranking[1][0].forename == ranking[1][0].forename:
        print(ranking[0][0].forename + " Versus " + ranking[2][0].forename +
              '\n' +
              ranking[1][0].forename + " Versus " + ranking[3][0].forename +
              '\n' +
              ranking[4][0].forename + " Versus " + ranking[5][0].forename +
              '\n' +
              ranking[6][0].forename + " Versus " + ranking[7][0].forename)
        print("Matchs du prochain tour : ")
        first_option(ranking, games)
    else:
        print(ranking[0][0].forename + " Versus " + ranking[1][0].forename +
              '\n' +
              ranking[2][0].forename + " Versus " + ranking[3][0].forename +
              '\n' +
              ranking[4][0].forename + " Versus " + ranking[5][0].forename +
              '\n' +
              ranking[6][0].forename + " Versus " + ranking[7][0].forename)
        print("Matchs du prochain tour : ")
        n = 0
        k = 1
        for game_index in range(0, 4):
            print("Match " + str(game_index + 1) + " : " +
                  str(ranking[n][0].forename)
                  + ' VS ' + str(ranking[k][0].forename))
            score_p1 = input("Score J1: ")
            score_p2 = input("Score J2: ")
            games.append(Game(ranking[n][0], ranking[k][0],
                              score_p1, score_p2))
            k += 2
            n += 2
    return games


def set_ranking(players):
    ranking = []
    print("Mettre à jour le classement général")
    for player in players:
        print("Joueur " + player.forename)
        score = input("Score : ")
        ranking.append([player, float(score)])
    sorted_rank = sorted(ranking, key=lambda k_v: k_v[1],
                         reverse=True)
    print(ranking)
    print("Classement à jour :")
    i = 1
    for rank in sorted_rank:
        print("Classé " + str(i) + " : " + rank[0].forename +
              " : " + str(rank[1]) + " pts")
        i += 1
    return ranking


def edit_ranking(ranking):
    print("Classement du Tournoi\n")
    for rank in ranking:
        print("Joueur " + rank[0].forename)
        score = input("Entrez le score : ")
        rank[1] += float(score)
    sorted_rank = sorted(ranking, key=lambda k_v: k_v[1],
                         reverse=True)
    print("Nouveau classement :")
    i = 1
    for rank in sorted_rank:
        print("Classé " + str(i) + " : " + rank[0].forename + " : " +
              str(rank[1]) + "pts")
        i += 1
    return sorted_rank


def players_ranking(players):
    for player in players:
        print("Joueur " + player.forename)
        rank = input("Entrez le classement : ")
        player.rank = int(rank)


def create_players():
    players = []
    for i in range(0, 8):
        print("Joueur " + str(i + 1))
        forename = input("Entrez le prenom :")
        name = input("Entrez le nom :")
        date = input("Entrez la date de naissance :")
        sex = input("Entrez le sexe :")
        rank = input("Entrez le classement :")
        players.append(Player(forename, name, date, sex, rank))
    players.sort()
    return players


def end_tournament(tournament, date_start_tournament, players):
    print("Terminer ?\n1. Terminer\n2.Modifier classement joueurs")
    text = input("Votre choix : ")
    if int(text) == 1:
        date_end_tournament = str(datetime.datetime.now())
        tournament.date_start = date_start_tournament
        tournament.date_end = date_end_tournament
        print("Tournoi Terminé")
        pass
    elif int(text) == 2:
        date_end_tournament = str(datetime.datetime.now())
        tournament.date_start = date_start_tournament
        tournament.date_end = date_end_tournament
        players_ranking(players)
        print("Tournoi Terminé")
        pass


def menu():
    print("1. Nouveau Tournoi\n")
    print("2. Rapports\n")
    print("Bienvenue !\n")
    choice = input("Votre choix : ")
    return choice


def reports():
    print("-------- Rapports --------\n")
    print("1. Liste des joueurs\n")
    print("2. Liste des joueurs par tournoi\n")
    print("3. Liste de tous les tournois\n")
    print("4. Liste des tours d'un tournoi\n")
    print("5. Liste des matchs d'un tournoi\n")
    choice = input("Votre choix : ")
    if int(choice) == 1:
        list_players()
    elif int(choice) == 2:
        list_players_tournament()
    elif int(choice) == 3:
        list_tournaments()
    elif int(choice) == 4:
        list_rounds_tournament()
    elif int(choice) == 5:
        list_games_tournament()
