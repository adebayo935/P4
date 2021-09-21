from game.models import Player, Round, Game
from game.views.reports import list_players, list_players_tournament,\
    list_tournaments, list_rounds_tournament, \
    list_games_tournament
import operator
import datetime


def add_round(rounds, list_games):
    name = input("Entrez le nom du tour : ")
    rounds.append(Round(list_games, name))
    print(rounds)
    for tour in rounds:
        print(tour.name)


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
    for game in games:
        print(game.score_p1 + " " + game.score_p2)
    return games


def next_round(ranking):
    names_games = []
    games = []
    names_games.append(ranking[0].forename + " Versus " + ranking[1].forename)
    names_games.append(ranking[2].forename + " Versus " + ranking[3].forename)
    names_games.append(ranking[4].forename + " Versus " + ranking[5].forename)
    names_games.append(ranking[6].forename + " Versus " + ranking[7].forename)
    print("Matchs du prochain tour : ")
    print(names_games)
    n = 0
    k = 1
    for i in range(0, 4):
        print("Match " + str(i + 1) + " " + str(names_games[i]))
        score_p1 = input("Score J1: ")
        score_p2 = input("Score J2: ")
        games.append(Game(ranking[n], ranking[k], score_p1, score_p2))
        k += 2
        n += 2

    for game in games:
        print(game.score_p1 + " " + game.score_p2)
    return games


def set_ranking(players):
    ranking = {}
    print("Mettre à jour le classement général")
    for player in players:
        print("Joueur " + player.forename)
        score = input("Score : ")
        ranking[player] = float(score)
    sorted(ranking.items(), key=lambda t: t[1])
    print("Classement à jour :")
    i = 1
    for rank in ranking:
        print("Classé " + str(i) + " : " + rank.forename + " : " +
              str(ranking[rank]) + " pts")
        i += 1
    return ranking


def edit_ranking(ranking):
    ranking_fake = []
    print("Classement du Tournoi\n")
    for rank in ranking:
        print("Joueur " + rank.forename)
        score = input("Entrez le score : ")
        ranking[rank] = float(score) + float(ranking[rank])
    sorted_rank = sorted(ranking.items(), key=operator.itemgetter(1),
                         reverse=True)
    sorted_rank = dict(sorted_rank)
    print("Nouveau classement :")
    i = 1
    for rank in sorted_rank:
        print("Classé " + str(i) + " : " + rank.forename + " : " +
              str(ranking[rank]) + "pts")
        ranking_fake.append(rank)
        i += 1
    return ranking


def players_ranking(players):
    for player in players:
        print("Joueur " + player.forename)
        rank = input("Entrez le classement : ")
        player.rank = rank


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
    text = input("Terminer le tournoi ? ")
    if str(text) == "y" or "Y":
        date_end_tournament = str(datetime.datetime.now())
        tournament.date_start = date_start_tournament
        tournament.date_end = date_end_tournament
        print("Tournoi Terminé")
        pass
    else:
        modify_rank = input("Modifier classement joueurs ?")
        if modify_rank == "y" or "Y":
            players_ranking(players)


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
