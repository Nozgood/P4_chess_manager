from models.turn import Turn
from models.game import Game
from models.player import Player

import shortuuid
from datetime import datetime
import json
import random

FILENAME = "./data/tournaments/tournaments.json"


class Tournament:
    """Tournament manages all the needed information, and the needed behaviors about a tournament"""

    def __init__(
            self,
            name: str,
            place: str,
            start_date: datetime.date,
            end_date: datetime.date,
            registered_players: list[Player],
            description: str,
            all_turns: list[Turn],
            number_of_turns=4,
            actual_turn=1,
            ID=None,
    ):
        if ID is None:
            ID = shortuuid.uuid()
        self.ID = ID
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.all_turns = all_turns
        self.registered_players = registered_players
        self.description = description
        self.number_of_turns = number_of_turns
        self.actual_turn = actual_turn

    def __str__(self):
        str_turns, str_players = [], []
        for turn in self.all_turns:
            str_turn = turn.__str__()
            str_turns.append(str_turn)

        joined_turns = "\n".join(str_turns)
        for player in self.registered_players:
            str_player = player.__str__()
            str_players.append(str_player)

        joined_players = "\n".join(str_players)

        return f"id:  {self.ID}\n " \
               f"name:  {self.name}\n " \
               f"place:  {self.place}\n " \
               f"start date:  {self.start_date}\n " \
               f"end date:  {self.end_date}\n " \
               f"all turns:\n  {joined_turns}\n " \
               f"registered players:\n  {joined_players}\n" \
               f"description:  {self.description}\n " \
               f"number of turns:  {self.number_of_turns} \n " \
               f"actual turn:  {self.actual_turn}\n"

    def __json__(self, json_players, json_turns):
        """Json formatting"""
        return {
            "ID": str(self.ID),
            "name": self.name,
            "place": self.place,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "all_turns": json_turns,
            "registered_players": json_players,
            "description": self.description,
            "number_of_turns": self.number_of_turns,
            "actual_turn": self.actual_turn,
        }

    @staticmethod
    def json_games_decoder(json_games: dict):
        formatted_games = []
        for game in json_games:
            player_one = Player.json_player_decoder(game["player_one_info"]["player_info"])
            player_two = Player.json_player_decoder(game["player_two_info"]["player_info"])
            formatted_game = Game(
                player_one=player_one,
                player_two=player_two,
                player_one_score=game["player_one_info"]["score"],
                player_two_score=game["player_two_info"]["score"]
            )
            formatted_games.append(formatted_game)
        return formatted_games

    @staticmethod
    def json_turn_decoder(json_turns: dict):
        formatted_turns = []
        for turn in json_turns:
            formatted_players = Player.json_players_decoder(turn["players"])
            formatted_games = Tournament.json_games_decoder(turn["all_games"])
            formatted_turn = Turn(
                name=turn["name"],
                players=formatted_players,
                number_of_games=turn["number_of_games"],
                all_games=formatted_games,
                start_date=turn["start_date"],
                start_hour=turn["start_hour"],
                end_hour=turn["end_hour"],
                end_date=turn["end_date"],
            )
            formatted_turns.append(formatted_turn)
        return formatted_turns

    @staticmethod
    def json_tournament_decoder(json_tournament):
        formatted_turns = Tournament.json_turn_decoder(json_tournament["all_turns"])
        formatted_players = Player.json_players_decoder(json_tournament["registered_players"])
        formatted_tournament = Tournament(
            ID=json_tournament["ID"],
            name=json_tournament["name"],
            place=json_tournament["place"],
            start_date=json_tournament["start_date"],
            end_date=json_tournament["end_date"],
            description=json_tournament["description"],
            number_of_turns=json_tournament["number_of_turns"],
            actual_turn=json_tournament["actual_turn"],
            all_turns=formatted_turns,
            registered_players=formatted_players,
        )
        return formatted_tournament

    @staticmethod
    def json_tournaments_decoder(json_tournaments: list):
        formatted_tournaments = []
        for tournament in json_tournaments:
            formatted_tournament = Tournament.json_tournament_decoder(tournament)
            formatted_tournaments.append(formatted_tournament)

        return formatted_tournaments

    def register_new_player(self, player: Player):
        """Registers a new player to the tournament

        :param player: the player who will be registered at the tournament
        :return:
        """
        for registered_player in self.registered_players:
            if player.national_chess_ID == registered_player.national_chess_ID:
                print("This player has been already registered")
                return None
        player.in_tournament = True
        player.tournament_id = self.ID
        self.registered_players.append(player)

    def blend_players_first_turn(self):
        """Blend players for the first turn of the tournament"""
        blended_players = self.registered_players
        random.shuffle(blended_players)
        return blended_players

    def sort_players_by_score(self):
        """Sort players by their score, in ascending order"""
        sorted_players = self.registered_players
        sorted_players.sort(key=Player.display_score, reverse=False)
        return sorted_players

    def find_player(self, nationalChessID: str):
        """
        Find a player in the tournament entries by the chessID. It's a helper

        :param nationalChessID: the chessID of the player we want to find
        """
        for player in self.registered_players:
            if player.national_chess_ID == nationalChessID:
                return player
        print("we didn't find a player with this national chess ID in this tournaments")

    def create_games(self, players: list[Player]):
        """ Create all the games for a turn in the tournament

        :param players: a list of sorted or blended players
        """
        all_games = []
        for i in range(0, len(players), 2):
            game = Game(players[i], players[i+1])
            all_games.append(game)
        return all_games

    def create_turn(self) -> Turn:
        """
        Creates a new turn in the tournament, manage all the needed information
        """
        if self.actual_turn == 1:
            players = self.blend_players_first_turn()
        else:
            players = self.sort_players_by_score()
        turn_name = "round " + str(self.actual_turn)
        start_date = datetime.today()
        start_hour = datetime.now().strftime("%H:%M:%S")
        self.check_players_opponents(players)
        all_games = self.create_games(players)
        turn = Turn(turn_name, players, len(all_games), all_games, start_date, start_hour)
        self.all_turns.append(turn)
        return turn

    def check_players_opponents(self, players: list[Player]):
        """
        Manage the case where two players have already played against

        :param players: list of players
        :return: the list of players that have been checked
        """
        if self.actual_turn == 1:
            print("it's the first turn, we don't need to check who played against who")
            return None
        for i in range(0, len(players), 2):
            if i == (len(players)-2):
                break
            if self.find_player_opponent(players[i], players[i+1].national_chess_ID) is True:
                players[i+1], players[i+2] = players[i+2], players[i+1]
        return players

    def find_player_opponent(self, player: Player, national_chess_id: str):
        """
        check if two players have already played against

        :param player: the player that we want check opponent
        :param national_chess_id: the chessID of the player we want to find in the array
        :return: Boolean, true if they have, false if not
        """
        for opponent_chess_id in player.has_played_with:
            if opponent_chess_id == national_chess_id:
                return True
        return False

    def update_actual_turn(self):
        """Update the number of the turn we are playing"""
        print("update actual turn: " + str(self.actual_turn) + str(self.number_of_turns))
        if self.actual_turn == self.number_of_turns:
            print("it was the last turn of the tournament")
            return False
        self.actual_turn += 1
        return True

    def end_turn(self, turn: Turn):
        """manage that what to be done at the end of a turn : update players score, and update turn number

        :param turn: the turn that is ended
        """
        turn.end_turn()
        self.registered_players = turn.players

    @staticmethod
    def json_players(players: list[Player]):
        json_players = []
        for player in players:
            json_player = player.__json__()
            json_players.append(json_player)
        return json_players

    @staticmethod
    def json_turns(turns: list[Turn]):
        json_turns = []
        for turn in turns:
            json_turn = turn.__json__()
            json_turns.append(json_turn)
        return json_turns

    def json_turns_and_players(self, players: list[Player], turns: list[Turn]):
        return self.json_players(players), self.json_turns(turns)

    def post(self, json_players, json_turns):
        with open(FILENAME, "r") as file:
            datas = json.load(file)
        json_self = self.__json__(json_players, json_turns)
        datas.append(json_self)
        with open(FILENAME, 'w') as file:
            json.dump(datas, file, indent=4)
        print(f"tournament created, id of the tournament: {self.ID}")

    @staticmethod
    def get(tournamentID: str):
        with open(FILENAME, "r") as file:
            datas = json.load(file)
            for tournament in datas:
                if tournament["ID"] == tournamentID:
                    formatted_tournament = Tournament.json_tournament_decoder(tournament)
                    return formatted_tournament
        print("we didn't find a tournament with this id in our database")
        return None

    @staticmethod
    def list():
        with open(FILENAME, "r") as file:
            all_tournaments = json.load(file)
        return all_tournaments

    def put(self, tournamentID: str, json_players, json_turns):
        new_information = self.__json__(json_players, json_turns)
        old_information = self.get(tournamentID)
        if old_information is None:
            print("this tournament doesn't exist in our database, please create it before trying to update")
            return None
        json_list_tournaments = Tournament.list()
        formatted_tournament_list = Tournament.json_tournaments_decoder(json_list_tournaments)
        index_of_tournament = None
        for formatted_tournament in formatted_tournament_list:
            if formatted_tournament.ID == old_information.ID:
                index_of_tournament = formatted_tournament_list.index(formatted_tournament)
            else:
                continue
        if index_of_tournament is None:
            print("an error occurred during the update of the tournaments database")
            return None
        json_list_tournaments[index_of_tournament] = new_information
        with open(FILENAME, "w") as file:
            json.dump(json_list_tournaments, file, indent=4)
        print("tournament successfully updated")
        return None
