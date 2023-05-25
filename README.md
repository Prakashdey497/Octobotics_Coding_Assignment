# Octobotics_Coding_Assignment

## Instructions



### Dependencies

- [`pygame`](https://pypi.org/project/pygame/)
- [`rqt_plot`](http://wiki.ros.org/rqt_plot)

```bash
pip install pygame
rosdep install rqt_plot
```

### Usage
- Create a workspace

```bash
mkdir -p ~/catkin_ws
```

- clone the repository

```bash
git clone https://github.com/Prakashdey497/Octobotics_Coding_Assignment.git
```

Copy the src folder from the cloned repository and paste it into your workspace. The folder structure should look like this:

**Folder structure Look like**:

```
catkin_ws/
        src/
            inverted_pendulum_controller/
            inverted_pendulum_sim/
```

- build the project

```bash
cd ~/catkin_ws/
catkin_make
```

- source the workspace

```bash
source devel/setup.bash
```

## Assignment Task:

### Goal1: Run the inverted pendulum sim using the initial parameters
Step 1:Launch the inverted pendulum simulation:
```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
```
Step 2: Set the initial parameters:
```bash
rosservice call /inverted_pendulum/set_params "{pendulum_mass: 2.0, pendulum_length: 300.0, cart_mass: 0.5, theta_0: 1.14, theta_dot_0: 0.0,theta_dot_dot_0: 0.0, cart_x_0: 0.0, cart_x_dot_0: 0.0, cart_x_dot_dot_0: 0.0}"
```

### Goal 2: Send sinusoidal force input to the cart

Step 1: Launch the inverted pendulum simulation:
```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
```

Step 2: Set the initial parameters:
```bash
rosservice call /inverted_pendulum/set_params "{pendulum_mass: 2.0, pendulum_length: 300.0, cart_mass: 0.5, theta_0: 1.14, theta_dot_0: 0.0,theta_dot_dot_0: 0.0, cart_x_0: 0.0, cart_x_dot_0: 0.0, cart_x_dot_dot_0: 0.0}"
```

Step 3: Run the sinusoidal force publisher:
```bash
rosrun inverted_pendulum_controller sinosodial_force_publisher.py
```

- Plot the applied control input using **rqt_plot**.

- [`Recorded video`](/data/sinosodial_input.webm) of changing frequencies and amplitudes of oscillations.

### Goal3: Balance the inverted pendulum Using PID


Step 1: Launch the inverted pendulum simulation:

 ```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
 ```
Step 2: Launch the controller:

```bash
roslaunch inverted_pendulum_controller controller.launch
```
Step 3: Set the initial parameters:


```bash
rosservice call /inverted_pendulum/set_params "{pendulum_mass: 2.0, pendulum_length: 300.0, cart_mass: 0.5, theta_0: 3.14, theta_dot_0: 0.0,theta_dot_dot_0: 0.0, cart_x_0: 0.0, cart_x_dot_0: 0.0, cart_x_dot_dot_0: 0.0}"
```

- [`Recorded video`](/data/pid.webm) After applied PID.


