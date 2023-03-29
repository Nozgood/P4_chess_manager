import random
from datetime import datetime, date

class Turn:
    def __init__(
            self,
            name: str,
            players,
            number_of_games: float,
            startDate: date,
            startHour: datetime.time,
            endHour=None,
            endDate=None,
            allGames=None,
    ):
        self.name = name
        self.players = players
        self.number_of_games = number_of_games
        self.startDate = startDate
        self.endDate = endDate
        self.startHour = startHour
        self.endHour = endHour
        self.allGames = allGames

    def start_turn(self):
        self.startDate = datetime.today()
        self.startHour = datetime.time().strftime("%H:%M:%S")

    def end_turn(self):
        self.endDate = date.today()
        self.endHour = datetime.time().strftime("%H:%M:%S")


    # def create_games_first_turn(self):
    #     self.blend_players_first_turn()
    #     count = 2
    #     self.allGames = [self.players[i:i+count] for i in range(0, len(self.players), count)]

    def update_points(self):
        pass
