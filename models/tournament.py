from models.turn import Turn
from models.player import Player

import uuid
from datetime import datetime
import random

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

    def register_new_player(self, player: Player):
        for registeredPlayer in self.registeredPlayers:
            if player.nationalChessID == registeredPlayer.nationalChessID:
                print("This player is already registered")
                return
        self.registeredPlayers.append(player)

    def blend_players_first_turn(self):
        blended_players = self.registeredPlayers
        random.shuffle(blended_players)
        return blended_players

    def create_first_turn(self):
        if self.actualTurn != 1:
            print("This is not the first turn")
            return
        blended_players = self.blend_players_first_turn()
        turn_name = "round " + str(self.actualTurn)
        start_date = datetime.today()
        start_hour = datetime.time().strftime("%H:%M:%S")
        number_of_games = len(self.registeredPlayers) / 2
        turn = Turn(turn_name, blended_players, number_of_games, start_date, start_hour)
        self.turns.append(turn)
        return turn

    def sort_players_by_score(self):
        sorted_players = self.registeredPlayers
        sorted_players.sort(key=Player.display_score, reverse=False)
        return sorted_players

    def create_turn(self):
        sorted_players = self.sort_players_by_score()
        turn_name = "round " + str(self.actualTurn)
        start_date = datetime.today()
        start_hour = datetime.time().strftime("%H:%M:%S")
        turn = Turn(turn_name, sorted_players, start_date, start_hour)
        self.turns.append(turn)
        return turn

    def post(self):
        pass

    def get(self, tournamentID):
        pass

    def put(self, tournamentID):
        pass
