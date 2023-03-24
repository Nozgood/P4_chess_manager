from turn import Turn
from player import Player
import uuid
import datetime

class Tournament:
    def __init__(
            self,
            name: str,
            place: str,
            startDate: datetime.date,
            endDate: datetime.date,
            turns: list[Turn],
            registeredPlayers: list[Player],
            description: str,
            numberOfTurns=4,
            actualTurn=1
    ):
        self.ID = uuid.uuid1()
        self.name = name
        self.place = place
        self.startDate = startDate.today()
        self.endDate = endDate
        self.actualTurn = actualTurn
        self.turns = turns
        self.registeredPlayers = registeredPlayers
        self.description = description
        self.numberOfTurns = numberOfTurns

    def generate_turn(self):
        pass

    def sort_players_by_points(self):
        pass

    def associate_players(self):
        pass

    def choose_players_with_same_points(self):
        pass

    def post(self):
        pass

    def get(self, tournamentID):
        pass

    def put(self, tournamentID):
        pass
