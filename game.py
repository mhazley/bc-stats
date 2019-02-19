class Player:

    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number


class Team:

    def __init__(self, league: str, name: str):
        self.league = league
        self.name = name
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def get_player(self, number):
        for player in self.players:
            if player.number == number:
                return player
        return None

    def print_team(self):
        for player in self.players:
            print(player.number, player.name)

class Score:

    def __init__(self):
        self.blockers = []
        self.jammer = None
        self.points = 0
        self.lost = False
        self.lead = False
        self.call = False
        self.inj = False
        self.ni = False

class Jam:

    def __init__(self, home_score: Score, away_score: Score ):
        self.home_score = home_score
        self.away_score = away_score


class Game:

    def __init__(self):
            self.jams = []

    def add_jam(self, jam: Jam):
        self.jams.append((jam))

