import datetime

from models.tournament import Tournament
from models.turn import Turn
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
                self.resume_tournament()
            if menu_selection == 4:
                print("See You ASAP...")
                running = False

    def create_tournament(self):
        """
        create_tournament manage all the necessaries information to create a tournament and store it in database
        :return: the new instance of tournament that has been created
        """
        """
        tournament_number_of_players = self.view.input_tournament_number_of_players()
        tournament_registered_players = self.register_players_in_tournament(tournament_number_of_players)
        json_players = []
        for player in tournament_registered_players:
            json_player = self.json_player(player)
            json_players.append(json_player)
            
        json_players = Tournament.json_players(tournament_registered_players)
        tournament_number_of_turns = self.view.input_tournament_number_of_turns()
        tournament_name = self.view.input_tournament_name()
        tournament_place = self.view.input_tournament_place()
        tournament_start_date = self.view.input_tournament_start_date()
        tournament_end_date = self.view.input_tournament_end_date()
        tournament_description = self.view.input_tournament_description()
        """

        tournament_number_of_players = 2
        tournament_registered_players = self.register_players_in_tournament(tournament_number_of_players)
        json_players = []
        for player in tournament_registered_players:
            json_player = self.json_player(player)
            json_players.append(json_player)

        tournament = Tournament(
            name="test",
            place="test",
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            description="test",
            registered_players=tournament_registered_players,
            number_of_turns=1,
            actual_turn=1,
            all_turns=[],
        )
        tournament.create_turn()
        json_turns = []
        for turn in tournament.all_turns:
            json_turn = self.json_turn(turn)
            json_turns.append(json_turn)
        tournament.post(json_players, json_turns)
        return tournament

    def register_players_in_tournament(self, number_of_players: int):
        slice_of_players = []
        count = 1
        while count <= number_of_players:
            player = self.get_player()
            slice_of_players.append(player)
            count += 1
        return slice_of_players

    def get_player(self):
        player_id = self.view.input_tournament_register_player()
        player_to_get = Player.get(player_id)
        player = Player(
            last_name=player_to_get.last_name,
            first_name=player_to_get.first_name,
            birth_date= player_to_get.birth_date,
            national_chess_id=player_to_get.national_chess_ID,
            has_played_with=[],
        )
        return player

    @staticmethod
    def json_player(player: Player):
        json_player = player.__json__()
        return json_player

    @staticmethod
    def json_turn(turn: Turn):
        json_turn = turn.__json__()
        return json_turn

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

    def resume_tournament(self):
        tournament_id = self.view.input_get_tournament_id()
        tournament = Tournament.get(tournament_id)
        print(f"test: {tournament.all_turns}")
        print(f"test: {type(tournament.all_turns[0])}")
        print(f"turn type:{type(tournament.all_turns[0])}")
        if tournament is None:
            return None
        self.view.display_tournaments_turn(tournament.all_turns[0])
        self.view.display_tournament_match("prout")


