from models.game import Game
from datetime import datetime, date

class Turn:
    def __init__(
            self,
            name: str,
            players,
            number_of_games: float,
            all_games: [list[Game]],
            start_date: date,
            start_hour: datetime.time,
            end_hour=None,
            end_date=None,
    ):
        self.name = name
        self.players = players
        self.number_of_games = number_of_games
        self.start_date = start_date
        self.end_date = end_date
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.all_games = all_games

    def __json__(self):
        """Json formatting"""
        return {
            "name": self.name,
            "players": self.players,
            "number_of_games": self.number_of_games,
            "allGames": self.all_games,
            "startDate": self.start_date,
            "startHour": self.start_hour,
            "endHour": self.end_hour,
            "endDate": self.end_date,
        }

    def end_turn(self):
        """manage needed information to end a turn"""
        self.end_date = date.today()
        self.end_hour = datetime.time().strftime("%H:%M:%S")
