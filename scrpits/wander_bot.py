#!/usr/bin/env python
 
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WanderBot():
    def __init__(self) -> None:       
        self.wander_bot_node = rospy.init_node('wanderbot')
        self.vel_pub = rospy.Publisher(self.cmd_vel_topic, Twist(), queue_size=10)
        self. cmd_vel_topic = '/cmd_vel'
        self.scan_sub = rospy.Subscriber(self.scan_topic, LaserScan(), self.WanderBotCallback())
        self.scan_topic = '/scan'
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

    def WanderBotPubSub(self):
        self.vel_pub
        self.scan_sub

    def WanderBotCallback(self, scan_msg):
        velocity = Twist()
        lidar_data = scan_msg.ranges

        if self.DetectObst(lidar_data):
            rospy.loginfo('Obstacle detected, turning')
            velocity.linear.x = 0.0
            velocity.angular.z = -0.5
        else:
            rospy.loginfo('No obstacle detected, driving forward')
            velocity.linear.x = 0.5
            velocity.angular.z = 0.0

        self.vel_pub(velocity)
