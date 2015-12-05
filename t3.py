class Board(Object):
    """A game board"""


    # track spaces individually, or keep in list?
    self.spaces = []


    def available_spaces(self):
        """Returns list of open spaces"""
        
        available_spaces = []
        for space in self.spaces:
            if space.player = None
                available_spaces.append(space)
        return available_spaces


class Space(Object):
    """A space on the game board"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player = None

