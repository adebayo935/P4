from modeles import Tournament
import datetime
from vues import create_players
from vues import first_round
from vues import set_ranking
from vues import add_round
from vues import edit_ranking
from vues import next_round
from vues import end_tournament
from vues import menu

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
    tournament = Tournament(name_tournament,place,players,rounds,time,description)
    end_tournament(tournament,date_start_tournament,final_ranking)


choice = menu()
if int(choice) == 1:
    create_tournament()
