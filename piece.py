import operator
ops = {"+": operator.add, "-": operator.sub}

board_size = 8
    # Variable determining the size the board.
    # Expected to be a positive intiger
    # deafult = 8. Change for custom modes.

piece_locs = {}

###################################################

class Piece(object):

    def __init__(self, loc, team):
        Teams = ['black','white']

        if team in Teams:
            self.team = team
        else:
            print 'Invalid Team.'
            return

        error = 'Invalid coordinates. Expected "loc" to be a list with only \
two positive intigers.'

        if len(loc)==2:
            try:
                x = int(loc[0])
                y = int(loc[1])
                if self.check_loc(x,y):
                    if not self.check_for_piece(x,y)[0]:
                        self.update_loc(x,y)
                    else:
                        print "Invalid coordinates. There's is already a \
piece in that location."
                        return
            except:
                print error
                return
        else:
            print error
            return

        self.moves = []

        # Ajusting for pespective.
        if self.team == "white":
            operator = "+"
            inverse = "-"
        else:
            operator = "-"
            inverse = "+"

        self.op = ops[operator]
        self.inv = ops[inverse]

        # Generating possible moves
        for piece in piece_locs:
            piece.possible_moves()

#>>>>>>>>>>>>> Old Code (for reference)(outdated) <<<<<<<<<<<<<<<<<<<<<<<<<
        # if isinstance(loc, list) and len(loc)==2:
        #     # Setting the x and y coordinates
        #     if self.check_loc(loc[0],loc[1]):
        #         self.loc = loc
        #
        #         piece_locs[self].loc
        # else:
        #    print 'Invalid coordinates. Expected "loc" to be a list with \
        #    two positive intigers.'

###################################################

    def move(self, x, y):
        # x and y being the new coordinates
        try:
            if [x,y] in self.moves:
                if self.check_loc(x,y):
                    result, piece = self.check_for_piece(x,y)
                    if result:
                        if self.eat(piece):
                            self.update_loc(x, y)
                        else:
                            return
                    else:
                        self.update_loc(x, y)

                    # Generating new possible moves
                    for piece in piece_locs:
                        piece.possible_moves()
                    return
            else:
                print "Can't move there or may not be able to move this piece"
                return
        except:
            print "Can't move there or may not be able to move this piece"



###################################################

    def check_loc(self, x, y, display_error = True):
        error = "Invalid coordinates. Outside of board."

        if x <= 0 or y <= 0:
            if display_error:
                print error
            return False

        if x > board_size or y > board_size:
            if display_error:
                print error
            return False
        return True

###################################################

    def check_for_piece(self, x, y):
        # Returns a boolean and the instace of the piece in that location
        if piece_locs == {}:
            return False, None

        for piece in piece_locs:
            if [x,y] == piece_locs[piece]:
                return True, piece
        return False, None

###################################################

    def update_loc(self, x, y):
        self.loc = [x, y]
        piece_locs[self] = self.loc

###################################################

    def eat(self, eaten):
        if self.team != eaten.team:
            # Simulating moving the piece off the board
            eaten.update_loc(-1, board_size)
            eaten.moves = None
            return True
        else:
            print "Friendly piece is already in that location."
            return False

###################################################

    def possible_moves(self):
        # Only here beacause otherwise Piece direct instances will throw
        # constant erros when trying to update their possible moves.
        #
        # Since possible_moves() is the function responsible for the
        # movement parameters of each piece type (ex. pawn, ...) it's not
        # necesary to have anyhting here.
        pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print "Running piece.py"

# pawn = Piece([1, 4], "black")
# queen = Piece([4, 1], "white")
