from typing_extensions import Self
import rospy
import std_msgs.msg
import geometry_msgs.msg
import sensor_msgs.msg

class WanderBot():
    def __init__(self) -> None:       
        # self.node_handle = rospy.init_node('wanderbot')
        self.obstacle_threshold = 1.0 # in meters

    def DetectObst(self, lidar_data: list):
        """Check Lidar scan data for values less then the threshold. 
        If data has value below threshold then an obstacle has been detected.

        Args:
            lidar_data (list): Lidar scan data

        Returns:
            (bool): True if an obstacle has been detected, False if not
        """
        for data in lidar_data:
            if data <= self.obstacle_threshold:
                return True
        return False

    def WanderBotSub(self):
        pass

    def WanderBotCallback(self, scan_msg):
        pass
