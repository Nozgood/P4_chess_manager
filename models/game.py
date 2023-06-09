from models.player import Player


class GamePlayerInfo:
    def __init__(self, player: Player, score=0):
        self.player = player
        self.score = score

    def __str__(self):
        return (
            f"player: {self.player} "
            f"score: {self.score} "
        )

    def __json__(self):
        json_player = self.player.__json__()
        json_score = 0
        if self.score != 0:
            json_score = self.score
        return {
            "player_info": json_player,
            "score": json_score
        }


class Game:
    """ Game represents and manage the opposition of 2 players """
    def __init__(
            self,
            player_one: Player,
            player_two: Player,
            player_one_score=0,
            player_two_score=0,
    ):
        player_one_info = GamePlayerInfo(player_one, player_one_score)
        player_two_info = GamePlayerInfo(player_two, player_two_score)
        self.player_one_info = player_one_info
        self.player_two_info = player_two_info

    def __str__(self):
        return (
            f"  player one info: {self.player_one_info} \n"
            f"  player two info: {self.player_two_info} \n"
        )

    def __json__(self):
        json_player_one = self.player_one_info.__json__()
        json_player_two = self.player_two_info.__json__()
        return {
            "player_one_info": json_player_one,
            "player_two_info": json_player_two,
        }
