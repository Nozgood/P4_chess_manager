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
        """
        Accepts an object type Player and format this object to json format

        :param player: an object of type Player
        :return: json format of the player
        """
        json_player = player.__json__()
        return json_player

    @staticmethod
    def json_turn(turn: Turn):
        """
        Accepts an object type Turn and format this object to json format

        :param turn: an object of type turn
        :return: json format of the turn
        """
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
                self.report_management()
            if menu_selection == 7:
                print("See You ASAP...")
                running = False

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
        json_players, json_turns = tournament.json_turns_and_players(
            tournament.registered_players,
            tournament.all_turns
        )
        tournament.post(json_players, json_turns)
        return tournament

    def register_players_in_tournament(self, number_of_players: int):
        """
        Accepts an int representing the number of player who wants to be registered to the tournament, get each player
        in the database, push it to a list and returns the list of players

        :param number_of_players: int representing the number of players to get
        :return: a list with all the players that want to be registered in the tournament
        """
        slice_of_players = []
        count = 1
        while count <= number_of_players:
            player = self.get_player()
            slice_of_players.append(player)
            count += 1
        return slice_of_players

    def get_player(self):
        """
        Takes the id of the player we want to get in the database, returns him / her
        :return: an object of type Player if found, None otherwise
        """
        player = None
        while player is None:
            player_id = self.view.input_tournament_register_player()
            player = Player.get(player_id)
        return player

    def register_player_in_db(self):
        """
        Takes all the needed information from the view to create an object type Player, save it to db and returns
        the saved player
        :return: the player that has been registered
        """
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
        """
        Manage the expecting behavior for a tournament that has started :
            - get the current tournament
            - check the status (games still to play, tournament ended...)
            - Takes the winner of a game
            - update tournament information in the database

        :return: None
        """
        tournament = self.get_tournament()
        tournament, status = self.check_tournament_status(tournament)
        if status is False:
            json_players, json_turns = tournament.json_turns_and_players(
                tournament.registered_players,
                tournament.all_turns
            )
            tournament.put(tournament.ID, json_players, json_turns)
            tournament.sort_players_by_score()
            player_best_score_index = len(tournament.registered_players) - 1
            self.view.display_tournament_winner(tournament.registered_players[player_best_score_index])
            return None
        current_turn = self.get_current_turn(tournament)
        current_game, index_of_game = Controller.get_current_game(current_turn)
        self.view.display_tournament_turn(current_turn)
        game_winner = self.view.input_game_winner(current_game, index_of_game + 1)
        if game_winner == 1:
            current_game.player_one_info.score += 1
            Controller.update_player_info_in_turn(current_turn, current_game)
        if game_winner == 2:
            current_game.player_two_info.score += 1
            Controller.update_player_info_in_turn(current_turn, current_game)
        if game_winner == 3:
            current_game.player_one_info.score += 0.5
            current_game.player_two_info.score += 0.5
            Controller.update_player_info_in_turn(current_turn, current_game)
        self.view.display_game_winner(game_winner)
        current_turn.all_games[index_of_game] = current_game
        current_turn_index = Controller.find_turn_index_in_tournament(tournament, current_turn)
        tournament.all_turns[current_turn_index] = current_turn
        json_players, json_turns = tournament.json_turns_and_players(
            tournament.registered_players,
            tournament.all_turns
        )
        tournament.put(tournament.ID, json_players, json_turns)
        return None

    @staticmethod
    def find_tournament_winner(tournament: Tournament):
        """
        accepts an object type Tournament and find the registered player that has the biggest score

        :param tournament: the tournament in which we want to find the winner
        :return: the player with the biggest score
        """
        registered_players = tournament.registered_players
        player_max_score = max(registered_players, key=lambda objet: objet.score)
        return player_max_score

    @staticmethod
    def update_player_info_in_turn(turn: Turn, game: Game):
        """
        Accepts an object type turn and an object type Game and update the players information in the turn based
        on the information of the game

        :param turn: the current turn in which we want to update information
        :param game: the game that contains information about the winner
        """
        turn.update_players_by_game(game)

    def check_tournament_status(self, tournament: Tournament):
        """
        accepts an object type Tournament and check the status of it:
            - get the current turn of a tournament
            - is there still game to play in this turn ?
            - is it the last turn of the tournament ?

        :param tournament: the tournament we want to check the status
        :return: the tournament with updated information
        """
        current_turn = self.get_current_turn(tournament)
        if self.are_still_game_to_play(current_turn) is False:
            print("hello turn not ended")
            tournament.end_turn(current_turn)
            is_turn_updated = tournament.update_actual_turn()
            if is_turn_updated is False:
                return tournament, False
            tournament.create_turn()
            json_turns = Tournament.json_turns(tournament.all_turns)
            json_players = Tournament.json_players(tournament.registered_players)
            tournament.put(tournament.ID, json_players, json_turns)
        return tournament, True

    @staticmethod
    def get_current_turn(tournament: Tournament) -> Optional[Turn]:
        """
        accepts an object type tournament and try to find the current turn of this tournament
        :param tournament: the tournament in which we want to find current turn
        :return: the current turn if there is, None if not
        """
        searched_name = "round " + str(tournament.actual_turn)
        founded_turn = None
        for turn in tournament.all_turns:
            if turn.name == searched_name:
                founded_turn = turn
        return founded_turn

    @staticmethod
    def get_current_game(turn: Turn):
        """
        accepts an object type Turn and try to find the current game of this turn

        :param turn: the turn in which we want to find the current game
        :return: the current Game if there is plus it indexes, None if not
        """
        for game in turn.all_games:
            if game.player_one_info.score == 0 and game.player_two_info.score == 0:
                return game, turn.all_games.index(game)
        print("all games for this turn has been played")
        return None, None

    @staticmethod
    def are_still_game_to_play(turn: Turn):
        """
        accepts an object type turn and will cheks if there are still games to play in this turn

        :param turn: the current turn we want to check
        :return: boolean : true if there is still game(s) to play, false if not
        """
        current_game = Controller.get_current_game(turn)
        print(f"current game: {current_game}")
        if current_game is None:
            print("hellllllo")
            return False
        return True

    @staticmethod
    def find_turn_index_in_tournament(tournament: Tournament, current_turn: Turn):
        """
        accepts an object type tournament and an object type turn and will try to find the index of the received turn
        in the tournament

        :param tournament: object type tournament
        :param current_turn: object type turn
        :return: the index of the turn if there is, None otherwise
        """
        for turn in tournament.all_turns:
            if turn.name == current_turn.name:
                index_of_turn = tournament.all_turns.index(turn)
                return index_of_turn
        print("we didn't find a turn with this name")
        return None

    @staticmethod
    def find_player_index_in_tournament(tournament: Tournament, current_player: Player):
        """
        accepts an object type tournament and an object type Player and will try to find the index of the received
        player in the tournament registered players

        :param tournament: object type Tournament
        :param current_player: object type Player
        :return: the index of the player in the tournament if there is, None otherwise
        """
        for player in tournament.registered_players:
            if current_player.national_chess_ID == player.national_chess_ID:
                index_of_player = tournament.registered_players.index(player)
                return index_of_player
        print("this player is not registered to the tournament")
        return None

    def display_tournament(self):
        """ Finds the tournament in the database and displays the information """
        tournament = self.get_tournament()
        print(f"tournament informations: \n {tournament}")

    def get_tournament(self):
        """
        Takes the id of the tournament we want to get, try to find it in the database and returns the result
        :return: the tournament information if it exists, None otherwise
        """
        tournament_id = self.view.input_get_tournament_id()
        tournament = Tournament.get(tournament_id)
        if tournament is None:
            return None
        tournament.ID = tournament_id
        return tournament

    def display_player(self):
        """ Find the player we want to display in the database and display him/her information on the console """
        player = self.get_player()
        if player is None:
            print("we didnt find a player with this national chess id in our database")
            return None
        print(f"player information:\n{player}")

    def report_management(self):
        """ manages the logical running of the report menu of the program """
        report_running = True
        while report_running is True:
            selection = self.view.input_report_menu()
            if selection == 1:
                players = Player.list()
                sorted_players = sorted(players, key=lambda x: x["last_name"])
                self.view.report_display_players(sorted_players)
            if selection == 2:
                tournaments = Tournament.list()
                self.view.report_display_tournaments(tournaments)
            if selection == 3:
                tournament = self.get_tournament()
                if tournament is None:
                    return None
                self.view.report_display_tournament_information(tournament)
            if selection == 4:
                tournament = self.get_tournament()
                if tournament is None:
                    return None
                tournament.registered_players.sort(key=lambda x: x.last_name)
                self.view.report_display_players(tournament.registered_players)
            if selection == 5:
                tournament = self.get_tournament()
                if tournament is None:
                    return None
                self.view.report_display_tournament_turns(tournament)
            if selection == 6:
                report_running = False
