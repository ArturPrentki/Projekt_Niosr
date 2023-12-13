#!/usr/bin/env python3

# Copyright 2023 stask
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist



class RobotControlNode(Node):

    def __init__(self):
        super().__init__('robot_control_node')
        self.subscription = self.create_subscription(Point,'point', self.listener_callback, 10)
        self.subscription
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 1)

    def listener_callback(self, point):
        self.get_logger().info(f'x: "{point.x}" y: "{point.y}"')
        velocity_msg = Twist()
        if (point.y < 150):
            velocity_msg.linear.x = 0.5
        elif (point.y > 300):
            velocity_msg.linear.x = -0.5
        else:  
            velocity_msg.linear.x = 0.0
        if(point.x > 400):
            velocity_msg.angular.z = -0.5
        elif(point.x < 200):
            velocity_msg.angular.z = 0.5
        else:
            velocity_msg.angular.z = 0.0
        self.publisher.publish(velocity_msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = RobotControlNode()
    try:
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
