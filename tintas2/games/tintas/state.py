import random
from typing import Optional

from games.tintas.action import TintasAction
from games.tintas.result import TintasResult
from games.state import State
from games.tintas.action import TintasMoveAction, TintasPassAction, TintasPlaceAction


class TintasState(State):

    #list each color for each player--------------------------------------------------------------------------
    pieces_0 = [0,0,0,0,0,0,0]
    pieces_1 = [0,0,0,0,0,0,0]

    #pieces-------------------------------------------------------------

    preto = "p"
    branco = "b"
    laranja = "l"
    rosa = "r"
    azul = "a"
    vermelho = "v"
    verde = "d"

    #cells----------------------------------------------------------------------------

    EMPTY_CELL = -1
    NP_CELL = -2

    #players------------------------------------------------------------------------------------

    PLAYER_0 = 0
    PLAYER_1 = 1
    def __init__(self):
        super().__init__()


        #grid----------------------------------------------------------------

        EC= TintasState.EMPTY_CELL
        _= TintasState.NP_CELL
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

        all_pieces = [TintasState.preto] * 7 
        all_pieces += [TintasState.branco] * 7
        all_pieces += [TintasState.laranja] * 7
        all_pieces +=[TintasState.verde] * 7
        all_pieces +=[TintasState.vermelho] * 7
        all_pieces +=[TintasState.azul] * 7
        all_pieces +=[TintasState.rosa] * 7

    #shuffle pieces ---------------------------------------------------------------------------------

        random.shuffle(all_pieces)

        peca_atual = 0
        for i in range(0, len(self.__grid)):
            lin = self.__grid[i]
            for j in range(0, len(lin)):
                if self.__grid[i][j] == EC:
                    self.__grid[i][j] = all_pieces[peca_atual]
                    peca_atual = peca_atual + 1

        self.__p0_has_pawn = False
        self.__p1_has_pawn = False

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

    #Verify if there is a winner

    def __check_winner(self, pieces_0, pieces_1):
        if self.__acting_player == 0 and pieces_0[0]==7 or pieces_0[1]==7 or pieces_0[2]==7 \
            or pieces_0[3]==7 or pieces_0[4]==7 or pieces_0[5]==7 or pieces_0[6]==7:
            return True
        if self.__acting_player == 0 and pieces_0[0]==4 and pieces_0[1]==4 and pieces_0[2]==4 and pieces_0[3]==4:
            return True
        else:
            if self.__acting_player == 1 and pieces_1[0]==7 or pieces_1[1]==7 or pieces_1[2]==7 \
            or pieces_1[3]==7 or pieces_1[4]==7 or pieces_1[5]==7 or pieces_1[6]==7:
                return True
            if self.__acting_player == 0 and pieces_0[0]==4 and pieces_0[1]==4 and pieces_0[2]==4 and pieces_0[3]==4:
                return True

    #"""
    """
          # check for 1 across------------------------------------------------------------
        for row in range(0, self.__grid):
            for col in range(0, self.__grid[0] - 3):
                if self.__grid[row][col] == player:
                    return True

        # check for 1 up and down-------------------------------------------------------------
        for row in range(0, self.__grid - 3):
            for col in range(0, self.__grid[0]):
                if self.__grid[row][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__grid):
            for col in range(0, self.__grid[0] - 3):
                if self.__grid[row][col] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__grid - 3):
            for col in range(0, self.__grid[0] - 3):
                if self.__grid[row][col] == player:
                    return True

        return False
    """
    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    #validate action--------------------------------------------------------------------------

    def validate_action(self, action: TintasAction) -> bool:
        if self.__acting_player == 0 and not self.__p0_has_pawn and type(action) != TintasPlaceAction:
            return False
        if self.__acting_player == 1 and not self.__p1_has_pawn and type(action) != TintasPlaceAction:
            return False
        return True

    #change player---------------------------------------------------------------------------

    def switch_player(self):
        self.__acting_player = 1 if self.__acting_player == 0 else 0


    #Validate pawn placement---------------------------------------------------------------------------------------------------
    """
    def validate_pawn_placement(self):
        is_valid_placement = False
        row = -1
        col = -1
     while is_valid_placement is False:
         if grid[row][col] == "EC" 
            is_valid_placement = True

    return row, col
    """
    #update vector of player
    
    def update_number_pieces(self, col, row, pieces_1, pieces_0):
        val = self.__grid[row][col]
        if val == "p" and self.__acting_player == 1:
            pieces_1[0] = pieces_1[0] +1
        else:
             if val == "b":
                pieces_1[1] = pieces_1[1] +1
             else: 
                if val == "l":
                    pieces_1[2] = pieces_1[2] +1
                else:
                    if val == "r":
                     pieces_1[3] = pieces_1[3] +1
                    else:
                        if val == "a":
                            pieces_1[4] = pieces_1[4] +1
                        else:
                            if val == "v":
                                pieces_1[5] = pieces_1[5] +1
                            else:
                                if val == "d":
                                    pieces_1[6] = pieces_1[6] +1
        if val == "p" and self.__acting_player == 0:
            pieces_0[0] = pieces_0[0] +1
        else:
             if val == "b":
                pieces_0[1] = pieces_0[1] +1
             else: 
                if val == "l":
                    pieces_0[2] = pieces_0[2] +1
                else:
                    if val == "r":
                     pieces_0[3] = pieces_0[3] +1
                    else:
                        if val == "a":
                            pieces_0[4] = pieces_0[4] +1
                        else:
                            if val == "v":
                                pieces_0[5] = pieces_0[5] +1
                            else:
                                if val == "d":
                                    pieces_0[6] = pieces_0[6] +1
        
    
    #update action----------------------------------------------------------------------------------------------

    def update(self, action: TintasAction):
        if type(action) == TintasPlaceAction:
            self.__grid[action.get_line()][action.get_col()] = self.__acting_player
            self.update_number_pieces()
            self.switch_player()
        elif type(action) == TintasMoveAction:
    
            #remove color piece and update vector of player
            """
            
            """
            
            pass
        elif type(action) == TintasPassAction:
            self.switch_player()
        else:
            pass
        
        # determine if there is a winner---------------------------------------------------------------------------------
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player----------------------------------------------------------------------
        
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1


    #display da grid------------------------------------------------------------------------------------------
    def __display_cell(self, row, col):
        val = self.__grid[row][col]
        if val == -2:
            print("   ",end="")
        else:
            print(f" {self.__grid[row][col]} ",end="")

    def __display_numbers(self):
        for col in range(0, len(self.__grid[0])):
            if col < 10:
                print(' ', end="") 

            print(col, end="")
            print("  ", end="")
        print("")
    

    def __display_separator(self):
        for col in range(0, len(self.__grid[0])):
            print("----", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, len(self.__grid)):
            for col in range(0, len(self.__grid[0])):
                self.__display_cell(row, col)
                
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")



    def is_finished(self) -> bool:
        return False

    def get_acting_player(self) -> int:
        return self.__acting_player

    

    def clone(self):
        cloned_state = TintasState()
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, len(self.__grid)):
            for col in range(0, len(self.__grid[0])):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[TintasResult]:
        if self.__has_winner:
            return TintasResult.LOOSE if pos == self.__acting_player else TintasResult.WIN
        if self.__is_full():
            return TintasResult.DRAW
        return None



    def get_num_rows(self):
        return self.__grid

    def get_num_cols(self):
        return self.__grid

    def before_results(self):
        pass
