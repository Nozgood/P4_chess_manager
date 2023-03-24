import random
from datetime import datetime, date

from player import Player
from game import Game


class Turn:
    def __init__(
            self,
            name: str,
            players: list[Player],
            allGames: list[Game],
            startDate: date,
            endDate: date,
            startHour: datetime.time,
            endHour: datetime.time):
        self.name = name
        self.players = players
        self.allGames = allGames
        self.startDate = startDate
        self.endDate = endDate
        self.startHour = startHour
        self.endHour = endHour

    def start_turn(self):
        self.startDate = datetime.today()
        self.startHour = datetime.time().strftime("%H:%M:%S")

    def end_turn(self):
        self.endDate = date.today()
        self.endHour = datetime.time().strftime("%H:%M:%S")

    def blend_players_first_turn(self):
        random.shuffle(self.players)
        return self.players

    def create_games_first_turn(self):
        self.blend_players_first_turn()
        count = 2
        self.allGames = [self.players[i:i+count] for i in range(0, len(self.players), count)]

    def update_points(self):
        pass

