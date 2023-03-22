class Tournament:
    def __init__(self, name, place, startDate, endDate, actualTurn, turns, registeredPlayers, description, numberOfTurns=4):
        self.ID = ""  # TODO: create method to generate tournamentID
        self.name = name
        self.place = place
        self.startDate = startDate
        self.endDate = endDate
        self.actualTurn = actualTurn
        self.turns = turns
        self.registeredPlayers = registeredPlayers
        self.description = description
        self.numberOfTurns = numberOfTurns

    def generateTurn(self):
        pass

    def sortPlayersByPoints(self):
        pass

    def associatePlayers(self):
        pass

    def choosePlayersWithSamePoints(self):
        pass

    def post(self):
        pass

    def get(self, tournamentID):
        pass

    def put(self, tournamentID):
        pass
