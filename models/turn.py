from models.game import Game
from datetime import datetime, date


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

        return (
            f"  name: {self.name} \n"
            f"  players:{joined_players} \n"
            f"  number of games:{self.number_of_games} \n"
            f"  start date:{self.start_date} \n"
            f"  end date:{self.end_date} \n"
            f"  start hour:{self.start_hour} \n"
            f"  end hour:{self.end_hour} \n"
            f"  all games:{joined_games} \n"
        )

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
            "end_hour": str(self.end_hour),
            "end_date": str(self.end_date),
        }

    def end_turn(self):
        """manage needed information to end a turn"""
        self.end_date = date.today()
        self.end_hour = datetime.now().strftime("%H:%M:%S")

    def update_players_by_game(self, game: Game):
        """Takes an ended game and update the information (score and has_played_with)
        abut the players that played this game

        :param game: a game that is ENDED
        :return:
        """
        self.update_player_has_played_with(
            game.player_one_info.player.national_chess_ID,
            game.player_two_info.player.national_chess_ID
        )
        self.update_player_score_by_id(
            game.player_one_info.player.national_chess_ID,
            game.player_one_info.score
        )
        self.update_player_has_played_with(
            game.player_two_info.player.national_chess_ID,
            game.player_one_info.player.national_chess_ID
        )
        self.update_player_score_by_id(
            game.player_two_info.player.national_chess_ID,
            game.player_two_info.score
        )

    def update_player_has_played_with(self, player_one_id, player_two_id: str):
        """Update the array of players that the player has played against

        :param player_one_id: the chessID of the player we want to update
        :param player_two_id: the chess id we want to put in the array of the player_one (player_one_id)
        """
        player_index = self.find_player_index(player_one_id)
        self.players[player_index].has_played_with.append(player_two_id)

    def find_player(self, national_chess_id: str):
        """
        Find a player in the tournament entries by the chessID. It's a helper

        :param national_chess_id: the chessID of the player we want to find
        """
        for player in self.players:
            if player.national_chess_ID == national_chess_id:
                return player
        print("we didn't find a player with this national chess ID in this tournaments")

    def find_player_index(self, national_chess_id):
        for player in self.players:
            if player.national_chess_ID == national_chess_id:
                return self.players.index(player)

    def update_player_score_by_id(self, national_chess_id: str, new_score: int):
        """Find a player by his chessID and update his score after a game

        :param national_chess_id: the chessID of the player that we wanna find
        :param new_score: the updated score
        """
        player = self.find_player(national_chess_id)
        if player is None:
            print("we didn't find a player with this national chess ID in this tournament")
            return None
        player.score += new_score
