from models.player import Player

class Game:
    def __init__(
            self,
            playerOneInfo: Player,
            playerTwoInfo: Player
    ):

        self.playerOneInfo = playerOneInfo
        self.playerTwoInfo = playerTwoInfo

    def give_win_point(self, player: Player):
        if self.playerOneInfo.nationalChessID == player.nationalChessID:
            self.playerOneInfo.score += 1
            return
        self.playerTwoInfo.score += 1

    def give_equal_point(self):
        self.playerOneInfo.score += 0.5
        self.playerTwoInfo.score += 0.5
