from models.player import Player
from models.tournament import Tournament
class PlayersReport:
    def __init__(self, players: list[Player]):
        self.players = players

    def __str__(self):
        return f"players: {self.players} \n"

class TournamentsReport:
    def __init__(self, tournaments: list[Tournament]):
        self.tournaments = tournaments

    def __str__(self):
        return f"tournaments: {self.tournaments} \n"

class TournamentReport:
    def __init__(self, tournament: Tournament):
        self.tournament_start_date = tournament.start_date
        self.tournament_end_date = tournament.end_date
        self.tournament_name = tournament.name

    def __str__(self):
        return f"Tournament name: {self.tournament_name} \n" \
               f"Start date of the tournament: {self.tournament_start_date} \n" \
               f"End date of the tournament: {self.tournament_end_date} \n"

class TournamentPlayersReport:
    def __init__(self, tournament: Tournament):
        self.tournament_players = tournament.registered_players

    def __str__(self):
        return f"players in the tournament: {self.tournament_players} \n"

class TournamentTurnsGamesReport:
    def __init__(self, tournament: Tournament):
        self.tournament_turns = tournament.all_turns

    def __str__(self):
        turn_games_informations = []
        for turn in self.tournament_turns:
            string_turn = f"turn: {turn} \n" \
                          f"games in this turn: {turn.all_games}"
            turn_games_informations.append(string_turn)
        return f"all turns and games in those turns: {turn_games_informations}"
