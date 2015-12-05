class Board(object):
    """A game board"""

    # These both store the same objects, nested and flat.
    spaces = []
    rows = [] # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


    def __init__(self):
        """Makes spaces for new boards"""

        location = 0

        for num1 in range(-1, 2):
            column = []

            for num2 in range(-1, 2):
                # print location, " at: ", num2, num1
                space = Space(num2, num1, location)
                self.spaces.append(space)
                column.append(space)
                location += 1

            self.rows.append(column)


    def available_spaces(self):
        """Returns list of open spaces"""

        available_spaces = []
        for space in self.spaces:
            if space.player == 0:
                available_spaces.append(space)

        return available_spaces


    def who_won(self):
        """Checks whether a player has won"""
        # check for winning row
        for row in self.rows:
            if (row[0].player != 0) and (row[0].player == 
                                            row[1].player == 
                                            row[2].player):
                return row[0].player

        # check for winning column
        for i in range(3):
            if (self.rows[0][i].player != 0) and (self.rows[0][i].player == 
                                                    self.rows[1][i].player == 
                                                    self.rows[2][i].player):
                return self.rows[0][i].player

        # check for diagonals
        if (self.rows[0][0].player != 0) and (self.rows[0][0].player ==
                                                self.rows[1][1].player == 
                                                self.rows[2][2].player):
            return self.rows[0][0].player

        elif (self.rows[2][0].player != 0) and (self.rows[2][0].player ==
                                                self.rows[1][1].player == 
                                                self.rows[0][2].player):
            return self.rows[2][0].player

        # leave as none, not 0, so that later I can check for if who_won changes to an int, move into that square
        # that would both block a potentially winning opponent and win the game for the computer
        return None


    def winning_move(self, player):
        """Checks whether there is a winning move available for a given player"""
        pass


    def print_board(self):
        """Prints board to screen"""

        for i in range(len(self.rows)):
            print self.rows[i][0].player, "||", self.rows[i][1].player, "||", self.rows[i][2].player
            if i < 2:
                print "==========="


class Space(object):
    """A space on the game board"""

    player = 0


    def __init__(self, x, y, location):
        """Sets coordinates of new space"""

        self.x = x
        self.y = y
        self.location = location


    def __repr__(self):
        """Shows coordinates when object printed"""

        return "%s: (%s, %s)" % (self.location, self.x, self.y)


if __name__ == "__main__":

    board = Board()
    # board.spaces[0].player = 1
    # board.spaces[4].player = 2
    # board.spaces[1].player = 1
    board.spaces[0].player = 2
    board.spaces[4].player = 2
    board.spaces[8].player = 1
    board.print_board()
    print "Who won: ", board.who_won()

