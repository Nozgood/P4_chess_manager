import datetime

from models.player import Player
from models.tournament import Tournament

player_one = Player(
    last_name='Safi',
    first_name='Nowfeel',
    birth_date='12/02/1999',
    national_chess_id='AB123',
    in_tournament=False,
    tournament_id="",
    has_played_with=[],
    score=0,
)
player_two = Player(
    last_name='Dupont',
    first_name='Jean',
    birth_date='01/01/1999',
    national_chess_id='AB456',
    in_tournament=False,
    tournament_id="",
    has_played_with=[],
    score=0,
)
player_three = Player(
    last_name='Luc',
    first_name='Charles',
    birth_date='02/02/1999',
    national_chess_id='AB789',
    in_tournament=False,
    tournament_id="",
    has_played_with=[],
    score=0,
)
player_four = Player(
    last_name='Paul',
    first_name='Jacques',
    birth_date='03/03/1999',
    national_chess_id='AB101112',
    in_tournament=False,
    tournament_id="",
    has_played_with=[],
    score=0,
)

player_two_found = player_two.get(player_two.national_chess_ID)
print(player_two_found)
#
#
# players = [player_one, player_two, player_three, player_four]
#
# test_tournament = Tournament("test", "valenciennes", datetime.date.today(), datetime.date.today(), [], players, "test")
#
# player_one.hasPlayedWith = [player_two.nationalChessID]
#
# test_tournament.actualTurn = 2
# test_tournament.check_players_opponents(test_tournament.registeredPlayers)
#
# for player in test_tournament.registeredPlayers:
#     print("players after checking opponents: {}".format(player.nationalChessID))
