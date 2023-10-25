def is_out_of_grid(max_coordinate, curr_coordinate):
    if curr_coordinate.x < 0 or curr_coordinate.y < 0 \
            or curr_coordinate.x > max_coordinate.x or curr_coordinate.y > max_coordinate.y:
        return True
    return False


def is_known_lost_location(curr_robot_position, known_location):
    for pos in known_location:
        if curr_robot_position.direction == pos.direction and curr_robot_position.coordinate.x == pos.coordinate.x \
                and curr_robot_position.coordinate.y == pos.coordinate.y:
            return True
    return False
