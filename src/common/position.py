from constants.orientation import Orientation


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RobotPosition:
    def __init__(self, direction, coordinate):
        self.coordinate = coordinate
        self.direction = direction
