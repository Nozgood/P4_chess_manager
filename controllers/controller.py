import datetime

from models.tournament import Tournament
from models.turn import Turn
from models.game import Game
from models.player import Player
from views.view import View
from typing import Optional

class Controller:
    def __init__(self, view: View):
        self.view = view

    @staticmethod
    def json_player(player: Player):
        json_player = player.__json__()
        return json_player

    @staticmethod
    def json_turn(turn: Turn):
        json_turn = turn.__json__()
        return json_turn

    def run(self):
        """
        run manages the logical running of the main menu of the program, it returns error if there is during the
        execution of the program
        """
        running = True
        while running:
            menu_selection = self.view.input_main_menu()
            if menu_selection == 1:
                self.register_player_in_db()
            if menu_selection == 2:
                self.create_tournament()
            if menu_selection == 3:
                self.resume_tournament()
            if menu_selection == 4:
                self.display_tournament()
            if menu_selection == 5:
                self.display_player()
            if menu_selection == 6:
                print("See You ASAP...")
                running = False

    def create_static_tournament(self):
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

    def create_tournament(self):
        """
        create_tournament manage all the necessaries information to create a tournament and store it in database
        :return: the new instance of tournament that has been created
        """

        tournament_number_of_players = self.view.input_tournament_number_of_players()
        tournament_registered_players = self.register_players_in_tournament(tournament_number_of_players)
        tournament_number_of_turns = self.view.input_tournament_number_of_turns()
        tournament_name = self.view.input_tournament_name()
        tournament_place = self.view.input_tournament_place()
        tournament_start_date = self.view.input_tournament_start_date()
        tournament_end_date = self.view.input_tournament_end_date()
        tournament_description = self.view.input_tournament_description()
        tournament = Tournament(
            name=tournament_name,
            place=tournament_place,
            start_date=tournament_start_date,
            end_date=tournament_end_date,
            description=tournament_description,
            registered_players=tournament_registered_players,
            number_of_turns=tournament_number_of_turns,
            actual_turn=1,
            all_turns=[],
        )
        tournament.create_turn()
        json_players = Tournament.json_players(tournament_registered_players)
        json_turns = tournament.json_turns(tournament.all_turns)
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
        player = Player.get(player_id)
        return player

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
        tournament = self.get_tournament()
        tournament, status = self.check_tournament_status(tournament)
        if status is False:
            json_players = Tournament.json_players(tournament.registered_players)
            json_turns = Tournament.json_turns(tournament.all_turns)
            tournament.put(tournament.ID, json_players, json_turns)
            tournament.sort_players_by_score()
            player_best_score_index = len(tournament.registered_players) - 1
            self.view.display_tournament_winner(tournament.registered_players[player_best_score_index])
            return None
        current_turn = self.get_current_turn(tournament)
        current_game, index_of_game = self.get_current_game(current_turn)
        self.view.display_tournament_turn(current_turn)
        game_winner = self.view.input_game_winner(current_game, index_of_game + 1)
        print("game winner: " + game_winner)
        if game_winner == "1":
            current_game.player_one_info.score += 1
            Controller.update_player_info_in_turn(current_turn, current_game)
            print("the player one win the game")
        if game_winner == "2":
            current_game.player_two_info.score += 1
            Controller.update_player_info_in_turn(current_turn, current_game)
            print("the player two win the game")
        if game_winner == "3":
            current_game.player_one_info.score += 0.5
            current_game.player_two_info.score += 0.5
            Controller.update_player_info_in_turn(current_turn, current_game)
            print("it's a draw")
        current_turn.all_games[index_of_game] = current_game
        current_turn_index = Controller.find_turn_index_in_tournament(tournament, current_turn)
        tournament.all_turns[current_turn_index] = current_turn
        json_players = Tournament.json_players(tournament.registered_players)
        json_turns = Tournament.json_turns(tournament.all_turns)
        tournament.put(tournament.ID, json_players, json_turns)

    @staticmethod
    def find_tournament_winner(tournament):
        registered_players = tournament.registered_players
        player_max_score = max(registered_players, key=lambda objet:objet.score)
        return player_max_score

    @staticmethod
    def update_player_info_in_turn(turn: Turn, game: Game):
        turn.update_players_by_game(game)

    def check_tournament_status(self, tournament: Tournament):
        current_turn = self.get_current_turn(tournament)
        if self.are_still_game_to_play(current_turn) is False:
            tournament.end_turn(current_turn)
            is_turn_updated = tournament.update_actual_turn()
            if is_turn_updated is False:
                return tournament, False
            tournament.create_turn()
            json_turns = Tournament.json_turns(tournament.all_turns)
            json_players = Tournament.json_players(tournament.registered_players)
            tournament.put(tournament.ID, json_players, json_turns)
        return tournament, True

    def get_current_turn(self, tournament: Tournament) -> Optional[Turn]:
        searched_name = "round " + str(tournament.actual_turn)
        founded_turn = None
        for turn in tournament.all_turns:
            if turn.name == searched_name:
                founded_turn = turn
        return founded_turn

    def get_current_game(self, turn: Turn):
        for game in turn.all_games:
            if game.player_one_info.score == 0 and game.player_two_info.score == 0:
                return game, turn.all_games.index(game)
        print("all games for this turn has been played")
        return None

    def are_still_game_to_play(self, turn: Turn):
        current_game = self.get_current_game(turn)
        print(current_game)
        if current_game is None:
            return False
        return True

    @staticmethod
    def find_turn_index_in_tournament(tournament, current_turn):
        for turn in tournament.all_turns:
            if turn.name == current_turn.name:
                index_of_turn = tournament.all_turns.index(turn)
                return index_of_turn
        print("we didn't find a turn with this name")
        return None

    @staticmethod
    def find_player_index_in_tournament(tournament, current_player):
        for player in tournament.registered_players:
            if current_player.national_chess_ID == player.national_chess_ID:
                index_of_player = tournament.registered_players.index(player)
                return index_of_player
        print("this player is not registered to the tournament")
        return None

    def display_tournament(self):
        tournament = self.get_tournament()
        print(f"tournament informations: \n {tournament}")

    def get_tournament(self):
        tournament_id = self.view.input_get_tournament_id()
        tournament = Tournament.get(tournament_id)
        if tournament is None:
            return None
        tournament.ID = tournament_id
        return tournament

    def display_player(self):
        player = self.get_player()
        if player is None:
            print("we didnt find a player with this national chess id in our database")
            return None
        print(f"player information:\n{player}")
