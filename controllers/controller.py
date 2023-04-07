from models.tournament import Tournament
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
