from models.turn import Turn
from models.game import Game
from models.player import Player

import uuid
from datetime import datetime
import random

class Tournament:
    """Tournament manages all the needed information, and the needed behaviors about a tournament"""

    def __init__(
            self,
            name: str,
            place: str,
            start_date: datetime.date,
            end_date: datetime.date,
            all_turns: list[Turn],
            registered_players: list[Player],
            description: str,
            number_of_turns=4,
            actual_turn=1
    ):
        self.ID = uuid.uuid1()
        self.name = name
        self.place = place
        self.start_date = start_date.today()
        self.end_date = end_date
        self.all_turns = all_turns
        self.registered_players = registered_players
        self.description = description
        self.number_of_turns = number_of_turns
        self.actual_turn = actual_turn

    def __json__(self):
        """Json formatting"""
        return {
            "Id": self.ID,
            "name": self.name,
            "place": self.place,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "allTurns": self.all_turns,
            "registeredPlayers": self.registered_players,
            "description": self.description,
            "numberOfTurns": self.number_of_turns,
            "actualTurn": self.actual_turn,
        }

    def register_new_player(self, player: Player):
        """Registers a new player to the tournament

        :param player: the player who will be registered at the tournament
        :return:
        """
        for registered_player in self.registered_players:
            if player.national_chess_ID == registered_player.national_chess_ID:
                print("This player has been already registered")
                return
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

    def update_players_by_game(self, game: Game):
        """Takes an ended game and update the informations (score and has_played_with)
        abut the players that played this game

        :param game: a game that is ENDED
        :return:
        """
        self.update_player_score_by_id(game.player_one_info.national_chess_ID, game.player_one_info.score)
        self.update_player_has_played(game.player_two_info.national_chess_ID, game.player_one_info)
        self.update_player_score_by_id(game.player_two_info.national_chess_ID, game.player_two_info.score)
        self.update_player_has_played(game.player_one_info.national_chess_ID, game.player_two_info)

    def update_player_score_by_id(self, nationalChessID: str, new_score: int):
        """Find a player by his chessID and update his score after a game

        :param nationalChessID: the chessID of the player that we wanna find
        :param new_score: the updated score
        """
        player = self.find_player(nationalChessID)
        player.score = new_score
        print("we didn't find a player with this national chess ID in this tournaments")
        return

    def update_player_has_played(self, nationalChessID: str, player: Player):
        """Update the array of players that the player has played against

        :param nationalChessID: the chessID of the player we wanna put in the array of the player
        :param player: the target of update
        """
        opponent = self.find_player(nationalChessID)
        player.has_played_with.append(opponent.national_chess_ID)

    def find_player(self, nationalChessID: str):
        """Find a player in the tournament entries by the chessID. It's a helper

        :param nationalChessID: the chessID of the player we want to find
        """
        for player in self.registered_players:
            if player.national_chess_ID == nationalChessID:
                return player
        print("we didn't find a player with this national chess ID in this tournaments")
        return

    def create_games(self, players: list[Player]):
        """ Create all the games for a turn in the tournament

        :param players: a list of sorted or blended players
        """
        all_games = list[Game]
        for i in range(0, len(players), 2):
            game = players[i:i+2]
            all_games.append(game)
        return all_games

    def create_turn(self):
        """Creates a new turn in the tournament, manage all the needed information"""
        players = list[Player]
        if self.actual_turn == 1:
            players = self.blend_players_first_turn()
        else:
            players = self.sort_players_by_score()
        turn_name = "round " + str(self.actual_turn)
        start_date = datetime.today()
        start_hour = datetime.time().strftime("%H:%M:%S")
        self.check_players_opponents(players)
        all_games = self.create_games(players)
        turn = Turn(turn_name, players, len(all_games), all_games, start_date, start_hour)
        self.all_turns.append(turn)
        return turn

    def check_players_opponents(self, players: list[Player]):
        """Manage the case where two players have already played against

        :param players: list of players
        :return: the list of players that have been checked
        """
        if self.actual_turn == 1:
            print("it's the first turn, we don't need to check who played against who")
            return
        for i in range(0, len(players), 2):
            if i == (len(players)-2):
                break
            if self.find_player_opponent(players[i], players[i+1].national_chess_ID):
                players[i+1], players[i+2] = players[i+2], players[i+1]
        return players

    def find_player_opponent(self, player: Player, national_chess_id: str):
        """check if two players have already played against

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
        if self.actual_turn == self.number_of_turns:
            print("it was the last turn of the tournaments")
            return
        self.actual_turn += 1

    def end_turn(self, turn: Turn):
        """manage that what to be done at the end of a turn : update players score, and update turn number

        :param turn: the turn that is ended
        """
        turn.end_turn()
        for game in turn.all_games:
            self.update_players_by_game(game)
        self.update_actual_turn()

    def post(self):
        pass

    def get(self, tournamentID):
        pass

    def put(self, tournamentID):
        pass
