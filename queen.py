from piece import Piece
from piece import board_size

###################################################

class Queen(Piece):

    def possible_moves(self):
        # Moves will be None after it has been eaten by another piece
        if self.moves == None:
            return

        self.moves = []

        # For simplicity in writing the code below. Since they are
        # funtion specific variables they cannot be placed in piece.py
        # and making thm class variables defeats the purpose of simplifying
        # the code due to the self. required.
        x,y = self.loc[0], self.loc[1]

# Queen movement parameters:
    # No need to use op or inv because a Queen's movement is universal
    # and does not rely on perspective.

        # Right
        for e in range(1,board_size+1):
            if self.universal_parameters(x+e, y):
                break

        # Left
        for e in range(1,board_size+1):
            if self.universal_parameters(x-e, y):
                break

        # Up
        for e in range(1,board_size+1):
            if self.universal_parameters(x, y+e):
                break

        # Down
        for e in range(1,board_size+1):
            if self.universal_parameters(x, y-e):
                break

        # Top Right diagonal
        for e in range(1,board_size+1):
            if self.universal_parameters(x+e, y+e):
                break

        # Bottom Right diagonal
        for e in range(1,board_size+1):
            if self.universal_parameters(x+e, y-e):
                break

        # Top Left diagonal
        for e in range(1,board_size+1):
            if self.universal_parameters(x-e, y+e):
                break

        # Bottom Left diagonal
        for e in range(1,board_size+1):
            if self.universal_parameters(x-e, y-e):
                break

    def universal_parameters(self, x, y):
        if self.check_loc(x, y, False):
            result, piece = self.check_for_piece(x, y)
            if result:
                if self.team != piece.team:
                    self.moves.append([x, y])
                    return True
                else:
                    return True
            self.moves.append([x, y])
        else:
            return True

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print "Running queen.py"

# queen = Queen([5,8],"white")
# block = Queen([5,5],"black")
