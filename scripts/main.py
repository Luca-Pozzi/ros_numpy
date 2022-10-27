#!/usr/bin/env python

import numpy as np
import cv2

import rospy
import ros_numpy
from sensor_msgs.msg import Image

class Converter:
    def __init__(self, depth):
        self.depth = depth
        self.img = None
    
    def callback(self, msg):
        self.img = ros_numpy.numpify(msg)

if __name__ == "__main__":
    rospy.init_node('tester')
    conv = Converter(depth = False)
    sub = rospy.Subscriber('/xtion/depth_registered/image_raw', Image, conv.callback)
    #sub = rospy.Subscriber('/xtion/rgb/image_raw', Image, conv.callback)    
    try:
        while not rospy.is_shutdown():
            if conv.img is not None:
                cv2.imshow('img', conv.img)
                cv2.waitKey(1)
                print(conv.img.shape)
                print(np.nanmax(conv.img), np.nanmin(conv.img))

    except KeyboardInterrupt:
        pass
