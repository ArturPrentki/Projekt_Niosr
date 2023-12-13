#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
import cv2 
import numpy as np 
from geometry_msgs.msg import Point
from cv_bridge import CvBridge

class CameraArucoSubscriber(Node):
    def __init__(self):
        super().__init__('camera_aruco_subscriber')
        self.window_name = "camera"
        self.subscription = self.create_subscription(Image,'image_raw',self.listener_callback,10)
        self.subscription 
        self.point = None
        self.publisher = self.create_publisher(Point, 'point', 10)

    def listener_callback(self, image_data):
        cv_image = CvBridge().imgmsg_to_cv2(image_data, desired_encoding='bgr8')
        self.detectAruco(cv_image)
        self.pointPublisher()

    def detectAruco(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_1000)
        param = cv2.aruco.DetectorParameters_create()
        corners, ids, rejected = cv2.aruco.detectMarkers(gray, dictionary, parameters=param)
        if len(corners) == 1:
            corner = corners[0][0]
            center_x = int((corner[0][0] + corner[1][0] + corner[2][0] + corner[3][0]) / 4)
            center_y = int((corner[0][1] + corner[1][1] + corner[2][1] + corner[3][1]) / 4)
            self.point = (center_x, center_y)
            cv2.circle(frame,self.point, 5, (0,0,255), -1)

        cv2.aruco.drawDetectedMarkers(frame, corners, ids)               
        cv2.imshow(self.window_name, frame)
        cv2.waitKey(25)

    def pointPublisher(self):
        if(self.point is not None):
            point_msg = Point()
            point_msg.x = float(self.point[0])
            point_msg.y = float(self.point[1])
            point_msg.z = 0.0
            self.publisher.publish(point_msg)

def main(args=None):
    rclpy.init(args=args)
    camera_aruco_subscriber = CameraArucoSubscriber()
    rclpy.spin(camera_aruco_subscriber)
    camera_aruco_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()