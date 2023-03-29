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

    def end_turn(self):
        self.endDate = date.today()
        self.endHour = datetime.time().strftime("%H:%M:%S")
