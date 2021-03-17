import pygame
import math
from queue import PriorityQueue

# Size of the screen
WIDTH = 800
# Since we are creating a Square we can use the Width for both length and width
WIN = pygame.display.set_mode((WIDTH, WIDTH))
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

    # Reset the color of the Node
    def reset(self):
        self.color = WHITE

    # Make a node start by assignin color
    def make_start(self):
        self.color = ORANGE

    # Make a node closed by assigning color
    def make_close(self):
        self.color = RED

    # Make a node open by assigning color
    def make_open(self):
        self.color = GREEN

    # Make a node a barrier by assigning color
    def make_barrier(self):
        self.color = BLACK

    # Make the end node by assigning color
    def make_end(self):
        self.color = TURQUOISE

    # Make the final path by assigning color
    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # self.row < self.total_rows - 1 checks it is not the last row
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # Moving Down
            self.neighbors.append(grid[self.row + 1][self.col])  # if not a barrier Add to the neighbor list

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # Moving UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # Moving Right
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row][self.col - 1].is_barrier():  # Moving Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lessthan__(self, other):
        return False


# Calculates using Manhattan distance
# Think of an L between the two points
# point1 is the starting point
# point2 is the ending point
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + (y1 - y2)
#Current is the end node that we are currently at
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# draw is a function
def algorithm(draw, grid, start, end):
    count = 0
    #Priority Queue has the smallest value at the beginning
    open_set = PriorityQueue()  # does not keep track of the items in the queue
    # The first number is the F score of first node
    open_set.put((0, count, start))
    came_from = {}  # Dictionary to Keep track of the path traveled from
    g_score = {node: float("inf") for row in grid for node in row}  # set the G score of all node to infinity
    g_score[start] = 0 #g score is the distance

    f_score = {node: float("inf") for row in grid for node in row}  # set the f score of all node to infinity
    f_score[start] = heuristic(start.get_pos(), end.get_pos())  # Get the f score from start to end

    # checks and keeps track of all the items in the priority queue and not in
    open_set_hash = {start}

    while not open_set.empty():
        # A way to exit the loop if user presses quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]  # Popping the lowest value F score
        open_set_hash.remove(current)  # remove any duplicates

        if current == end:  # If the popped node is the end node the algorithm finished
            reconstruct_path(came_from, end, draw)
            return True  # Make the path and

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1  # currently shortest distance and add 1
            if temp_g_score < g_score[neighbor]:  # If a better neighbor is found update g and f score of current neighbor
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1 #which node currently on
                    open_set.put((f_score[neighbor], count, neighbor)) #Add the neighbor to possible node set
                    open_set_hash.add(neighbor) #Add possible neighbor to the hash
                    neighbor.make_open()

        draw()

        if current != start: #If the current node is not a starting node close it
            current.make_close()

# create a grid to hold each node using the number of rows and the width of entire grid
# rows is the
def make_grid(rows, width):
    grid = []  # Create gri
    gap = width // rows  # The space between each node
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)  # Insert a Spot object into the grid list
            grid[i].append(node)

    return grid


# Draw each of the grid lines
def draw_grid(win, rows, width):
    GAP = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * GAP), (width, i * GAP))  # Start drawing a horizontal line for each row
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * GAP, 0), (j * GAP, width))  # Start drawing a vertical line for each row


# Draw the game window
# win is the window size
# grid is the
def draw(win, grid, rows, width):
    win.fill(WHITE)  # At the beginning of every frame with white to update

    for row in grid:
        for node in row:
            node.draw(win)  # Calls draw function that colors each node

    draw_grid(win, rows, width)  # Draws the gridline
    pygame.display.update()  # Update the game screen


# Get the clicked position on the grid
# pos is the mouse position
def get_clicked_pos(pos, rows, width):
    GAP = width // rows
    y, x = pos

    row = y // GAP
    col = x // GAP
    return row, col


# this is the Main loop
def main(win, width):
    ROWS = 50  # Amount of Rows to draw
    grid = make_grid(ROWS, width)
    # Initialize the start and end position
    start = None
    end = None

    run = True  # Variable to keep the game running
    started = False  # Has the algorithm started to not allow the user to stop the algorithm

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If you press the X on top right, then stop running the game
                run = false

            if started:  # If the algorithm has started not allow interruption to algorithm or modify nodes
                continue

            if pygame.mouse.get_pressed()[0]:  # Left
                pos = pygame.mouse.get_pos()  # Get the current position of the mouse
                row, col = get_clicked_pos(pos, ROWS,
                                           width)  # Use helper function to get the X Y coordinate of the node
                node = grid[row][col]  # Index the Row and Column in the grid assigning to Node
                if not start and node != end:  # If no start position is selected make the next Clicked on Node the start node
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node  # Make the current spot an end by assigning color
                    end.make_end()
                # If the spot clicked on is not a start or ending point then barriers will be created
                elif node != end and node != start:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # Right
                pos = pygame.mouse.get_pos()  # Get the current position of the mouse
                row, col = get_clicked_pos(pos, ROWS,
                                           width)  # Use helper function to get the X Y coordinate of the node
                node = grid[row][col]  # Index the Row and Column in the grid assigning to Node
                node.reset()  # Reset current node
                if node == start:  # Reset start Position
                    start = None
                elif node == end:  # Reset end Position
                    end = None

            if event.type == pygame.KEYDOWN:  # If the spacebar is pressed it updated the neighbors list
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

    pygame.quit()


main(WIN, WIDTH)
