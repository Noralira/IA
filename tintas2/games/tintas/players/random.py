from random import randint

from games.tintas.action import TintasAction
from games.tintas.player import TintasPlayer
from games.tintas.state import TintasState
from games.state import State


class RandomTintasPlayer(TintasPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TintasState):
        return TintasAction(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
