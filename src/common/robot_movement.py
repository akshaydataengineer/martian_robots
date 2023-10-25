from constants.orientation import Orientation


def move_clockwise(direction):
    switcher = {
        Orientation.North.value: Orientation.East.value,
        Orientation.East.value: Orientation.South.value,
        Orientation.South.value: Orientation.West.value,
        Orientation.West.value: Orientation.North.value,
    }
    return switcher.get(direction, None)


def move_anti_clockwise(direction):
    switcher = {
        Orientation.North.value: Orientation.West.value,
        Orientation.East.value: Orientation.North.value,
        Orientation.South.value: Orientation.East.value,
        Orientation.West.value: Orientation.South.value,
    }
    return switcher.get(direction, None)