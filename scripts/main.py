#!/usr/bin/env python

import os
import numpy as np
import cv2

import rospy
import ros_numpy
from sensor_msgs.msg import CompressedImage

from struct import unpack

marker_mapping = {
    0xffd8: "Start of Image",
    0xffe0: "Application Default Header",
    0xffdb: "Quantization Table",
    0xffc0: "Start of Frame",
    0xffc4: "Define Huffman Table",
    0xffda: "Start of Scan",
    0xffd9: "End of Image"
}

ONLINE = True

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
        b = [x.encode('hex') for x in raw_data] 
        print(b)
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
    '''
    # Get the compression type and CVMat datatype
    depth_fmt, compr_type = fmt.split(';')
    print(compr_type)
    # Remove the white spaces
    depth_fmt = depth_fmt.strip()
    # Get the numpy dtype  and the number of channels corresponding to the CVMat datatype
    dtype, channels = ros_numpy.compressed_image.name_to_dtypes[depth_fmt]
    # Given the dtype, get the size of a single datapoint (in bytes)
    item_size = np.ones((1), dtype = dtype).itemsize    # NOTE: quite bulky
    print(480 * 640 * item_size)
    print(raw_data.decode('utf-8').hex())
    #print(raw_data[1].decode('utf-8'))
    '''

    '''
    data = np.frombuffer(raw_data, dtype = np.uint8, offset = 12)
    print(len(raw_data))
    print(len(data))
    '''
    
    '''
    img = ros_numpy.numpify(msg)
    cv2.imshow('test', img)
    '''