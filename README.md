# The ARM

## Controlling a (10 DOF) robotic arm with hand via [OpenPose translated](https://github.com/m4n0b0dy/Arm-server) commands

## Project ToDos
- [x] Robot Arm Physically Built (with custom right hand)
- [x] Robot Arm Progammable via Pi and PCA9685 Library
- [x] Dockerfile for launching Flask API, receiving instructions, and controlling hand via PCA9685

## Project Tools
- Python
  - Flask
  - PCA9685
- Docker base images
  - Ubuntu 18.04

## The Video
- [Video Published Here](https://www.reddit.com/r/robotics/comments/jvvtqn/real_time_robot_armhand_control_with_human/)

## Installation and Running
### (on Raspberry Pi with PCA9685 board and LewanSoul Robot Arm)
```sh
git clone git@github.com:m4n0b0dy/Arm-robot.git
docker build --tag arm:latest .
docker run --device /dev/i2c-1 --network="host" --name arm -d arm:latest
```
### Docker container "arm" is now running the Flask API on port 5005
### To call the API, simply post a request to the Arm server hostname

## Parts List
- Raspberry Pi 3 or 4
- [LewanSoul Arm](https://www.banggood.com/LOBOT-6DOF-Metal-RC-Robot-Arm-Programmable-MP3-Music-With-Digital-Servo-p-1410198.html?rmmds=myorder&cur_warehouse=CN)
- [LewanSoul Right Hand](https://www.banggood.com/LOBOT-uHand2_0-DIY-RC-Robot-Arm-Independent-Fingers-With-LFD-01-Anti0-block-Servos-p-1527085.html?rmmds=myorder&cur_warehouse=CN)
- [PCA9685 Controller](https://www.amazon.com/gp/product/B07WS5XY63/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [Jumper Wiring](https://www.amazon.com/gp/product/B081CBSDHV/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [Servo Extension Wiring](https://www.amazon.com/gp/product/B01HLUZO4S/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
