import datetime

from models.player import Player
from models.tournament import Tournament
from views.view import View
from controllers.controller import Controller

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
all_players = [player_one, player_two, player_three, player_four]

tournament = Tournament(
    name="test",
    place="Saint-Saulve",
    start_date=datetime.date.today(),
    end_date=datetime.date.today(),
    registered_players=all_players,
    all_turns=[],
    description="test tournament"
)

view = View()
controller = Controller(view)
controller.run()
