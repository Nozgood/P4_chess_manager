from models.person import Person
import json

filename = "./data/players/players.json"

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

    def __json__(self):
        return {
            "lastName":self.lastName,
            "firstName":self.firstName,
            "birthDate":self.birthDate,
            "nationalChessID":self.nationalChessID,
            "tournamentID":self.tournamentID,
            "hasPlayedWith":self.hasPlayedWith,
            "score":self.score,
            "inTournament":self.inTournament
        }

    def join_tournament(self, tournament):
        self.inTournament = True
        self.tournamentID = tournament.ID
        tournament.registeredPlayers.append(self)
        print(f"player {self.firstName} {self.lastName}' successfully registered to the tournament")

    def display_score(self):
        return self.score

    def post(self):
        with open(filename, "r") as file:
            datas = json.load(file)
            print(datas)
            json_self = self.__json__()
        datas.append(json_self)
        with open(filename, 'w') as file:
            json.dump(datas, file, indent=4)

    def get(self, nationalChesID: str):
        pass

    def put(self, nationalChessID: str):
        pass
