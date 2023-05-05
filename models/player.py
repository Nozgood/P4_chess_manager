from models.person import Person
import json

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

    def __str__(self):
        return f"  first name: {self.first_name} \n" \
               f"  last name: {self.last_name} \n" \
               f"  birth date: {self.birth_date} \n" \
               f"  national chess id: {self.national_chess_ID} \n" \
               f"  in tournament ?: {self.in_tournament} \n" \
               f"  has played with: {self.has_played_with} \n" \
               f"  score: {self.score} \n" \


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
    def json_player_decoder(json_player: dict):
        formatted_player = Player(
            last_name=json_player["last_name"],
            first_name=json_player["first_name"],
            birth_date=json_player["birth_date"],
            national_chess_id=json_player["national_chess_ID"],
            has_played_with=json_player["has_played_with"],
            score=json_player["score"],
            in_tournament=json_player["in_tournament"]
        )
        return formatted_player

    @staticmethod
    def json_players_decoder(json_players: list):
        formatted_players = []
        for player in json_players:
            formatted_player = Player(
                last_name=player["last_name"],
                first_name=player["first_name"],
                birth_date=player["birth_date"],
                national_chess_id=player["national_chess_ID"],
                has_played_with=player["has_played_with"],
                score=player["score"],
                in_tournament=player["in_tournament"]
            )
            formatted_players.append(formatted_player)
        return formatted_players

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
            datas = json.load(file)
            formatted_players = Player.json_players_decoder(datas)
            for player in formatted_players:
                if player.national_chess_ID == national_chess_ID:
                    return player
        print("we didn't find a player with this nationalChessID in our database")
        return None

    @staticmethod
    def list() -> list:
        with open(FILENAME, "r") as file:
            datas = json.load(file)
        return datas

    def put(self, nationalChessID: str):
        new_information = self.__json__()
        old_information = self.get(nationalChessID)
        if old_information is None:
            print("this player doesn't exist in our database, please create him before trying to update")
            return None
        json_players = self.list()
        formatted_players = Player.json_players_decoder(json_players)
        index_of_player = None
        for formatted_player in formatted_players:
            if formatted_player.national_chess_ID == old_information.national_chess_ID:
                index_of_player = formatted_players.index(formatted_player)
            else:
                continue
        if index_of_player is None:
            print("an error occurred during the update of the tournaments database")
            return None
        json_players[index_of_player] = new_information
        with open(FILENAME, "w") as file:
            json.dump(json_players, file, indent=4)
        print("player successfully updated")
        return None
