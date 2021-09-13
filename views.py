from models import Player
from models import Round
from models import Game
from reports import list_players
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
    print("Matchs du prochain tour : ")
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
    choice = input("Changer le classement général ? (Y/N)")
    if choice == "y":
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
    if end_tournament == "y":
        date_end_tournament = str(datetime.datetime.now())
        tournament.date_start = date_start_tournament
        tournament.date_end = date_end_tournament
        print("Tournoi Terminé")
        pass
    else:
        modify_rank = input("Modifier classement général ?")
        if modify_rank == "y":
            edit_ranking(final_ranking)


def menu():

    print("1. Nouveau Tournoi\n")
    print("2. Rapports\n")
    print("Bienvenue !\n")
    print(menu)
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
