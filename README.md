# robosys_ros
Challenges of robot system studies 2.

We created a node that operates two LEDs with the keyboard.

## movie

## Requirement
This package requires the following to run:
* raspberry pi 3
* Ubuntu  
    Ubuntu 16.04 (Ubuntu 16.04 Server recomended)  
* ROS  
    Kinetic Kame
* led x 2
* resistor x 2
  * 1kΩ
  
## Installation
Input the following commands.

        $ cd ~/catkin_ws/src
        $ git clone https://github.com/iidayuki/robosys_ros.git
        $ cd ~/catkin_ws
        $ catkin_make
        $ cd ~/catkin_ws/src/robosys_ros/myled
        $ chmod +x setup.sh
        $ ./setup.sh
        
## Usage
Input the following commands.

        $ roscore
    
In another terminal

        $ rosrun robosys_ros led_sub.py

In another terminal

        $ rosrun robosys_ros led_pub.py
        
With the input of the following keyboard, the LED can be turned on and off.

        a: The LED on the left turns on and the LED on the right turns off.
        s: Lights the left and right LEDs.
        d: The LED on the left turns off and the LED on the right turns on.
        q: Lights the left and right LEDs.
        
END: Ctr+c + Enter 
        
## Removal
Input the following commands.

        $ cd ~/catkin_ws/src/robosys_ros/myled
        $ chmod +x release.sh
        $ ./release.sh
        
## License
This repository is licensed under the GPLv3 license, see [LICENSE](https://github.com/iidayuki/robosys_ros/blob/master/LICENSE).


        
        
        
