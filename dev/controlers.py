from dev.models import Tournament
from dev.views.asks import create_players, first_round, set_ranking, add_round, edit_ranking, next_round, end_tournament,ask_input, print_text
import datetime
from tinydb import TinyDB


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
        db = TinyDB('dev/db_tournaments.json')
        players_table = db.table('players')
        players_table.insert_multiple(serialized_players)
    return serialized_players


def serializing_games(games):
    serialized_fake = []
    for game in games:
        serialized_game = {
            "Player 1": game.p1.forename,
            "Player 2": game.p2.forename,
            "Score P1": game.score_p1,
            "Score P2": game.score_p2
        }
        serialized_fake.append(serialized_game)
    print(serialized_fake)
    return serialized_fake


def serializing_rounds(rounds,serialized_games):
    serialized_fake = []
    for tour in rounds:
        serialized_round = {
            "date debut": tour.date_start,
            "date fin": tour.date_end,
            "Nom": tour.name,
            "Liste matchs": serialized_games
            }
        serialized_fake.append(serialized_round)
    return serialized_fake


def serializing_tournaments(tournament,serialized_players,serialized_rounds):
    serialized_tournaments = []
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
    serialized_tournaments.append(serialized_tournament)
    db = TinyDB('dev/db_tournaments.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.insert_multiple(serialized_tournaments)


def get_ranking(previous_matchs):
    ranking = []
    winners = []
    tied = []
    losers = []
    for i in range(0,4):
        if previous_matchs[i].score_p1 > previous_matchs[i].score_p2:
            winners.append(previous_matchs[i].p1)
            losers.append(previous_matchs[i].p2)
        elif previous_matchs[i].score_p2 > previous_matchs[i].score_p1:
            winners.append(previous_matchs[i].p2)
            losers.append(previous_matchs[i].p1)
        else:
            tied.append(previous_matchs[i].p1)
            tied.append(previous_matchs[i].p2)

    winners.sort()
    losers.sort()
    tied.sort()

    for winner in winners:
        ranking.append(winner)
    for player in tied:
        ranking.append(player)
    for loser in losers:
        ranking.append(loser)
    return ranking


def create_tournament():
    print_text("------- Nouveau Tournoi ------\n")
    name_tournament = ask_input('Entrez le nom du tournoi : ')
    description = ask_input("Description : ")
    time = ask_input("Temps : ")
    place = ask_input("Lieu : ")
    date_start_tournament = str(datetime.datetime.now())

    serialized_rounds = []
    serialized_games = []

    players = create_players()
    serialized_players = serializing_players(players)

    date_start_round = str(datetime.datetime.now())
    games = first_round(players)
    serialized_games.append(serializing_games(games))
    date_end_round = str(datetime.datetime.now())
    final_ranking = set_ranking(players)
    rounds = []
    add_round(rounds,games)
    rounds[0].date_start = date_start_round
    rounds[0].date_end = date_end_round
    serialized_rounds.append(serializing_rounds(rounds,serialized_games))
    ranking = get_ranking(games)

    for i in range(1, 4):
        date_start_round = str(datetime.datetime.now())
        games = next_round(ranking)
        serialized_games.append(serializing_games(games))
        date_end_round = str(datetime.datetime.now())
        final_ranking = edit_ranking(final_ranking)
        add_round(rounds,games)
        rounds[i].date_start = date_start_round
        rounds[i].date_end = date_end_round
        serialized_rounds.append(serializing_rounds(rounds,serialized_games))
        ranking = get_ranking(games)

    tournament = Tournament(name_tournament,place,time,players,rounds,description)
    end_tournament(tournament,date_start_tournament,players)
    serializing_tournaments(tournament,serialized_players,serialized_rounds)