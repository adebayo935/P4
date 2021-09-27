from game.models import Tournament
from game.views.asks import create_players, first_round, \
    set_ranking, add_round, edit_ranking, next_round, \
    end_tournament, ask_input, print_text
import datetime
from tinydb import TinyDB


def saving_players(players):
    serialized_players = []
    saving = ask_input("Sauvegarder ?")
    if int(saving) == 1:
        serialized_players = serializing_players(players)
        pass
    else:
        pass
    return serialized_players


def saving_first_round(rounds, serialized_games):
    serialized_rounds = []
    saving = ask_input("Sauvegarder ?")
    if int(saving) == 1:
        serialized_rounds = [serializing_first_round(rounds, serialized_games)]
        pass
    else:
        pass
    return serialized_rounds


def saving_round(serialized_rounds, rounds, serialized_games):
    saving = ask_input("Sauvegarder ?")
    if int(saving) == 1:
        serialized_rounds.append(serializing_round(rounds, serialized_games))
        pass
    else:
        pass


def serializing_players(players):
    serialized_players = []
    for player in players:
        serialized_player = {
            'forename': player.forename,
            'name': player.name,
            'date': player.date,
            'sex': player.sex,
            'rank': player.rank
        }
        serialized_players.append(serialized_player)
        db = TinyDB('game/db_tournaments.json')
        players_table = db.table('players')
        players_table.insert_multiple(serialized_players)
    return serialized_players


def serializing_games(games):
    serialized_games = []
    for game in games:
        serialized_game = {
            "Player 1": game.p1.forename,
            "Player 2": game.p2.forename,
            "Score P1": game.score_p1,
            "Score P2": game.score_p2
        }
        serialized_games.append(serialized_game)
    return serialized_games


def serializing_first_round(rounds, serialized_games):
    serialized_round = {
        "date debut": rounds[0].date_start,
        "date fin": rounds[0].date_end,
        "Nom": rounds[0].name,
        "Liste matchs": serialized_games
    }
    return serialized_round


def serializing_round(rounds, serialized_games):
    serialized_round = {
        "date debut": rounds[-1].date_start,
        "date fin": rounds[-1].date_end,
        "Nom": rounds[-1].name,
        "Liste matchs": serialized_games
    }
    return serialized_round


def serializing_tournaments(tournament, serialized_players, serialized_rounds):
    serialized_tournament = {
        'name': tournament.name,
        'place': tournament.place,
        'players': serialized_players,
        'rounds': serialized_rounds,
        'time': tournament.time,
        'description': tournament.description,
        'date_start': tournament.date_start,
        'date_end': tournament.date_end,
        'nb_rounds': tournament.nb_rounds
    }
    db = TinyDB('game/db_tournaments.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.insert(serialized_tournament)


def make_round(name_round, i, rounds, serialized_rounds):
    date_start_round = str(datetime.datetime.now())
    games = next_round(name_round)
    serialized_games = serializing_games(games)
    date_end_round = str(datetime.datetime.now())
    final_ranking = edit_ranking(name_round)
    add_round(rounds, games)
    rounds[i].date_start = date_start_round
    rounds[i].date_end = date_end_round
    saving_round(serialized_rounds, rounds, serialized_games)
    return final_ranking


def create_tournament():
    print_text("------- Nouveau Tournoi ------\n")
    name_tournament = ask_input('Entrez le nom du tournoi : ')
    description = ask_input("Description : ")
    time = ask_input("Temps : ")
    place = ask_input("Lieu : ")
    date_start_tournament = str(datetime.datetime.now())

    players = create_players()
    serialized_players = saving_players(players)

    date_start_round = str(datetime.datetime.now())
    games = first_round(players)
    serialized_games = serializing_games(games)
    date_end_round = str(datetime.datetime.now())
    ranking = set_ranking(players)
    rounds = []
    add_round(rounds, games)
    rounds[0].date_start = date_start_round
    rounds[0].date_end = date_end_round
    serialized_rounds = saving_first_round(rounds, serialized_games)
    second_round = make_round(ranking, 1, rounds, serialized_rounds)
    third_round = make_round(second_round, 2, rounds, serialized_rounds)
    make_round(third_round, 3, rounds, serialized_rounds)

    tournament = Tournament(name_tournament, place, time,
                            players, rounds, description)
    end_tournament(tournament, date_start_tournament, players)
    serializing_tournaments(tournament, serialized_players, serialized_rounds)
