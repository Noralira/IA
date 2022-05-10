import random
from typing import Optional

from games.connect4.action import Connect4Action
from games.connect4.result import Connect4Result
from games.state import State


class Connect4State(State):
    preto = "1"
    branco = "2"
    laranja = "3"
    rosa = "4"
    azul = "5"
    vermelho = "6"
    verde = "7"

    EMPTY_CELL = -1
    NP_CELL = -2

    def __init__(self):
        super().__init__()


        """
        the dimensions of the board
        """
        """
        the grid
        """
        EC= Connect4State.EMPTY_CELL
        _= Connect4State.NP_CELL
        self.__grid = [
            [ _, _, _,EC, _, _, _, _, _],
            [ _, _,EC, _,EC, _,EC, _, _],
            [ _, _, _,EC, _,EC, _,EC, _],
            [ _, _,EC, _,EC, _,EC, _, _],
            [ _,EC, _,EC, _,EC, _,EC, _],
            [EC, _,EC, _,EC, _,EC, _, _],
            [ _,EC, _,EC, _,EC, _,EC, _],
            [EC, _,EC, _,EC, _,EC, _,EC],
            [ _,EC, _,EC, _,EC, _,EC, _],
            [ _, _,EC, _,EC, _,EC, _,EC],
            [ _,EC, _,EC, _,EC, _,EC, _],
            [ _, _,EC, _,EC, _,EC, _, _],
            [ _,EC, _,EC, _,EC, _, _, _],
            [ _, _,EC, _,EC, _,EC, _, _],
            [ _, _, _, _, _,EC, _, _, _]
        ]

        all_pieces = [Connect4State.preto] * 7 
        all_pieces += [Connect4State.branco] * 7
        all_pieces += [Connect4State.laranja] * 7
        all_pieces +=[Connect4State.verde] * 7
        all_pieces +=[Connect4State.vermelho] * 7
        all_pieces +=[Connect4State.azul] * 7
        all_pieces +=[Connect4State.rosa] * 7

    

        random.shuffle(all_pieces)
        print(all_pieces)
        peca_atual = 0
        for i in range(0, len(self.__grid)):
            lin = self.__grid[i]
            for j in range(0, len(lin)):
                if self.__grid[i][j] == EC:
                    self.__grid[i][j] = all_pieces[peca_atual]
                    peca_atual = peca_atual + 1

        

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: Connect4Action) -> bool:
        col = action.get_col()

        # valid column
        if col < 0 or col >= self.__num_cols:
            return False

        # full column
        if self.__grid[0][col] != Connect4State.EMPTY_CELL:
            return False

        return True

    def update(self, action: Connect4Action):
        col = action.get_col()

        # drop the checker
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__acting_player
                break

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
            0:                              ' ',
            1:                              ' ',
            Connect4State.EMPTY_CELL:       ' '
        }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="") #colocar cores aleatorias com limite
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = Connect4State(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[Connect4Result]:
        if self.__has_winner:
            return Connect4Result.LOOSE if pos == self.__acting_player else Connect4Result.WIN
        if self.__is_full():
            return Connect4Result.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass
