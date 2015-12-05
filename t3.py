class Board(object):
    """A game board"""

    # track spaces individually, or keep in list?
    spaces = []

    def __init__(self):
        """Makes spaces for new boards"""

        for num1 in range(-1, 2):
            for num2 in range(-1, 2):
                print num1, num2
                space = Space(num1, num2)
                self.spaces.append(space)

    def available_spaces(self):
        """Returns list of open spaces"""

        available_spaces = []
        for space in self.spaces:
            if space.player == None:
                available_spaces.append(space)

        return available_spaces

    def is_won(self):
        """Checks whether a player has won"""
        pass

    def winning_move(self, player):
        """Checks whether there is a winning move available for a given player"""
        pass


class Space(object):
    """A space on the game board"""

    player = None

    def __init__(self, x, y):
        """Sets coordinates of new space"""

        self.x = x
        self.y = y

    def __repr__(self):
        """Shows coordinates when object printed"""

        return "(%s, %s)" % (self.x, self.y) 




if __name__ == "__main__":

    board = Board()

