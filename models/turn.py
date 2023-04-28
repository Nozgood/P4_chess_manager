from models.game import Game
from datetime import datetime, date
from collections import namedtuple
import json
import uuid

FILENAME = "./data/turns/turns.json"

class Turn:
    def __init__(
            self,
            name: str,
            players,
            number_of_games: float,
            all_games: list[Game],
            start_date: date,
            start_hour: datetime.time,
            end_hour=None,
            end_date=None,
    ):
        self.name = name
        self.players = players
        self.number_of_games = number_of_games
        self.start_date = start_date
        self.end_date = end_date
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.all_games = all_games

    def __str__(self):
        str_players, str_games = [], []
        for player in self.players:
            str_player = player.__str__()
            str_players.append(str_player)

        joined_players = "\n".join(str_players)

        for game in self.all_games:
            str_game = game.__str__()
            str_games.append(str_game)

        joined_games = "\n".join(str_games)

        return f"  name: {self.name} \n" \
               f"  players:{joined_players} \n"\
               f"  number of games:{self.number_of_games} \n"\
               f"  start date:{self.start_date} \n"\
               f"  end date:{self.end_date} \n"\
               f"  start hour:{self.start_hour} \n"\
               f"  end hour:{self.end_hour} \n"\
               f"  all games:{joined_games} \n"\

    def __json__(self):
        """Json formatting"""

        json_players = []
        json_games = []

        for player in self.players:
            json_player = player.__json__()
            json_players.append(json_player)

        for game in self.all_games:
            json_game = game.__json__()
            json_games.append(json_game)
        return {
            "name": self.name,
            "players": json_players,
            "number_of_games": self.number_of_games,
            "all_games": json_games,
            "start_date": str(self.start_date),
            "start_hour": str(self.start_hour),
            "end_hour": self.end_hour,
            "end_date": self.end_date,
        }

    def end_turn(self):
        """manage needed information to end a turn"""
        self.end_date = date.today()
        self.end_hour = datetime.time().strftime("%H:%M:%S")

    def json_turn_decoder(self, value: dict):
        return namedtuple('Turn', value.keys())(*value.values())

    def post(self):
        with open(FILENAME, "r") as file:
            datas = json.load(file)
        json_self = self.__json__()
        datas.append(json_self)
        with open(FILENAME, 'w') as file:
            json.dump(datas, file, indent=4)

    def get(self, turn_ID: str):
        with open(FILENAME, "r") as file:
            datas = json.load(file, object_hook=self.json_turn_decoder)
            for turn in datas:
                if turn_ID == turn_ID:
                    return turn
        print("we didn't find a player with this nationalChessID in our database")
        return None

    def list(self):
        with open(FILENAME, "r") as file:
            datas = json.load(file, object_hook=self.json_turn_decoder)
        return datas

    def put(self, turn_ID: str):
        new_information = self.__json__()
        old_information = self.get(turn_ID)
        if old_information is None:
            return None
        all_turns = self.list()
        index_of_player = all_turns.index(old_information)
        all_turns[index_of_player] = new_information
        with open(FILENAME, "w") as file:
            json.dump(all_turns, file, indent=4)
        print("turn successfully updated")
        return None
