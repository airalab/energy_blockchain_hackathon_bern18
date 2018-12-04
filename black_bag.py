# -*- coding: utf-8 -*-

import rosbag
from std_msgs.msg import String, Float64


bag = rosbag.Bag('./black.bag', 'w')

'''
/consumption/provenance/type: std_msgs/String: ‘Coal’
/consumption/provenance/proof: std_msgs/String ‘None’
/consumption/quantity: std_msgs/Float64: 91639.00
/consumption/compensation/factor: std_msgs/Float64: 0.94,
/consumption/compensation/proof: std_msgs/String: ‘0xae3e06ab88c735f8c4381f1955f44ab562479a7617dc1a0f4a4b921ed380a0d8’,
/consumption/compensation/quantity: std_msgs/Float64: 86140.66
'''

def write(bag, topic, msg_type, value):
    bag.write(topic, msg_type(data=value))

try:
    write(bag, '/consumption/provenance/type', String, 'Coal')
    write(bag, '/consumption/provenance/proof', String, 'None')
    write(bag, '/consumption/quantity', Float64, 91639.00)
    write(bag, '/consumption/compensation/factor', Float64, 0.94)
    write(bag, '/consumption/compensation/proof', String, '0xae3e06ab88c735f8c4381f1955f44ab562479a7617dc1a0f4a4b921ed380a0d8')
    write(bag, '/consumption/compensation/quantity', Float64, 86140.66)
finally:
    bag.close()
