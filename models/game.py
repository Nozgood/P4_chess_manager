from models.player import Player

class GamePlayerInfo:
    def __init__(self, player: Player, score=0):
        self.player = player
        self.score = score

    def __json__(self):
        json_player = self.player.__json__()
        print(f"score of player in match: {self.score}")
        return {
            "player_info": json_player,
            "score": self.score or 0
        }
class Game:
    """ Game represents and manage the opposition of 2 players """
    def __init__(
            self,
            player_one: Player,
            player_two: Player,
    ):
        player_one_info = GamePlayerInfo(player_one)
        player_two_info = GamePlayerInfo(player_two)
        self.player_one_info = player_one_info
        self.player_two_info = player_two_info

    def __json__(self):
        json_player_one = self.player_one_info.__json__()
        json_player_two = self.player_two_info.__json__()
        return {
            "player_one_info": json_player_one,
            "player_two_info": json_player_two,
        }

    def give_win_point(self, player: Player):
        """Add a point to the score of the winner player

        :param player: take one player (the winner) as argument
        """
        if self.player_one_info.player.national_chess_ID == player.national_chess_ID:
            self.player_one_info.score += 1
            return None
        self.player_two_info.score += 1
        return None

    def give_equal_point(self):
        """ Give 0.5 points to both players that play the game. It used when players are tied"""
        self.player_one_info.score += 0.5
        self.player_one_info.score += 0.5
