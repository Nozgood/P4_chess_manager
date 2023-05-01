import datetime

from player import Player
from tournament import Tournament
from turn import Turn
from game import Game


class Report:
    def __init__(
            self,
            players: list[Player],
            tournaments: list[Tournament],
            nameOfGivenTournament: str,
            dateOfGivenTournament: datetime.date,
            playersInGivenTournament: list[Player],
            allTurnsInGivenTournament: list[Turn],
            allGamesInGivenTournament: list[Game]
    ):
        self.players = players
        self.tournaments = tournaments
        self.nameOfGivenTournament = nameOfGivenTournament
        self.playersInGivenTournament = dateOfGivenTournament
        self.playersInGivenTournament = playersInGivenTournament
        self.allTurnsInGivenTournament = allTurnsInGivenTournament
        self.allGamesInGivenTournament = allGamesInGivenTournament

    def generate_report(self):
        pass
