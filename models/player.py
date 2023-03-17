class Player:
    def __init__(self, lastName: str,firstName: str, birthDate: str,nationalChessID: str, inTournament=None):
        self.lastName = lastName,
        self.firstName = firstName,
        self.birthDate = birthDate,
        self.nationalChessID = nationalChessID,
        self.inTournament = inTournament

    def join_tournament(self, tournamentID: int):
        self.inTournament = tournamentID
        print(f"player {self.firstName} {self.lastName}' successfully registered to the tournament")
