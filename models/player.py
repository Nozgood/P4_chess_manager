from models.person import Person
import json
from collections import namedtuple

FILENAME = "./data/players/players.json"

class Player(Person):
    """Player, a legacy of Person, manage all the needed information for a player"""
    def __init__(
        self,
        last_name: str,
        first_name: str,
        birth_date: str,
        national_chess_id: str,
        in_tournament=False,
        tournament_id="",
        has_played_with=list[str],
        score=0,
    ):
        super().__init__(first_name, last_name, birth_date)
        self.national_chess_ID = national_chess_id
        self.in_tournament = in_tournament
        self.score = score
        self.tournament_id = tournament_id
        self.has_played_with = has_played_with

    def __json__(self):
        """Format an object of type player in json (to be used in db)"""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": str(self.birth_date),
            "national_chess_ID": self.national_chess_ID,
            "tournament_ID": self.tournament_id,
            "has_played_with": self.has_played_with,
            "score": self.score,
            "in_tournament": self.in_tournament
        }

    def display_score(self):
        return self.score

    @staticmethod
    def json_player_decoder(value: dict):
        return namedtuple('Player', value.keys())(*value.values())

    def post(self):
        with open(FILENAME, "r") as file:
            datas = json.load(file)
        json_self = self.__json__()
        datas.append(json_self)
        with open(FILENAME, 'w') as file:
            json.dump(datas, file, indent=4)
        print("player successfully registered in the database")

    @staticmethod
    def get(national_chess_ID: str):
        with open(FILENAME, "r") as file:
            datas = json.load(file, object_hook=Player.json_player_decoder)
            for player in datas:
                if player.national_chess_ID == national_chess_ID:
                    return player
        print("we didn't find a player with this nationalChessID in our database")
        return None

    def list(self):
        with open(FILENAME, "r") as file:
            datas = json.load(file, object_hook=Player.json_player_decoder())
        return datas

    def put(self, nationalChessID: str):
        new_information = self.__json__()
        old_information = self.get(nationalChessID)
        if old_information is None:
            return None
        all_players = self.list()
        index_of_player = all_players.index(old_information)
        all_players[index_of_player] = new_information
        with open(FILENAME, "w") as file:
            json.dump(all_players, file, indent=4)
        print("player successfully updated")
        return None
