from models import Tournament
from views import create_players
from views import first_round
from views import set_ranking
from views import add_round
from views import edit_ranking
from views import next_round
from views import end_tournament
from views import menu
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

    # Start Tournament
    name_tournament = input("Entrez le nom du tournoi : ")
    description = input("Description : ")
    time = input("Temps : ")
    place = input("Lieu : ")
    date_start_tournament = str(datetime.datetime.now())

    # Create players
    players = create_players()

    # Saving Players
    serialized_players = {}
    for player in players:
        serialized_player = {
            'forename': player.forename,
            'name': player.name,
            'date': player.date,
            'sex': player.sex,
            'rank': player.rank
        }
        serialized_players.pop(serialized_player)
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()
    players_table.insert_multiple(serialized_players)


    # Round 1
    date_start_round = str(datetime.datetime.now())
    games1 = first_round(players)
    date_end_round = str(datetime.datetime.now())
    final_ranking = set_ranking(players)
    rounds = []
    add_round(rounds,games1)
    rounds[0].date_start = date_start_round
    rounds[0].date_end = date_end_round
    ranking = get_ranking(games1)

    # Round 2
    date_start_round = str(datetime.datetime.now())
    games2 = next_round(ranking)
    date_end_round = str(datetime.datetime.now())
    final_ranking = edit_ranking(final_ranking)
    add_round(rounds,games2)
    rounds[1].date_start = date_start_round
    rounds[1].date_end = date_end_round
    ranking = get_ranking(games2)

    # Round 3
    date_start_round = str(datetime.datetime.now())
    games3 = next_round(ranking)
    date_end_round = str(datetime.datetime.now())
    final_ranking = edit_ranking(final_ranking)
    add_round(rounds,games3)
    rounds[2].date_start = date_start_round
    rounds[2].date_end = date_end_round
    ranking = get_ranking(games3)


    # Round 4
    date_start_round = str(datetime.datetime.now())
    games4 = next_round(ranking)
    date_end_round = str(datetime.datetime.now())
    final_ranking = edit_ranking(final_ranking)
    add_round(rounds,games4)
    rounds[3].date_start = date_start_round
    rounds[3].date_end = date_end_round

    # Ending Tournament
    ending = input('Terminer le tournoi ?')
    if ending == "n":
        modify = input('Modifier classement général ?')
        if modify == "y":
            final_ranking = edit_ranking(final_ranking)
        else:
            print('Tournoi terminé')
            pass
    else:
        print('Tournoi Terminé')
        pass
    tournaments = []
    tournaments.append(Tournament(name_tournament,place,players,rounds,time,description))

    # Saving Tournament
    serialized_tournaments = {}
    for tournament in tournaments:
        end_tournament(tournament, date_start_tournament, final_ranking)
        serialized_tournament = {
            'name': tournament.name,
            'place': tournament.place,
            'players': tournament.players,
            'rounds': tournament.rounds,
            'time': tournament.time,
            'description': tournament.description,
            'date_start': tournament.date_start,
            'date_end': tournament.date_end,
            'nb_rounds': tournament.nb_rounds
        }
        serialized_tournaments.pop(serialized_tournament)
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.truncate()
    tournaments_table.insert_multiple(serialized_tournaments)




choice = menu()
if int(choice) == 1:
    create_tournament()