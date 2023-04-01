from models.person import Person
import json

filename = "./data/players/players.json"

class Player(Person):
    def __init__(
        self,
        last_name: str,
        first_name: str,
        birth_date: str,
        national_chess_id: str,
        tournament_id="",
        has_played_with=list[str],
        score=0,
        in_tournament=False,
    ):
        super().__init__(first_name, last_name, birth_date)
        self.national_chess_ID = national_chess_id
        self.in_tournament = in_tournament
        self.score = score
        self.tournament_id = tournament_id
        self.has_played_with = has_played_with

    def __json__(self):
        return {
            "lastName": self.last_name,
            "firstName": self.first_name,
            "birthDate": self.birth_date,
            "nationalChessID": self.national_chess_ID,
            "tournamentID": self.tournament_id,
            "hasPlayedWith": self.has_played_with,
            "score": self.score,
            "inTournament": self.in_tournament
        }

    def join_tournament(self, tournament):
        self.in_tournament = True
        self.tournament_id = tournament.ID
        tournament.registeredPlayers.append(self)
        print(f"player {self.first_name} {self.last_name}' successfully registered to the tournament")

    def display_score(self):
        return self.score

    def post(self):
        with open(filename, "r") as file:
            datas = json.load(file)
        json_self = self.__json__()
        datas.append(json_self)
        with open(filename, 'w') as file:
            json.dump(datas, file, indent=4)

    def get(self, nationalChessID: str):
        print(nationalChessID)
        with open(filename, "r") as file:
            datas = json.load(file)
            for player in datas:
                if player["nationalChessID"] == nationalChessID:
                    return player
        print("we didn't found a player with this nationalChessID in our database")

    def list(self):
        with open(filename, "r") as file:
            datas = json.load(file)
            return datas

    def put(self, nationalChessID: str):
        pass
