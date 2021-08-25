from models import Player
from models import Round
from models import Game
import operator
import datetime


def add_round(rounds,list_games):
    name = input("Entrez le nom du tour : ")
    rounds.append(Round(list_games,name))


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
        names_games.append(players_sup[i].forename + " Versus " + players_inf[i].forename)
    print(names_games)

    for i in range(0, 4):
        print("Match " + str(i+1) + " " + str(names_games[i]))
        score_p1 = input("Score J1: ")
        score_p2 = input("Score J2: ")
        games.append(Game(players_sup[i], players_inf[i], score_p1, score_p2))
    return games


def next_round(ranking):
    names_games = []
    games = []
    names_games.append(ranking[0].forename + " Versus " + ranking[1].forename)
    names_games.append(ranking[2].forename + " Versus " + ranking[3].forename)
    names_games.append(ranking[4].forename + " Versus " + ranking[5].forename)
    names_games.append(ranking[6].forename + " Versus " + ranking[7].forename)
    print("Matchs du tour : ")
    print(names_games)
    for i in range(0, 4):
        print("Match " + str(i+1) + " " + str(names_games[i]))
        score_p1 = input("Score J1: ")
        score_p2 = input("Score J2: ")
        games.append(Game(ranking[0],ranking[1],score_p1,score_p2))
        games.append(Game(ranking[2],ranking[3],score_p1,score_p2))
        games.append(Game(ranking[4],ranking[5],score_p1,score_p2))
        games.append(Game(ranking[6],ranking[7],score_p1,score_p2))
    return games


def set_ranking(players):
    ranking = {}
    print("Mettre à jour le classement général")
    for player in players:
        print("Joueur "+player.forename)
        score = input("Score : ")
        ranking[player] = float(score)
    sorted(ranking.items(), key=lambda t: t[1])
    print("Classement à jour :")
    i = 1
    for rank in ranking:
        print("Classé "+str(i)+" : "+ rank.forename+ " : " + str(ranking[rank])+" pts")
        i += 1
    return ranking


def edit_ranking(ranking):
    choice = input("Changer le classement général ? (O/N)")
    if choice == "o":
        for rank in ranking:
            print("Joueur "+rank.forename)
            score = input("Entrez le score : ")
            ranking[rank] = float(score) + float(ranking[rank])

        sortedRank = sorted(ranking.items(), key=operator.itemgetter(1), reverse=True)
        sortedRank = dict(sortedRank)
        print("Nouveau classement :")
        i = 1
        for rank in sortedRank:
            print("Classé "+str(i)+" : "+rank.forename+" : "+str(ranking[rank])+"pts")
            i += 1
    else:
        pass
    return ranking


def create_players():
    players = []
    for i in range(0,8):
        print("Joueur "+str(i+1))
        forename = input("Entrez le prenom :")
        name = input("Entrez le nom :")
        date = input("Entrez la date de naissance :")
        sex = input("Entrez le sexe :")
        rank = input("Entrez le classement :")
        players.append(Player(forename,name,date,sex,rank))
    players.sort()
    return players


def end_tournament(tournament,date_start_tournament,final_ranking):
    end_tournament = input("Terminer le tournoi ? ")
    if end_tournament == "o":
        date_end_tournament = str(datetime.datetime.now())
        tournament.date_start = date_start_tournament
        tournament.date_end = date_end_tournament
        pass
    else:
        modify_rank = input("Modifier classement général ?")
        if modify_rank == "o":
            edit_ranking(final_ranking)


def menu():

    menu = ["1. Nouveau Tournoi", "2. Charger Tournoi", "3. Sauvegarder Tournoi", "4. Rapports"]
    print("Bienvenue !\n")
    print(menu)
    choice = input("Votre choix : ")
    return choice