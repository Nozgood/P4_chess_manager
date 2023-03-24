from person import Person
from tournament import Tournament

class Player(Person):
    def __init__(
        self,
        lastName: str,
        firstName: str,
        birthDate: str,
        nationalChessID: str,
        tournamentID="",
        score=0,
        inTournament=False
    ):
        super().__init__(firstName, lastName, birthDate)
        self.nationalChessID = nationalChessID,
        self.inTournament = inTournament
        self.score = score
        self.tournamentID = tournamentID

    def join_tournament(self, tournament: Tournament):
        self.inTournament = True
        self.tournamentID = tournament.ID
        tournament.registeredPlayers.append(self)
        print(f"player {self.firstName} {self.lastName}' successfully registered to the tournament")

    def post(self):
        pass

    def get(self, nationalChesID: str):
        pass

    def put(self, nationalChessID: str):
        pass
