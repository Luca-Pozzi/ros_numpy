#!/usr/bin/env python

import os
import numpy as np
import cv2

import rospy
import ros_numpy
from sensor_msgs.msg import CompressedImage

ONLINE = False

if __name__ == '__main__':
    # Get the path of this script
    wd = os.path.abspath(os.path.dirname(__file__))
    if ONLINE:
        # If connected to a robot/simulation, acquire a message from topic
        rospy.init_node('compressed_image_converter')
        msg = rospy.wait_for_message('/xtion/rgb/image_rect_color/compressed', CompressedImage)
        
        # Save the message fields (apart from `header`) for offline use
        fmt = msg.format
        raw_data = msg.data
        with open(os.path.join(wd, 'fmt.txt'), 'w') as f:
            f.write(fmt)
        with open(os.path.join(wd, 'raw_data.txt'), 'wb') as f:
            f.write(raw_data) 
    else:
        # If not connected to a robot/simulation, load the saved message fields
        with open(os.path.join(wd, 'fmt.txt'), 'r') as f:
            fmt = f.read()
        with open(os.path.join(wd, 'raw_data.txt'), 'rb') as f:
            raw_data = f.read() 

    dts = ros_numpy.image.name_to_dtypes
    dts = ros_numpy.compressed_image.name_to_dtypes
    print(dts)
    print(len(raw_data))
    print(fmt)
    depth_fmt, compr_type = fmt.split(';')
    data = np.frombuffer(raw_data, dtype = np.uint8)
    # remove white space
    depth_fmt = depth_fmt.strip()
    '''
    img = ros_numpy.numpify(msg)
    cv2.imshow('test', img)
    '''