from models import Tournament
from views import create_players
from views import first_round
from views import set_ranking
from views import add_round
from views import edit_ranking
from views import next_round
from views import end_tournament
import datetime
from tinydb import TinyDB


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

    print("------- Nouveau Tournoi ------\n")

    # Start Tournament
    name_tournament = input("Entrez le nom du tournoi : ")
    description = input("Description : ")
    time = input("Temps : ")
    place = input("Lieu : ")
    date_start_tournament = str(datetime.datetime.now())

    # Create players
    players = create_players()

    # Saving Players
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
    db = TinyDB('db_players.json')
    players_table = db.table('players')
    players_table.truncate()
    players_table.insert_multiple(serialized_players)

    date_start_round = str(datetime.datetime.now())
    games = first_round(players)
    date_end_round = str(datetime.datetime.now())
    final_ranking = set_ranking(players)
    rounds = []
    add_round(rounds,games)
    rounds[0].date_start = date_start_round
    rounds[0].date_end = date_end_round

    # Serializing Game
    serialized_rounds = []
    serialized_games = []

    for round in rounds:

        for game in games:
            serialized_game = {
                "Player 1": game.p1.forename,
                "Player 2": game.p2.forename,
                "Score P1": game.score_p1,
                "Score P2": game.score_p2
            }
            serialized_games.append(serialized_game)

        # Serializing Rounds
        serialized_round = {
            "date debut": round.date_start,
            "date fin": round.date_end,
            "Nom": round.name,
            "Liste matchs": serialized_games
        }
        serialized_rounds.append(serialized_round)

    ranking = get_ranking(games)

    for i in range(1, 4):
        date_start_round = str(datetime.datetime.now())
        games = next_round(ranking)
        date_end_round = str(datetime.datetime.now())
        final_ranking = edit_ranking(final_ranking)
        add_round(rounds,games)
        rounds[i].date_start = date_start_round
        rounds[i].date_end = date_end_round

        for round in rounds:

            # Serializing Games
            for game in games:
                serialized_game = {
                    "Player 1": game.p1.forename,
                    "Player 2": game.p2.forename,
                    "Score P1": game.score_p1,
                    "Score P2": game.score_p2
                }
                serialized_games.append(serialized_game)

            # Serializing Rounds
            serialized_round = {
                "date début": round.date_start,
                "date fin": round.date_end,
                "Nom": round.name,
                "Liste matchs": serialized_games
            }
            serialized_rounds.append(serialized_round)

        ranking = get_ranking(games)

    tournaments = []
    tournaments.append(Tournament(name_tournament,place,time,players,rounds,description))

    for tournament in tournaments:

        end_tournament(tournament,date_start_tournament,final_ranking)

        # Saving Tournament
        serialized_tournaments = []
        end_tournament(tournament, date_start_tournament, final_ranking)
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
        db = TinyDB('db_tournaments.json')
        tournaments_table = db.table('tournaments')
        tournaments_table.truncate()
        tournaments_table.insert_multiple(serialized_tournaments)
