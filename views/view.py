from models.player import Player
from models.tournament import Tournament
import datetime

ERR_NOT_NUMERIC_VALUE = "please fill this field in digits"


class View:
    def __init__(self):
        return

    @staticmethod
    def input_main_menu():
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
        digit_menu_selection = ""
        print("\n --- Report Management --- \n")
        print("(1) List of all the players in the database (sorted alphabetically by last name)")
        print("(2) List of all the tournaments in the database")
        print("(3) Name and date of a given tournament (need tournament id)")
        print("(4) "
              "List of registered players in a tournament (sorted alphabetically by last name, need tournament id)")
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
        tournament_name = input("enter the name of the tournament: \n")
        return tournament_name

    @staticmethod
    def input_tournament_place():
        tournament_place = input("enter the place of the tournament: \n")
        return tournament_place

    @staticmethod
    def input_tournament_start_day():
        start_day = None
        while start_day is None:
            try:
                start_day = int(input("please enter the day the tournament will start (in digits): \n"))
                return start_day
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_month():
        start_month = None
        while start_month is None:
            try:
                start_month = int(input("please enter the month the tournament will start (in digits): \n"))
                return start_month
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_year():
        start_year = None
        while start_year is None:
            try:
                start_year = int(input("please enter the year the tournament will start (in digits): \n"))
                return start_year
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_day():
        end_day = None
        while end_day is None:
            try:
                end_day = int(input("please enter the day the tournament will end (in digits): \n"))
                return end_day
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_month():
        end_month = None
        while end_month is None:
            try:
                end_month = int(input("please enter the month the tournament will end (in digits): \n"))
                return end_month
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_year():
        end_year = None
        while end_year is None:
            try:
                end_year = int(input("please enter the year the tournament will end (in digits): \n"))
                return end_year
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_date():
        start_day = View.input_tournament_start_day()
        start_month = View.input_tournament_start_month()
        start_year = View.input_tournament_start_year()
        start_date = datetime.date(start_year, start_month, start_day)
        return start_date

    @staticmethod
    def input_tournament_end_date():
        end_day = View.input_tournament_end_day()
        end_month = View.input_tournament_end_month()
        end_year = View.input_tournament_end_year()
        end_date = datetime.date(end_year, end_month, end_day)
        return end_date

    @staticmethod
    def input_tournament_description():
        tournament_description = input("please enter the description of the tournament: \n")
        return tournament_description

    @staticmethod
    def input_tournament_register_player():
        return input(
            "please enter the national chess ID of the player you want to register for the tournament: \n"
        )

    @staticmethod
    def input_tournament_number_of_turns():
        number_of_turns = None
        while number_of_turns is None:
            try:
                number_of_turns = int(input("how much turns this tournament will count ? (in digits) \n"))
                return number_of_turns
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_number_of_players():
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
        return input("please enter the national chess ID of the player you want to register: \n")

    @staticmethod
    def input_player_first_name():
        return input("please enter the first name of the player you want to register: \n")

    @staticmethod
    def input_player_last_name():
        return input("please enter the last name of the player you want to register: \n")

    @staticmethod
    def input_player_birth_date():
        birth_day, birth_month, birth_year = 0, 0, 0
        try:
            birth_day = int(input("please enter the birth's day of the player (in digits): \n"))
            birth_month = int(input("please enter the birth's month of the player (in digits): \n"))
            birth_year = int(input("please enter the birth's year of the player (in digits): \n"))
        except ValueError:
            print("you must enter the date in digits please")
        birth_date = datetime.date(birth_year, birth_month, birth_day)
        return birth_date

    @staticmethod
    def input_get_tournament_id():
        return input("please fill the id of the tournament you want to resume: \n")

    @staticmethod
    def display_tournament_turn(turn):
        print(f"current turn: {turn.name}")

    @staticmethod
    def display_game_winner(game_winner):
        if game_winner == 1:
            print("the player one wins the game ! 😄")
        if game_winner == 2:
            print("the player two wins the game")
        if game_winner == 3:
            print("it's a draw")

    @staticmethod
    def input_game_winner(game, game_number):
        print(f"current game: game {game_number}")
        game_result = None
        while game_result is None:
            try:
                game_result = int(input(
                    f"Please choose the digit corresponding to the result of the game \n"
                    f"1) Player One - "
                    f"{game.player_one_info.player.first_name} "
                    f"{game.player_one_info.player.last_name} - win \n"
                    f"2) Player Two - "
                    f"{game.player_two_info.player.first_name} "
                    f"{game.player_two_info.player.last_name} - win \n"
                    f"3) Draw \n"))
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)
        return game_result

    @staticmethod
    def display_tournament_winner(player: Player):
        print(f"Congratulations ! This tournament is ended and the winner is: \n "
              f"  {player.first_name} {player.last_name} with a score of {player.score} points ! "
              )

    @staticmethod
    def report_display_players(players: list):
        for player in players:
            print(f"player: {player}")

    @staticmethod
    def report_display_tournaments(tournaments: list):
        for tournament in tournaments:
            print(f"tournament: {tournament}")

    @staticmethod
    def report_display_tournament_information(tournament: Tournament):
        print(f"tournament name: {tournament.name} \n "
              f"start date: {tournament.start_date} \n "
              f"end date: {tournament.end_date}")

    @staticmethod
    def report_display_tournament_players(tournament: Tournament):
        for player in tournament.registered_players:
            print(f"registered player: {player}")

    @staticmethod
    def report_display_tournament_turns(tournament: Tournament):
        for turn in tournament.all_turns:
            print(f"turn: {turn}")
