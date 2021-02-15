from _node import Node


# Calculate the L distance between Nodes
class path_finder():
    def heuristic(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)
