from models.tournament import Tournament
from models.player import Player
from views.view import View

class Controller:
    def __init__(self, view: View):
        self.view = view

    def run(self):
        running = True
        """
        run manages the logical running of the main menu of the program, it returns error if there is during the
        execution of the program
        """
        while running:
            menu_selection = self.view.input_main_menu()
            if menu_selection == 1:
                self.register_player_in_db()
            if menu_selection == 2:
                self.create_tournament()
            if menu_selection == 3:
                print("See You ASAP...")
                running = False

    def create_tournament(self):
        tournament_name = self.view.input_tournament_name()
        tournament_place = self.view.input_tournament_place()
        tournament_start_date = self.view.input_tournament_start_date()
        tournament_end_date = self.view.input_tournament_end_date()
        tournament_description = self.view.input_tournament_description()
        tournament_registered_players = []
        tournament = Tournament(
            name=tournament_name,
            place=tournament_place,
            start_date=tournament_start_date,
            end_date=tournament_end_date,
            description=tournament_description,
            registered_players=tournament_registered_players,
        )
        tournament.post()
        return tournament

    def get_player(self):
        player_id = self.view.input_tournament_register_players()
        player_to_get = Player.get(player_id)
        return player_to_get

    def register_player_in_db(self):
        player_chess_id = self.view.input_player_chess_id()
        player_first_name = self.view.input_player_first_name()
        player_last_name = self.view.input_player_last_name()
        player_birth_date = self.view.input_player_birth_date()
        player_to_save = Player(
            first_name=player_first_name,
            last_name=player_last_name,
            national_chess_id=player_chess_id,
            birth_date=player_birth_date,
            has_played_with=[],
        )
        player_to_save.post()
        return player_to_save
