# Projekt_Niosr
Projekt zaliczeniowy z Niosr Artur Prentki i Stanisław Kuczma


# Robot_control
## Requirements
### usb_cam
install package 
https://github.com/ros-drivers/usb_cam.git
### gazebo and turtlebot3
install turtle bot for gazebo and export dependecies
`sudo apt install ros-humble-turtlebot3*` </br>
`sudo apt install gazebo`</br>
`export TURTLEBOT3_MODEL=burger`</br>
`export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH: ros2 pkg \
prefix turtlebot3_gazebo \
/share/turtlebot3_gazebo/models/`

```bash
rosdep install --from-paths src --ignore-src -y
colcon build --symlink-install --packages-up-to robot_control
ros2 launch robot_control robot_control.launch.py
```

### Input

| Name         | Type                  | Description  |
| ------------ | --------------------- | ------------ |
| `/image_raw` | sensor_msgs::msg::Image | Camera live feed. |

### Output

| Name         | Type                  | Description  |
| ------------ | --------------------- | ------------ |
| `/cmd_vel` | geometry_msgs::msg::Twist | Robot control signal. |
| `/point` | geometry_msgs::msg::Point | Center point of aruco cube. |



### Description

Launch starts two nodes. /camera_aruco_node checks if there is topic /image_raw available, find aruco tag 7x7x1000 and publishes centerpoint location under /point topic. Second node /robot_control_node takes point coordinates and according to its position sets /cmd_vel in order to move robot (Front, Back, Left, Right) when aruco tag is in the center robot stays idle.




## References / External links
https://chev.me/arucogen/ </br>
Aruco tag generator </br>
https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html </br>
ROS website </br>
https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html </br>
OpenCV library with Aruco tags </br>


