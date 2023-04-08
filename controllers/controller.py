from models.tournament import Tournament
from models.player import Player
from views.view import View

class Controller:
    def __init__(self, view: View):
        self.view = view

    def run(self):
        """
        run manages the creation and the running of a tournament, this is the main function of the controller
        """
    # tournament = view.create_tournament() => c'est également ici que l'on va inscrire les joueurs (ajouter une méthode à la fin pour inscrire un joueur en retar)
    # envoyer le tournoi en DB
    # créer le premier tour du tournoi
    # envoyer le tour en DB
    # créer les matchs du premier tour
    #
        tournament_to_create = self.create_tournament()
        tournament_to_create.post()

    # TODO: MANAGE THE REGISTERING PLAYERS PART
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
        return tournament

    def get_player(self):
        player_id = self.view.input_get_player_id()
        player_to_get = Player.get(player_id)
        return player_to_get
