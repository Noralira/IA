from games.tintas.player import TintasPlayer
from games.tintas.state import TintasState
from games.game_simulator import GameSimulator


class TintasSimulator(GameSimulator):

    def __init__(self, player1: TintasPlayer, player2: TintasPlayer):
        super(TintasSimulator, self).__init__([player1, player2])


    def init_game(self):
        return TintasState()

    def before_end_game(self, state: TintasState):
        # ignored for this simulator
        pass

    def end_game(self, state: TintasState):
        # ignored for this simulator
        pass
