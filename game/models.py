class Player:
    def __init__(self, forename, name, date, sex, rank):
        self.name = str(name)
        self.forename = str(forename)
        self.date = date
        self.sex = sex
        self.rank = int(rank)

    def __lt__(self, other):
        return self.rank < other.rank


class Tournament:

    date_start = str()
    date_end = str()

    def __init__(self, name, place, time, players, rounds, description):
        self.name = name
        self.place = place
        self.nb_rounds = 4
        self.players = players
        self.rounds = rounds
        self.time = time
        self.description = str(description)


class Round:

    date_start = str()
    date_end = str()

    def __init__(self, list_games, name):
        self.list_games = list_games
        self.name = name


class Game:
    def __init__(self, p1, p2, score_p1, score_p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = score_p1
        self.score_p2 = score_p2
