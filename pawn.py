from queen import Queen
from piece import board_size, piece_locs

###################################################

class Pawn(Queen):
    # Pawn is a child of Queen because it needs its movement parameters if
    # it becomes a queen. The Piece functions can be accesed through Queen
    # because it inherits from Piece. Therefore, Pawn inherits from Piece
    # indirectly through Queen.

    def __init__(self, loc, team, first_move = True):
        self.first_move = first_move
        self.is_queen = False
        super(Pawn, self).__init__(loc, team)

###################################################

    def move(self, x, y):
        if [x,y] in self.moves:
            self.first_move = False
            super(Pawn, self).move(x, y)
        else:
            print "Can't move there or may not be able to move this piece."
            return

###################################################

    def possible_moves(self):
        # if pawn has becomed a queen
        if self.is_queen == True:
             super(Pawn, self).possible_moves()
             return

        # Moves will be None after it has been eaten by another piece
        if self.moves == None:
            return

        self.moves = []

        # For simplicity in writing the code below. Since they are
        # funtion specific variables they cannot be placed in piece.py
        x,y = self.loc[0], self.loc[1]

# Pawn movement parameters:
        # Forward by one or two spaces
        if not self.check_for_piece(x, self.op(y,1))[0]:
            self.moves.append([x, self.op(y,1)])
            if self.first_move:
                if not self.check_for_piece(x, self.op(y,2))[0]:
                    self.moves.append([x, self.op(y,2)])

        # Checking diagonals
        if self.check_for_piece(self.op(x,1), self.op(y,1))[0]:
            self.moves.append([ self.op(x,1), self.op(y,1) ])
        if self.check_for_piece(self.inv(x,1), self.op(y,1))[0]:
            self.moves.append([ self.inv(x,1), self.op(y,1) ])

###################################################

    def transform(self):
        if self.team == "white":
            if self.loc[1] == board_size:
                self.is_queen = True
                self.possible_moves()
                return
            else:
                print "This pawn can't transform into a queen while \
in this location"
                return
        elif self.loc[1] == 1:
            self.is_queen = True
            self.possible_moves()
            return
        print "This pawn can't transform into a queen while in this location"
        return


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print "Running pawn.py"

# wqueen = Queen([5,1], "white")
# wpawn = Pawn([5,2], "white")
# bqueen = Queen([5,8], "black")
# bpawn = Pawn([5,7], "black")
