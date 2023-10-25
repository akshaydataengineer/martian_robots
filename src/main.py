import sys
from common.command import execute_input_command_sequence
from common.file_operation import get_json_object_from_file, write_json_object_to_file
from common.parser import parse_command_line_arg
from constants.input_tag import JsonPaserTag


def process_robot_movements(argv):
    input_file_path, output_file_path = parse_command_line_arg(argv)
    result = list()
    if len(input_file_path) > 0 and len(output_file_path) > 0:
        file_data = get_json_object_from_file(input_file_path)
        input_data = file_data[JsonPaserTag.Input.value]
        for input_command_sequence in input_data:
            output_data = execute_input_command_sequence(input_command_sequence)
            result.append(output_data)
        write_json_object_to_file(output_file_path, result, 3)
    else:
        print('Invalid input command. execute "main.py -h" to get details on mandatory inputs.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sys.argv[1:])
    process_robot_movements(sys.argv[1:])
