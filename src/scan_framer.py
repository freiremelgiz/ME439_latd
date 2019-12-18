#!/usr/bin/env python

## scan_framer.py
# This program receives a LaserScan message from /scan
# and re-publishes it to /framed_scan.
# This was necessary when using ROS Distributed Systems
# because tf frame data was lost over network.
__author__ = "Victor Freire, Rebecca Roembke, Wanyue Xu"
__email__ = "freiremelgiz@wisc.edu"

# Dependencies
import rospy
import tf
from sensor_msgs.msg import LaserScan

## INIT Objects
# Initialize node
rospy.init_node('scan_framer', anonymous=False)
# Create publisher for framed LaserScan data
pub = rospy.Publisher('/framed_scan', LaserScan, queue_size = 0)

# Dummy callback
def frame_scan(msg):
    pub.publish(msg)

# Listens for LaserScan data continuously when called
def transformer():
    # Create Subscriber for LaserScan data
    sub = rospy.Subscriber('/scan', LaserScan, frame_scan)
    rospy.spin()

if __name__ == '__main__':
    try:
        transformer()
    except rospy.ROSInterruptException:
        pass
