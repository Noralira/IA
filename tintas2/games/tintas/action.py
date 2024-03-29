class TintasAction():

    __col: int
    __row: int

    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col
    

# Move pawn action
class TintasMoveAction(TintasAction):
    
    __col: int
    __line: int

    def __init__(self, col: int, line: int):
        self.__col = col
    
    def get_line(self):
        return self.__line

    def get_col(self):
        return self.__col
    

# Place pawn action
class TintasPlaceAction(TintasAction):
    
    __col: int
    __line: int

    def __init__(self, col: int, line: int):
        self.__col = col
    
    def get_line(self):
        return self.__line

    def get_col(self):
        return self.__col

# Pass action
class TintasPassAction(TintasAction):
    pass