import enum


# Using enum class create enumerations
class JsonPaserTag(enum.Enum):
    Input = 'input'
    Id = 'id'
    MaxPlaneSize = 'max_plane_size'
    RobotMovement = 'robot_movement_input'
    RobotInitialLocation = 'initial_point'
    CommandSeq = 'command_sequence'
    ErrorMsg = 'error_msg'
    RobotLastLocation = 'robot_last_location'

