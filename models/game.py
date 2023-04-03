from models.player import Player

class Game:
    """ Game represents and manage the opposition of 2 players """
    def __init__(
            self,
            playerOneInfo: Player,
            playerTwoInfo: Player
    ):

        self.playerOneInfo = playerOneInfo
        self.playerTwoInfo = playerTwoInfo

    def give_win_point(self, player: Player):
        """Add a point to the score of the winner player

        :param player: take one player (the winner) as argument
        """
        if self.playerOneInfo.national_chess_ID == player.national_chess_ID:
            self.playerOneInfo.score += 1
            return
        self.playerTwoInfo.score += 1

    def give_equal_point(self):
        """ Give 0.5 points to both players that play the game. It used when players are tied"""
        self.playerOneInfo.score += 0.5
        self.playerTwoInfo.score += 0.5
