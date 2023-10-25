## Problem: Martian Robots 

### The Problem 

The surface of Mars can be modelled by a rectangular grid around which robots are able to move according to instructions provided from Earth. You are to write a program that determines each sequence of robot positions and reports the final position of the robot. 

A robot position consists of a grid coordinate (a pair of integers: x-coordinate followed by ycoordinate) and an orientation (N, S, E, W for north, south, east, and west). 

A robot instruction is a string of the letters “L”, “R”, and “F” which represent, respectively, the instructions: 

• Left : the robot turns left 90 degrees and remains on the current grid point. 

• Right : the robot turns right 90 degrees and remains on the current grid point. 

• Forward : the robot moves forward one grid point in the direction of the current orientation and maintains the same orientation. The direction North corresponds to the direction from grid point (x, y) to grid point (x,y+1). There is also a possibility that additional command types maybe required in the future and provision should be made for this. 

Since the grid is rectangular and bounded, a robot that moves “off” an edge of the grid is lost forever. However, lost robots leave a robot “scent” that prohibits future robots from dropping off the world at the same grid point. The scent is left at the last grid position the robot occupied before disappearing over the edge. An instruction to move “off” the world from a grid point from which a robot has been previously lost is simply ignored by the current robot.

### Input 

The first line of input is the upper-right coordinates of the rectangular world, the lower-left coordinates are assumed to be 0,0. 

The remaining input consists of a sequence of robot positions and instructions (two lines per robot). 

A position consists of two integers specifying the initial coordinates of the robot and an orientation (N, S, E, W), all separated by white space on one line. A robot instruction is a string of the letters “L”, “R”, and “F” on one line. 

Each robot is processed sequentially, i.e., finishes executing the robot instructions before the next robot begins execution. 

The maximum value for any coordinate is 50. All instruction strings will be less than 100 characters in length. 

### Output 

For each robot position/instruction in the input, the output should indicate the final grid position and orientation of the robot. If a robot falls off the edge of the grid the word “LOST” should be printed after the position and orientation. 

### Sample Input 

5 3 

1 1 E 

RFRFRFRF 

3 2 N 

FRRFLLFFRRFLL 

0 3 W 

LLFFFLFLFL 

### Sample Output 

11 E 

3 3 N LOST 

2 3 S

## Solution
### Assumptions
* The solution will be run on a mac os using PyCharm and Python version 3.10 or higher

### Out of Scope
Exception handling and logging is not considered in scope due to timeline


### Code Strecture

#### Folder: src 

Below is the file description under src folder. 
1. constants/input_tag.py -> Enum to store the tag value of JSON file
2. constants/instuction.py -> Enum to store the instruction value such as L, R, F
3. constants/rientation.py -> Enum to store the orientation info such as N, S, W , E
4. common/file_operation.py -> function to read and write data into files 
5. common/parser.py -> function to parse input data and validate it 
6. common/validation.py -> function to validate data and check if robot is moving out of edge. 
7. common/robot_movement.py -> function identify robot movement direction and find next orientation. 
8. common/position.py -> class defination to store coordinate and orientation information.
9. common/command.py -> Function to store teh overall logic flow against instruction execution and result storage.
10. main.py -> Entry point to execute the program. 


#### Folder: test 

This folder contaons test cases and sample data files used to perfomr testing. 

#### How to Run this code

1. Prepare input file that contains max plane size, initial point and movement command. 
   Sample input file is accessible in folder /test/files/input_data.json

2. Run the below command to use the input file and write output to file. 
   Python3 main.py -i <inputfile> -o <outputfile>

   e.g. 
   Python3  src/main.py -i FOLDER_PATH/martian_robots/test/files/input_data.json -o FOLDER_PATH/martian_robots/test/files/output_data.json

3. Review the results in output file. 

###### Sample Input
{
  "input": [
    {
      "id": "input-1",
      "max_plane_size": "5 3",
      "robot_movement_input": [
        {
          "initial_point": "1 1 E",
          "command_sequence": "RFRFRFRF"
        },
        {
          "initial_point": "3 2 N",
          "command_sequence": "FRRFLLFFRRFLL"
        },
        {
          "initial_point": "0 3 W",
          "command_sequence": "LLFFFLFLFL"
        }
      ]
    },
    {
      "id": "input-2",
      "max_plane_size": "5 A",
      "robot_movement_input": [
        {
          "initial_point": "1 1 E",
          "command_sequence": "RFRFRFRF"
        }
      ]
    },
    {
      "id": "input-3",
      "max_plane_size": "5 5",
      "robot_movement_input": [
        {
          "initial_point": "1 1 AX",
          "command_sequence": "RFRFRFRF"
        }
      ]
    },
    {
      "id": "input-4",
      "max_plane_size": "5 5",
      "robot_movement_input": [
        {
          "initial_point": "1 1 E",
          "command_sequence": "RFRFXXXXXXX"
        }
      ]
    }
  ]
}
###### Sample Output
[
   {
      "id": "input-1",
      "error_msg": [],
      "robot_last_location": [
         "1 1 E",
         "3 3 N LOST",
         "2 3 S"
      ]
   },
   {
      "id": "input-2",
      "error_msg": [
         "unexpected value for input max_plane_size: 5 A"
      ],
      "robot_last_location": []
   },
   {
      "id": "input-3",
      "error_msg": [
         "unexpected value for input initial_point: 1 1 AX"
      ],
      "robot_last_location": []
   },
   {
      "id": "input-4",
      "error_msg": [
         "unexpected value for input command_sequence: RFRFXXXXXXX"
      ],
      "robot_last_location": []
   }
]
