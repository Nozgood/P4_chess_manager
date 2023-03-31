import datetime

from models.player import Player
from models.tournament import Tournament

player_one = Player("safi", "nowfeel", "23/02/1999", "AB123", "", "", 1, True)
player_two = Player("dupont", "jean", "23/02/1999", "AB456", "", "", 2, True)
player_three = Player("luc", "charles", "23/02/1999", "AB789", "", "", 3, True)
player_four = Player("jacques", "paul", "23/02/1999", "AB101112", "", "", 4, True)


players = [player_one, player_two, player_three, player_four]

test_tournament = Tournament("test", "valenciennes", datetime.date.today(), datetime.date.today(), [], players, "test")

player_one.hasPlayedWith = [player_two.nationalChessID]

test_tournament.actualTurn = 2
test_tournament.check_players_opponents(test_tournament.registeredPlayers)

for player in test_tournament.registeredPlayers:
    print("players after checking opponents: {}".format(player.nationalChessID))
