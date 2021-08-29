
# JACOB Self-Driving Truck with induction charger

This repository contains code for an autonomous smallscale truck with wireless inductive charging.
It is part of our autonomous vehicle project and contains code for three different path following methods:
- SLAM with Pure Pursuit (and Stanley steering) steering controller
- Supervised Deep Learning steering controller with OpenCV
- Lane Detector with steering controller (PID) and OpenCV
- Ackermann Messages

The system is based on Ubuntu 16.04 with ROS Kinetic running on a Nvidia Jetson TX2. The truck itself is controlled by a Teensy 3.2 microcontroller. Other components used are the RPlidar A2M8 lidar and the Logitech C922 webcam.

#### Start-up
To start the autonomous system, type:
```sh
$ roslaunch car_cmd run.launch  
```

### ROS nodes 
| Folder | Functionality |
| ------ | ------ |
|Teensy|Contains the code for the Teensy microcontroller|
|ackermann_odom | Estimates odometry for Ackermann vehicle with IMU |
|aruco_detector|For detecting ArUco markers with camera, also contains generator|
|can_charger_node|ROS CAN bus interface for Jetson TX2|
|car_cmd|Central node for publishing car commands to microcontroller|
|car_gui|Graphical User Interface for status overviews|
|car_setup_tf|TF broadcaster (base_link to laser)|
|cv_lanetracker|OpenCV Lane Detector for center offset measure|
|dnn_simulator|Deep Learning controller for Udacity Simulator, with trainer|
|dnn_steering_node|Deep Learning steering controller, also contains trainer and data logger|
|esc_vel_pub|Estimates velocity from controller command (sensorless)|
|heartbeat_broadcaster|Publishes alive msgs to microcontroller|
|path_trackers|Pure Pursuit and Stanley steering controllers|
|rosbag_resampler|Script for resampling a rosbag that has topics publishing at different sample rates|
|rplidar_pwm_ros|Modified RPlidar ROS node with PWM motor control (https://github.com/davidbsp/rplidar_ros)
|waypoint_logger|ROS node for recording a new path

#### Also used:
| Name | Link |
| ------ | ------ |
|ROS Kinetic|https://www.ros.org/|
|Hector SLAM| [http://wiki.ros.org/hector_slam](http://wiki.ros.org/hector_slam) |
|Joy|[http://wiki.ros.org/joy](http://wiki.ros.org/joy)|
|ROS Serial|[http://wiki.ros.org/rosserial](http://wiki.ros.org/rosserial)|
|Udacity Self-Driving Car Simulator (Term 1, v2)|https://github.com/udacity/self-driving-car-sim|

A modified version of Hector SLAM is attached as a zip.
