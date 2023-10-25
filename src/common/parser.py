import sys, getopt
from constants.instruction import Instruction
from constants.orientation import Orientation
from common.position import Coordinate, RobotPosition
from constants.input_tag import JsonPaserTag

LOST_KEYWORD = ' LOST'


def validate_command_sequence(sequence):
    command = sequence.strip()
    if len(command) < 1 or len(command) > 100:
        return False
    for unique_command in list(dict.fromkeys(command)):
        if unique_command not in [Instruction.Left.value, Instruction.Right.value, Instruction.Forward.value]:
            return False
    return True


def parse_coordinate(sequence):
    coordinate = sequence.strip().split(' ')
    x = None
    y = None
    if coordinate[0].isdigit() and coordinate[1].isdigit():
        x = int(coordinate[0])
        y = int(coordinate[1])
    return Coordinate(x, y)


def parse_initial_robot_position(sequence):
    position = sequence.strip().split(' ')
    direction = None
    valid_dir = [Orientation.West.value, Orientation.East.value, Orientation.North.value, Orientation.South.value]
    if position[2] in valid_dir:
        direction = position[2]
    return RobotPosition(direction, parse_coordinate(sequence))


def parse_input_data(input_command_sequence):
    error_msg = list()
    tag = JsonPaserTag
    max_coordinate = parse_coordinate(input_command_sequence[tag.MaxPlaneSize.value])
    if max_coordinate.x is None:
        error_msg.append("unexpected value for input max_plane_size: " + input_command_sequence[tag.MaxPlaneSize.value])
    robot_movement_sequence = input_command_sequence[tag.RobotMovement.value]
    for movement_sequence in robot_movement_sequence:
        pos = parse_initial_robot_position(movement_sequence[tag.RobotInitialLocation.value])
        if pos.direction is None or pos.coordinate.x is None:
            error_msg.append(
                "unexpected value for input initial_point: " + movement_sequence[tag.RobotInitialLocation.value])
        command_sequence = movement_sequence[tag.CommandSeq.value]
        if not validate_command_sequence(command_sequence):
            error_msg.append("unexpected value for input command_sequence: " + movement_sequence[tag.CommandSeq.value])
    return max_coordinate, robot_movement_sequence, error_msg


def build_output_text(curr_robot_position, is_lost):
    text = ''
    if is_lost:
        text = LOST_KEYWORD
    return str(curr_robot_position.coordinate.x) + ' ' + str(curr_robot_position.coordinate.y) + ' ' + \
           curr_robot_position.direction + text


def parse_command_line_arg(argv):
    input_file_path = ""
    output_file_path = ""
    opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <inputfile> -o <outputfile>')
        elif opt in ("-i", "--ifile"):
            input_file_path = arg
        elif opt in ("-o", "--ifile"):
            output_file_path = arg

    return input_file_path, output_file_path
