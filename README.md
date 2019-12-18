# Lidar Assisted Teleoperated Driving (LATD)

A lidar (Light Detection and Ranging) device is a laser sensor that can collect distances to objects in a 2D plane at a high rate. Traditionally, these devices have been used in autonomous robots to sense the environment and avoid obstacles. Our team was interested in exploring how these devices can help humans driving robots. We used a SICK lidar to map out the terrain in front of the robot in real time.  Then, we used this 2D map to drive the robot and avoid obstacles. A laptop keyboard is the controller to drive the robot. Data from the Lidar is streamed over network and plotted in Rviz in real time.

## Project Overview

This project was designed with 4 stages. This package has functionality up until Stage 3 (experimental).

![Image of LATD STAGES](https://github.com/freiremelgiz/ME439_latd/blob/master/resources/Stages.PNG)


## Project Features
### ROS Distributed Systems Features

To enable ROS Distributed Systems Features, set your environment variables as shown in the image below.

![Image of ROS DIST SYS](https://github.com/freiremelgiz/ME439_latd/blob/master/resources/ROSDistSys.PNG)


On a ROS environment, set these variables with:
```
export ROS_MASTER_URI=http://10.141.149.10:11311
export ROS_IP=10.141.32.234
```


### SICK lidar driver (tim_5xx)

The ROS package sick_tim developed by SICK AG has no PCL dependencies and can be run on Debian (Raspberry Pi)
https://github.com/uos/sick_tim


### Installing

Clone this repository with:
```
git clone https://github.com/freiremelgiz/ME439_latd
```
# Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Victor Freire**   - <freiremelgiz@wisc.edu>
* **Rebecca Roembke** - <rroembke@wisc.edu>
* **Wanyue Xu**       - <wxu97@wisc.edu>


## Acknowledgments

* Josh Tabor
* Professor Peter Adamczyk
