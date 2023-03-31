from models.person import Person

class Player(Person):
    def __init__(
        self,
        lastName: str,
        firstName: str,
        birthDate: str,
        nationalChessID: str,
        tournamentID="",
        hasPlayedWith=list[str],
        score=0,
        inTournament=False,
    ):
        super().__init__(firstName, lastName, birthDate)
        self.nationalChessID = nationalChessID,
        self.inTournament = inTournament
        self.score = score
        self.tournamentID = tournamentID
        self.hasPlayedWith = hasPlayedWith

    def join_tournament(self, tournament):
        self.inTournament = True
        self.tournamentID = tournament.ID
        tournament.registeredPlayers.append(self)
        print(f"player {self.firstName} {self.lastName}' successfully registered to the tournament")

    def display_score(self):
        return self.score

    def post(self):
        pass

    def get(self, nationalChesID: str):
        pass

    def put(self, nationalChessID: str):
        pass
