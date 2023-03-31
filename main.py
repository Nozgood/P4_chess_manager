import datetime

from models.player import Player
from models.tournament import Tournament

player_one = Player("safi", "nowfeel", "23/02/1999", "AB123", "", 2, True)
player_two = Player("dupont", "jean", "23/02/1999", "AB456", "", 3, True)
player_three = Player("luc", "charles", "23/02/1999", "AB789", "", 1, True)

players = [player_one, player_two, player_three]

test_tournament = Tournament("test", "valenciennes", datetime.date.today(), datetime.date.today(), [], players, "test")
for player in test_tournament.registeredPlayers:
    print("players before blending: {}".format(player.nationalChessID))

test_tournament.blend_players_first_turn()
for player in test_tournament.registeredPlayers:
    print("players after blending: {}".format(player.nationalChessID))

