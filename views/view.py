from models.tournament import Tournament
import datetime

class View:
    def __init__(self):
        return

    @staticmethod
    def input_tournament_name():
        tournament_name = input("enter the name of the tournament: \n ")
        return tournament_name

    @staticmethod
    def input_tournament_place():
        tournament_place = input("enter the place of the tournament: \n")
        return tournament_place

    @staticmethod
    def input_tournament_start_date():
        start_day, start_month, start_year = 0, 0, 0
        try:
            start_day = int(input("please enter the day the tournament will start (in digits): \n"))
            start_month = int(input("please enter the month the tournament will start (in digits): \n"))
            start_year = int(input("please enter the year the tournament will start (in digits): \n"))
        except ValueError:
            print("you must enter the date in digits please")
        start_date = datetime.date(start_year, start_month, start_day)
        return start_date

    @staticmethod
    def input_tournament_end_date():
        end_day, end_month, end_year = 0, 0, 0
        try:
            end_day = int(input("please enter the day the tournament will end (in digits): \n"))
            end_month = int(input("please enter the month the tournament will end (in digits): \n"))
            end_year = int(input("please enter the year the tournament will end (in digits): \n"))
        except ValueError:
            print("you must enter the date in digits please")
        end_date = datetime.date(end_year, end_month, end_day)
        return end_date

    @staticmethod
    def input_tournament_description():
        tournament_description = input("please enter the description of the tournament: \n")
        return tournament_description

    @staticmethod
    def input_get_player_id():
        player_to_register_id = input("please enter the national chess ID of the player you want to register: \n")
        return player_to_register_id

