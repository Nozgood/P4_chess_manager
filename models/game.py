from models.player import Player

class Game:
    """ Game represents and manage the opposition of 2 players """
    def __init__(
            self,
            player_one_info: Player,
            player_two_info: Player
    ):

        self.player_one_info = player_one_info
        self.player_two_info = player_two_info

    def __json__(self):
        return {
            "playerOneInfo": self.player_one_info,
            "playerTwoInfo": self.player_two_info,
        }

    def give_win_point(self, player: Player):
        """Add a point to the score of the winner player

        :param player: take one player (the winner) as argument
        """
        if self.player_one_info.national_chess_ID == player.national_chess_ID:
            self.player_one_info.score += 1
            return None
        self.player_two_info.score += 1
        return None

    def give_equal_point(self):
        """ Give 0.5 points to both players that play the game. It used when players are tied"""
        self.player_one_info.score += 0.5
        self.player_one_info.score += 0.5
