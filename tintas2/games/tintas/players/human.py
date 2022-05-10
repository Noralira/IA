from games.tintas.action import TintasAction
from games.tintas.player import TintasPlayer
from games.tintas.state import TintasState


class HumanTintasPlayer(TintasPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TintasState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return TintasAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: TintasState):
        # ignore
        pass

    def event_end_game(self, final_state: TintasState):
        # ignore
        pass
