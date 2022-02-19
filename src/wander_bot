#!/usr/bin/env python
 
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WanderBot():
    def __init__(self):       
        self.wander_bot_node = rospy.init_node('wanderbot')
        self. cmd_vel_topic = '/cmd_vel'
        self.vel_pub = rospy.Publisher(self.cmd_vel_topic, Twist, queue_size=100)
        self.scan_topic = '/scan'
        self.scan_sub = rospy.Subscriber(self.scan_topic, LaserScan, self.WanderBotCallback, queue_size=100)
        self.obstacle_threshold = 1.0 # in meters

    def DetectObst(self, lidar_data):
        """Check Lidar scan data for values less then the threshold. 
        If data has value below threshold then an obstacle has been detected.

        Args:
            lidar_data (list): Lidar scan data

        Returns:
            (bool): True if an obstacle has been detected, False if not
        """

        i = 20
        for i in range(160):
            # data in lidar_data:
            if lidar_data[i] <= self.obstacle_threshold:
                return True
        return False

    def WanderBotCallback(self, scan_msg):
        """Callback function to publish velocities depending on if an obstacle is or is not detected.

        Args:
            (scan_msg): Lidar scan data
        """        

        velocity = Twist()
        lidar_data = scan_msg.ranges

        if not self.DetectObst(lidar_data):
            rospy.loginfo('No obstacle detected, driving forward')
            velocity.linear.x = 0.5
            velocity.angular.z = 0.0
        else:
            rospy.loginfo('Obstacle detected, turning')
            velocity.linear.x = 0.0
            velocity.angular.z = -0.5

        self.vel_pub.publish(velocity)

if __name__ == '__main__':
    Bot = WanderBot()
    # Bot.WanderBotPubSub()
    rospy.spin()
