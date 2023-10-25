import unittest
import common.command as com
from common.parser import validate_command_sequence, parse_coordinate, parse_initial_robot_position


class MyTestCase(unittest.TestCase):
    def test_validate_command_sequence(self):
        command = "FRRFLLFFRRFLL"
        self.assertEqual(validate_command_sequence(command), True)
        command = "FRXXXXX"
        self.assertEqual(validate_command_sequence(command), False)
        command = ""
        self.assertEqual(validate_command_sequence(command), False)

    def test_coordinate_class(self):
        obj = parse_coordinate("5 3")
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 3)
        obj = parse_coordinate("    50 4    ")
        self.assertEqual(obj.x, 50)
        self.assertEqual(obj.y, 4)
        obj = parse_coordinate("A B")
        self.assertTrue(obj.x is None)

    def test_robot_position_class(self):
        obj = parse_initial_robot_position("5 3 N")
        self.assertEqual(obj.coordinate.x, 5)
        self.assertEqual(obj.coordinate.y, 3)
        self.assertEqual(obj.direction, 'N')
        obj = parse_initial_robot_position("    50 4 S    ")
        self.assertEqual(obj.coordinate.x, 50)
        self.assertEqual(obj.coordinate.y, 4)
        self.assertEqual(obj.direction, 'S')
        obj = parse_initial_robot_position("5 3 AX")
        self.assertTrue(obj.direction is None)


if __name__ == '__main__':
    unittest.main()
