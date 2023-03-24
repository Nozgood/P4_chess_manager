from player import Player

class Game:
    def __init__(
            self,
            playerOneInfo: Player,
            playerTwoInfo:Player
    ):

        self.playerOneInfo = playerOneInfo
        self.playerTwoInfo = playerTwoInfo

    def giveWinPoint(self, player: Player):
        if self.playerOneInfo.firstName == player.firstName and self.playerOneInfo.lastName == player.lastName:
            self.playerOneInfo.score += 1
            return
        self.playerTwoInfo.score += 1

    def giveEqualPoint(self):
        self.playerOneInfo.score += 0.5
        self.playerTwoInfo.score += 0.5
