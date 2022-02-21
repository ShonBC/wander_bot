# Wander_bot
Implementation of a simple wandering algorithm much like a Roomba robot vacuum cleaner. The robot should move forward until it reaches an obstacle (but not colliding), then rotate in place until the way ahead is clear, then move forward again and repeat. The obstacle detection monitors the LiDAR scan data between the ranges of 0-60 degrees and 300-360 degrees with 0 being straight forward.

# Prerequisites:
- Ubuntu 18.04
- ROS Melodic
- ROS Beginner tutorials installed:
    sudo apt-get install ros-melodic-ros-tutorials
- Turtlebot3 ROS Package

# Build and Run:
Clone the repo in the src folder of a catkin workspace.

    git clone https://github.com/ShonBC/wander_bot.git

Build the packages in the workspace. 
If the catkin workspace was created using catkin_make then navigate to the catkin workspace directory and run:

    catkin_make
    . ~/<catkin_ws_directory_name>/devel/setup.bash

If the workspace was created using catkin build then run:

    catkin build
    . ~/<catkin_ws_directory_name>/devel/setup.bash

# Run the Wander_Bot_Node:
By default the wander_bot.launch file will not record a bag file. To run the node and record a bag file run:

    roslaunch wander_bot wander_bot.launch record_bag:=true

The bag file will be recorded in the [docs/bag](docs/bag) directory. To examine the bag file first navigate into the [docs/bag](docs/bag) directory in a terminal and run:

    rosbag info wander_bag.bag
    
To play the bag file back and see the published messages first ensure a ROS master is active, in a terminal run:

    roscore

In a new terminal echo the cmd_vel topic:

    rostopic echo /cmd_vel

In a new terminal navigate to the [docs/bag](docs/bag) directory and run:

    roscd wander_bot/docs/bag
    rosbag play wander_bag.bag
