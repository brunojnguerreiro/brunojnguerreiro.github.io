Title: Code
Sort-Order: 2

Software, datasets and templates that I make available, mostly related to drone
control, estimation and simulation. My personal repositories are on
[github.com/brunojnguerreiro](https://github.com/brunojnguerreiro).

**Lab repositories:** most of the code developed in my research group is
published by the Cyber-physical and Aerospace Control (CybAer) Lab at NOVA FCT,
on the institutional GitHub organization
[github.com/cybaer-nova](https://github.com/cybaer-nova).

Below are my code contributions, both in my own repositories and in those of
other institutions, from the most recent to the oldest.

### [crazynova2](https://github.com/cybaer-nova/crazynova2)

*2024 · CybAer lab · Python (ROS 2)*

Flight software for the Crazyflie nano-quadcopters in the NOVA FCT arena, based
on [Crazyswarm2](https://github.com/IMRCLab/crazyswarm2). I added the CybAer
test scripts and logging configuration, deloggers for the on-board micro-SD logs
and ROS bags (MATLAB/Octave and Python), a simple velocity controller
for the Crazyflie, and examples for infinite trajectories and multi-drone
hovering.

<div style="clear:both"></div>

### [crazys-uavs](https://github.com/cybaer-nova/crazys-uavs)

*2024 · CybAer lab · C++ (ROS/Gazebo)*

Simulation environment for the Unmanned Aerial Vehicles course at NOVA FCT,
based on [CrazyS](https://github.com/gsilano/CrazyS), the software-in-the-loop
platform for the Crazyflie 2.0 nano-quadcopter. I added a Gazebo world of the
CybAer flight arena, a hovering example launcher for it and flight logging
with date-stamped log files.

<div style="clear:both"></div>

### [M690B-Wiki](https://github.com/hardtekpt/M690B-Wiki)

<img src="{static}/images/code/m690b-wiki.jpg" alt="M690B drone in outdoor flight" class="float-image-right">

*2023 · CybAer lab · documentation* · [Wiki](https://hardtekpt.github.io/M690B-Wiki/)

Documentation for preparing, testing and conducting indoor and outdoor missions
with the M690B drone: vehicle setup, known issues, mission logs and roadmap. I
contributed the flight mission logs, including those of the in-flight capture
manoeuvres with MPC from the [CAPTURE](http://capture.isr.tecnico.ulisboa.pt/)
project.

<div style="clear:both"></div>

### [dc-motor-control](https://github.com/cybaer-nova/dc-motor-control)

<img src="{static}/images/code/dc-motor-control.jpg" alt="Arduino-based DC motor position control setup with encoder and motor driver" class="float-image-right">

*2023 · CybAer lab · C++ (Arduino)*

Position control of a DC motor with encoder using an Arduino, for the
Introduction to Electrical and Computer Engineering course at NOVA FCT. Students
see for the first time the difference between a well-tuned controller and one
with overshoot. Includes the Arduino code, the circuit and 3-D printable parts.

<div style="clear:both"></div>

### [nova-ieec-m262](https://github.com/brunojnguerreiro/nova-ieec-m262)

<img src="{static}/images/code/nova-ieec-m262.gif" alt="Animation of the simulated drone flying from the start point to the target" class="float-image-right">

*2021 · personal · MATLAB/Octave*

Class repository for module 2.6.2 (Systems, Decision and Control) at NOVA FCT:
a simple drone simulation for tuning the gains of a height controller and
comparing the responses.

<div style="clear:both"></div>

### [nova-drone-arena](https://github.com/brunojnguerreiro/nova-drone-arena)

<img src="{static}/images/code/nova-drone-arena.jpg" alt="Illustration of the NOVA DroneArena netted flight cage with three drones" class="float-image-right">

*2021 · personal, also in the CybAer lab · C++, MATLAB* · [Lab copy](https://github.com/cybaer-nova/drone-arena-marvelmind)

Software for the NOVA-DroneArena, the drone testbed at NOVA School of Science
and Technology, developed by Hugo Cabrita in his MSc thesis. Includes an
installation guide, MATLAB/Simulink controllers, the Marvelmind indoor
positioning configuration and C++ code for testing the drone.

<div style="clear:both"></div>

### [replace-dataset1](https://github.com/brunojnguerreiro/replace-dataset1)

<img src="{static}/images/code/replace-dataset1.png" alt="Sample plots: RGB image, depth point cloud, and inertial trajectory with features" class="float-image-right">

*2021 · personal · MATLAB*

Dataset from the [REPLACE](http://replace.isr.tecnico.ulisboa.pt/) project for
validating simultaneous localization, mapping and moving object tracking
(SLAMMOT) algorithms. Motion-capture ground truth and RGB-D camera data in a
ROS bag, with MATLAB code to parse and plot it.

<div style="clear:both"></div>

### [thesis-template](https://github.com/brunojnguerreiro/thesis-template)

<img src="{static}/images/code/thesis-template.jpg" alt="Autonomous helicopter in flight, a figure from the template" class="float-image-right">

*2017 · personal · TeX*

LaTeX thesis template created from my own PhD thesis, with colours following
the Técnico visual identity.

<div style="clear:both"></div>
