import pygame
import math
from queue import PriorityQueue

# Size of the screen
WIDTH = 800
# Since we are creating a Square we can use the Width for both length and width
WIN = pygame.display.set_mode(WIDTH, WIDTH)
pygame.display.set_caption("A* Path Finding Algorithm")
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

    # Return the color Red when Node is closed
    def is_closed(self):
        return self.color == RED

    # Return the color Green when Node is open
    def is_open(self):
        return self.color == GREEN

    # Return the color Black when Node is a barrier
    def is_barrier(self):
        return self.color == BLACK

    # Return the color Orange when is the Start Node
    def is_start(self):
        return self.color == ORANGE

    # Return the color Turquoise when is the Start Node
    def is_end(self):
        return self.color == TURQUOISE

    # Reset the color of the Node to White
    def reset(self):
        return self.color == WHITE

    def make_close(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lessthan__(self, other):
        return False


# Calculates using Manhattan distance
# Think of an L between the two points
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + (y1 - y2)

# create a grid using the number of rows and the width of entire grid
def make_grid(rows, width):
    grid = []
    gap = width
