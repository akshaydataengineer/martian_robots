from constants.instruction import Instruction
from constants.orientation import Orientation
from constants.input_tag import JsonPaserTag
from common.position import Coordinate, RobotPosition
from common.robot_movement import move_clockwise, move_anti_clockwise
from common.parser import parse_input_data, parse_initial_robot_position, build_output_text
from common.validation import is_out_of_grid, is_known_lost_location


def next_forward_coordinate(curr_direction, curr_coordinate):
    if curr_direction == Orientation.North.value:
        return Coordinate(curr_coordinate.x, curr_coordinate.y + 1)
    elif curr_direction == Orientation.South.value:
        return Coordinate(curr_coordinate.x, curr_coordinate.y - 1)
    elif curr_direction == Orientation.East.value:
        return Coordinate(curr_coordinate.x + 1, curr_coordinate.y)
    else:
        return Coordinate(curr_coordinate.x - 1, curr_coordinate.y)


def move_robot(command, curr_robot_position, max_coordinate, known_location):
    if command == Instruction.Forward.value:
        if is_known_lost_location(curr_robot_position, known_location):
            return curr_robot_position
        next_coordinate = next_forward_coordinate(curr_robot_position.direction, curr_robot_position.coordinate)
        if is_out_of_grid(max_coordinate, next_coordinate):
            return None
        return RobotPosition(curr_robot_position.direction, next_coordinate)
    elif command == Instruction.Right.value:
        return RobotPosition(move_clockwise(curr_robot_position.direction), curr_robot_position.coordinate)
    elif command == Instruction.Left.value:
        return RobotPosition(move_anti_clockwise(curr_robot_position.direction), curr_robot_position.coordinate)
    return None


def execute_input_command(curr_robot_position, command_sequence, known_location, max_coordinate):
    for char in list(command_sequence.strip()):
        next_position = move_robot(char, curr_robot_position, max_coordinate, known_location)
        if next_position is None:
            return curr_robot_position, True
        curr_robot_position = next_position
    return curr_robot_position, False


def execute_input_command_sequence(input_command_sequence):
    known_location = list()
    output_location = list()
    tag = JsonPaserTag
    input_id = input_command_sequence[tag.Id.value]
    max_coordinate, robot_movement_sequence, error_msg = parse_input_data(input_command_sequence)
    if len(error_msg) == 0:
        for movement_sequence in robot_movement_sequence:
            curr_robot_position = parse_initial_robot_position(movement_sequence[tag.RobotInitialLocation.value])
            command_sequence = movement_sequence[tag.CommandSeq.value]
            curr_robot_position, is_lost =\
                execute_input_command(curr_robot_position, command_sequence, known_location, max_coordinate)
            if is_lost:
                known_location.append(curr_robot_position)
            output_location.append(build_output_text(curr_robot_position, is_lost))
    return {
        tag.Id.value: input_id,
        tag.ErrorMsg.value: error_msg,
        tag.RobotLastLocation.value: output_location
    }
