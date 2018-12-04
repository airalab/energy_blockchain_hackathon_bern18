# -*- coding: utf-8 -*-

import rosbag
from std_msgs.msg import String, Float64


bag = rosbag.Bag('./green.bag', 'w')

'''
/consumption/provenance/type: std_msgs/String: ‘Wind’,
/consumption/provenance/proof: std_msgs/String <link_to_tobalaba>
/consumption/quantity: std_msgs/Float64: 91639.00
/consumption/compensation/factor: std_msgs/Float64: 0,
/consumption/compensation/proof: std_msgs/String: ‘None’,
/consumption/compensation/quantity: std_msgs/Float64: 0
'''

def write(bag, topic, msg_type, value):
    bag.write(topic, msg_type(data=value))

try:
    write(bag, '/consumption/provenance/type', String, 'Wind')
    write(bag, '/consumption/provenance/proof', String, '0x9715f1a4df2d42d71ff74d9cc07715b20843fd0a')
    write(bag, '/consumption/quantity', Float64, 91639.00)
    write(bag, '/consumption/compensation/factor', Float64, 0.0)
    write(bag, '/consumption/compensation/proof', String, 'None')
    write(bag, '/consumption/compensation/quantity', Float64, 0)
finally:
    bag.close()
