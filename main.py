from views.view import View
from controllers.controller import Controller


def run():
    view = View()
    controller = Controller(view)
    controller.run()


run()
