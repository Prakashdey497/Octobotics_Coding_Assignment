# Octobotics_Coding_Assignment

## Instructions



### Dependencies

- [`pygame`](https://pypi.org/project/pygame/)

```bash
pip install pygame
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

copy src folder from clone directory paste it on your_workspace

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
- Run the inverted pendulum simulation
```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
```
- Set the initial parameter
```bash
rosservice call /inverted_pendulum/set_params "{pendulum_mass: 2.0, pendulum_length: 300.0, cart_mass: 0.5, theta_0: 3.14, theta_dot_0: 0.0,theta_dot_dot_0: 0.0, cart_x_0: 0.0, cart_x_dot_0: 0.0, cart_x_dot_dot_0: 0.0}"
```

### Goal 2: Send sinusoidal force input to the cart
Step1.
```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
```

Step2.
```bash
rosservice call /inverted_pendulum/set_params "{pendulum_mass: 2.0, pendulum_length: 300.0, cart_mass: 0.5, theta_0: 3.14, theta_dot_0: 0.0,theta_dot_dot_0: 0.0, cart_x_0: 0.0, cart_x_dot_0: 0.0, cart_x_dot_dot_0: 0.0}"
```

Step3.
```bash
rosrun inverted_pendulum_controller sinosodial_force_publisher.py
```

- Plot the applyed force on the rqt_plot
```bash
rqt_plot
```

### Goal3: Balance the inverted pendulum Using PID

 Step1. 
 ```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
 ```
Step2.
```bash
roslaunch inverted_pendulum_controller controller.launch
```
Step3:
```bash
rosservice call /inverted_pendulum/set_params "{pendulum_mass: 2.0, pendulum_length: 300.0, cart_mass: 0.5, theta_0: 3.14, theta_dot_0: 0.0,theta_dot_dot_0: 0.0, cart_x_0: 0.0, cart_x_dot_0: 0.0, cart_x_dot_dot_0: 0.0}"
```


