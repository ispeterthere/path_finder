# Constant Colors that will be used
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # Keep Track of the position of Nodes on a Grid using their X and Y Coordinate
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Get the current position of the Node
    def get_pos(self):
        return self.row, self.col

    # Return the color red when Node is closed
    def is_closed(self):
        return self.color == RED

    # Return the color green when Node is open
    def is_open(self):
        return self.color == GREEN

    # Return the color black when Node is a barrier
    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE
