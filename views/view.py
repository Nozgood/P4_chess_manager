from models.player import Player
from models.tournament import Tournament
from models.turn import Turn
from models.game import Game
import datetime

ERR_NOT_NUMERIC_VALUE = "please fill this field in digits"


class View:
    def __init__(self):
        return

    @staticmethod
    def input_main_menu():
        """
        Takes the input from the user to choose which action to make in the main menu of the application

        :return: the digit corresponding to the action the user wants to make
        """
        digit_menu_selection = ""
        print("\n --- Chess Manager --- \n")
        print("(1) Register a player in the database")
        print("(2) Create a new tournament")
        print("(3) Resume a tournament \n")
        print("(4) Display a Tournament information (need it id)")
        print("(5) Display a Player information (need him national chess id)")
        print("(6) Generate a report \n")
        print("(7) Exit the application \n")
        try:
            digit_menu_selection = int(
                input("please insert the digit corresponding to the action you want to make: \n"))
        except ValueError:
            print("please enter a digit value")
        return digit_menu_selection

    @staticmethod
    def input_report_menu():
        """
        Takes the input from the user to choose which action to make in the report menu of the application

        :return: the digit corresponding to the action the user wants to make
        """
        digit_menu_selection = ""
        print("\n --- Report Management --- \n")
        print("(1) List of all the players in the database (sorted alphabetically by last name)")
        print("(2) List of all the tournaments in the database")
        print("(3) Name and date of a given tournament (need tournament id)")
        print(
            "(4) "
            "List of registered players in a tournament (sorted alphabetically by last name, need tournament id)"
        )
        print("(5) List of all turns of a tournament and all games of each turn (need tournament id)")
        print("(6) Go back to main menu")
        try:
            digit_menu_selection = int(
                input("please insert the digit corresponding to the action you want to make: \n"))
        except ValueError:
            print("please enter a digit value")
        return digit_menu_selection

    @staticmethod
    def input_tournament_name():
        """
        Saves the input from the user for the name of a created tournament

        :return: the input
        """
        tournament_name = input("enter the name of the tournament: \n")
        return tournament_name

    @staticmethod
    def input_tournament_place():
        """
        Saves the input from the user for the place of a created tournament

        :return: the input
        """
        tournament_place = input("enter the place of the tournament: \n")
        return tournament_place

    @staticmethod
    def input_tournament_start_day():
        """
        Saves the input from the user for the start day of a created tournament

        :return: the input
        """
        start_day = None
        while start_day is None:
            try:
                start_day = int(input("please enter the day the tournament will start (in digits): \n"))
                return start_day
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_month():
        """
        Saves the input from the user for the start month of a created tournament

        :return: the input
        """
        start_month = None
        while start_month is None:
            try:
                start_month = int(input("please enter the month the tournament will start (in digits): \n"))
                return start_month
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_year():
        """
        Saves the input from the user for the start year of a created tournament

        :return: the input
        """
        start_year = None
        while start_year is None:
            try:
                start_year = int(input("please enter the year the tournament will start (in digits): \n"))
                return start_year
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_day():
        """
        Saves the input from the user for the end day of a created tournament

        :return: the input
        """
        end_day = None
        while end_day is None:
            try:
                end_day = int(input("please enter the day the tournament will end (in digits): \n"))
                return end_day
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_month():
        """
        Saves the input from the user for the end month of a created tournament

        :return: the input
        """
        end_month = None
        while end_month is None:
            try:
                end_month = int(input("please enter the month the tournament will end (in digits): \n"))
                return end_month
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_year():
        """
        Saves the input from the user for the end year of a created tournament

        :return: the input
        """
        end_year = None
        while end_year is None:
            try:
                end_year = int(input("please enter the year the tournament will end (in digits): \n"))
                return end_year
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_date():
        """
        Saves the 3 inputs for a starting date (day, month year) create a datetime object and returns it

        :return: the datetime object that has been created
        """
        start_day = View.input_tournament_start_day()
        start_month = View.input_tournament_start_month()
        start_year = View.input_tournament_start_year()
        start_date = datetime.date(start_year, start_month, start_day)
        return start_date

    @staticmethod
    def input_tournament_end_date():
        """
        Saves the 3 inputs for a starting date (day, month year) create a datetime object and returns it

        :return: the datetime object that has been created
        """
        end_day = View.input_tournament_end_day()
        end_month = View.input_tournament_end_month()
        end_year = View.input_tournament_end_year()
        end_date = datetime.date(end_year, end_month, end_day)
        return end_date

    @staticmethod
    def input_tournament_description():
        """
        Saves the input from the user for the description of a created tournament

        :return: the input
        """
        tournament_description = input("please enter the description of the tournament: \n")
        return tournament_description

    @staticmethod
    def input_tournament_register_player(players_in_db: list):
        """
        Saves the input of the user to get a player in the database and register him/her to a tournament

        :return: the input
        """
        for player in players_in_db:
            print(f"({players_in_db.index(player)})player: {player}")
        print(f"({len(players_in_db)}) Add a new player in the database and register him / her")
        int_player_choice = None
        while int_player_choice is None:
            try:
                int_player_choice = int(input(
                    "please enter the digit corresponding to the player you want to register to the tournament: \n"
                ))
                if int_player_choice < 0 or int_player_choice > len(players_in_db):
                    print("the digit you enter is not valid, try again")
                    int_player_choice = None
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)
        if int_player_choice == len(players_in_db):
            return int_player_choice
        return players_in_db[int_player_choice]

    @staticmethod
    def input_tournament_number_of_turns():
        """
        Saves the input from the user for the number of turns of a created tournament

        :return: the input
        """
        number_of_turns = None
        while number_of_turns is None:
            try:
                number_of_turns = int(input("how much turns this tournament will count ? (in digits) \n"))
                return number_of_turns
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_number_of_players():
        """
        Saves the input from the user for the number of players of a created tournament

        :return: the input
        """
        number_of_players = None
        while number_of_players is None:
            try:
                number_of_players = int(
                    input("please enter how much players will participate to the tournament(in digits) \n"))
                return number_of_players
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_player_chess_id():
        """
        Saves the input from the user for the chess ID of a created player

        :return: the input
        """
        return input("please enter the national chess ID of the player you want to register: \n")

    @staticmethod
    def input_player_first_name():
        """
        Saves the input from the user for the first name of a created player

        :return: the input
        """
        return input("please enter the first name of the player you want to register: \n")

    @staticmethod
    def input_player_last_name():
        """
        Saves the input from the user for the last name of a created player

        :return: the input
        """
        return input("please enter the last name of the player you want to register: \n")

    @staticmethod
    def input_player_birth_day():
        """
        Saves the input from the user for the birth's day of a created player

        :return: the input
        """
        birth_day = None
        while birth_day is None:
            try:
                birth_day = int(input("please enter the birth's day of the player (in digits): \n"))
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)
        return birth_day

    @staticmethod
    def input_player_birth_month():
        """
        Saves the input from the user for the birth's month of a created player

        :return: the input
        """
        birth_month = None
        while birth_month is None:
            try:
                birth_month = int(input("please enter the birth's month of the player (in digits): \n"))
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)
        return birth_month

    @staticmethod
    def input_player_birth_year():
        """
        Saves the input from the user for the birth's year of a created player

        :return: the input
        """
        birth_year = None
        while birth_year is None:
            try:
                birth_year = int(input("please enter the birth's year of the player (in digits): \n"))
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)
        return birth_year

    @staticmethod
    def input_player_birth_date():
        """
        Saves the 3 input for a birthdate, create a datetime object and returns it

        :return: the datetime object that has been created
        """
        birth_day = View.input_player_birth_day()
        birth_month = View.input_player_birth_month()
        birth_year = View.input_player_birth_year()
        birth_date = datetime.date(birth_year, birth_month, birth_day)
        return birth_date

    @staticmethod
    def input_get_tournament_id():
        """
        Saves the input of the user to get a tournament (except to receive an id)

        :return: the input
        """
        return input("please fill the id of the tournament you want to resume: \n")

    @staticmethod
    def display_tournament_turn(turn: Turn):
        """
        Accepts a turn and display it name

        :param turn: the turn that we want to print it name
        """
        print(f"current turn: {turn.name}")

    @staticmethod
    def display_game_winner(game_winner: int):
        """
        Accepts an int corresponding to the winner of a game and display a message in the console

        :param game_winner: the digit corresponding to the player that has won the game
        """
        if game_winner == 1:
            print("the player one wins the game ! 😄")
        if game_winner == 2:
            print("the player two wins the game")
        if game_winner == 3:
            print("it's a draw")

    @staticmethod
    def input_game_winner(game: Game, game_number: int):
        """
        Accepts an object of type Game and the number of the game in the turn, display the number of the current
        game saves the input corresponding to thewinner of the game and returns it

        :param game: object of type Game which contains the information of the players
        :param game_number: int corresponding to the current game in the turn
        :return: an int corresponding to the result of the game
        """
        print(f"current game: game {game_number}")
        game_result = None
        while game_result is None:
            try:
                game_result = int(
                    input(
                        f"Please choose the digit corresponding to the result of the game \n"
                        f"1) Player One - "
                        f"{game.player_one_info.player.first_name} "
                        f"{game.player_one_info.player.last_name} - win \n"
                        f"2) Player Two - "
                        f"{game.player_two_info.player.first_name} "
                        f"{game.player_two_info.player.last_name} - win \n"
                        f"3) Draw \n"
                    )
                )
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)
        return game_result

    @staticmethod
    def display_tournament_winner(player: Player):
        """
        Accepts an object of type Player which corresponds to the winner of a tournament and display his / her
        information

        :param player: the winner of the tournament (of the type Player)
        """
        print(
            f"Congratulations ! This tournament is ended and the winner is: \n "
            f"  {player.first_name} {player.last_name} with a score of {player.score} points ! "
        )

    @staticmethod
    def report_display_players(players: list):
        """
        Accepts a list of players and display information for each player in the list

        :param players: a list containing players
        :return:
        """
        for player in players:
            print(f"player: {player}")

    @staticmethod
    def report_display_tournaments(tournaments: list):
        """
        Accepts a list of tournaments and display information for each tournament in the list

        :param tournaments: a list containing tournaments
        """
        for tournament in tournaments:
            print(f"tournament: {tournament}")

    @staticmethod
    def report_display_tournament_information(tournament: Tournament):
        """
        Accepts an object of type Tournament and display information

        :param tournament: the object type Tournament that we want to display
        """
        print(
            f"tournament name: {tournament.name} \n "
            f"start date: {tournament.start_date} \n "
            f"end date: {tournament.end_date}")

    @staticmethod
    def report_display_tournament_players(tournament: Tournament):
        """
        Accepts an object of type Tournament and display each player who is registered for this tournament

        :param tournament: the object type Tournament that we want to display
        """
        for player in tournament.registered_players:
            print(f"registered player: {player}")

    @staticmethod
    def report_display_tournament_turns(tournament: Tournament):
        """
        Accepts an object of type Tournament and display each turn for this tournament

        :param tournament: the object type Tournament that we want to display
        """
        for turn in tournament.all_turns:
            print(f"turn: {turn}")
