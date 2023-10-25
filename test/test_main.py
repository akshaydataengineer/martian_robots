import os
import unittest
from main import process_robot_movements
from common.file_operation import get_json_object_from_file


class MainFunction(unittest.TestCase):

    def test_main_function_output(self):
        args = ['-i', os.getcwd() + '/files/input_data.json',
                '-o', os.getcwd() + '/files/output_data.json']
        self.assertTrue(process_robot_movements(args))
        data = get_json_object_from_file(os.getcwd() + '/files/output_data.json')
        for item in data:
            if item['id'] == 'input-1':
                self.assertTrue(len(item['error_msg']) == 0)
                self.assertTrue(len(item['robot_last_location']) == 3)
                self.assertTrue('1 1 E' in list(item['robot_last_location']))
                self.assertTrue('2 3 S' in list(item['robot_last_location']))
                self.assertTrue('3 3 N LOST' in list(item['robot_last_location']))
            else:
                self.assertTrue(len(item['error_msg']) > 0)
                self.assertTrue(len(item['robot_last_location']) == 0)


if __name__ == '__main__':
    unittest.main()
