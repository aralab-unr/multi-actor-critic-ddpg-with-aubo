# multi-actor-critic-ddpg-with-aubo


## How to run NIPS2017-LearningToRun from https://github.com/megvii-research/NIPS2017-LearningToRunACE
```
conda create -n opensim-rl -c kidzik -c conda-forge opensim python=3.6.1
conda activate opensim-rl
pip install osim-rl
pip install Pyro4
pip install tensorflow_gpu==1.13.1
pip install keras==2.2.4
pip install runenv==1.0.1 
cd workspace/NIPS2017-LearningToRunACE/baseline
python farm.py
python test.py -a=10 -c=5 -t=200 -p logs
```


## Prerequisites for this github
- Ubuntu 16.04 with ROS Kinetic (preferred) OR Ubuntu 18.04 with ros Melodic 

- Install ros kinetic from source - did not work
```
sudo apt-get install python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential
sudo rosdep init
rosdep update
cd ..
mkdir ~/ros_catkin_ws
cd ~/ros_catkin_ws
pip install -U rosdep rosinstall_generator wstool rosinstall
rosinstall_generator desktop_full --rosdistro kinetic --deps --wet-only --tar > kinetic-desktop-full-wet.rosinstall
pip install pyyaml==5.4.1
wstool init -j8 src kinetic-desktop-full-wet.rosinstall 
pip install cmake
sudo apt-get install cmake
pip install empy
rosdep install --from-paths src --ignore-src --rosdistro kinetic -y
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release 
```

- Install ros melodic - if installation from source did not work for kinetic
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo dpkg --configure -a
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```

- Other requirements (Ubuntu 18.04)
```
conda create -n opensim-rl -c kidzik -c conda-forge opensim python=3.6.1
conda activate opensim-rl
pip install osim-rl
pip install Pyro4
pip install tensorflow_gpu==1.13.1
pip install keras==2.2.4
pip install runenv==1.0.1 
pip install gym==0.15.6
pip install scipy tqdm joblib cloudpickle click opencv-python
sudo apt install libpython3.6-dev
sudo apt install libopenmpi-dev
pip install mpi4py
```

- Install ros kinetic (Ubuntu 16.04)
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
source /opt/ros/kinetic/setup.bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
sudo apt install ros-kinetic-moveit
sudo apt-get install ros-kinetic-moveit-visual-tools
sudo apt-get install ros-kinetic-industrial-msgs
sudo apt-get install ros-kinetic-industrial-utils
sudo apt install python3-pip
pip3 install -U catkin_tools
pip3 install click
conda install Pillow

```

- Must have compiled the aubo robot github repo under the kinetic branch,which can be found here:
  - It is safe to remove auto_controller/aubo_demo folder in src if you get build error with this package
```
https://github.com/adarshsehgal/aubo_robot/tree/kinetic
```
- To avoid libmoveit_robot_trajectory.so error, follow below commands
  - replace the version number of 0.9.18 with what you have in below directory
  - don’t change 0.9.15 
```
cd /opt/ros/kinetic/lib 
sudo cp -r libmoveit_robot_trajectory.so.0.9.18 .. 
sudo cp -r libmoveit_robot_state.so.0.9.18 ..
sudo cp -r libmoveit_robot_model.so.0.9.18 ..
cd .. 
sudo mv libmoveit_robot_state.so.0.9.18 libmoveit_robot_state.so.0.9.15 
sudo mv libmoveit_robot_model.so.0.9.18 libmoveit_robot_model.so.0.9.15
sudo mv libmoveit_robot_trajectory.so.0.9.18 libmoveit_robot_trajectory.so.0.9.15
sudo cp -r libmoveit_robot_state.so.0.9.15 lib/ 
sudo cp -r libmoveit_robot_model.so.0.9.15 lib/ 
sudo cp -r libmoveit_robot_trajectory.so.0.9.15 lib/
```
- Fix python error
```
Error processing line 1 of /home/adarshsehgal/.local/lib/python3.5/site-packages/distutils-precedence.pth:

  Traceback (most recent call last):
    File "/usr/lib/python3.5/site.py", line 173, in addpackage
      exec(line)
    File "<string>", line 1, in <module>
    File "/home/adarshsehgal/.local/lib/python3.5/site-packages/_distutils_hack/__init__.py", line 194
      f'spec_for_{name}',
                       ^
  SyntaxError: invalid syntax

Remainder of file ignored
Traceback (most recent call last):
  File "/home/adarshsehgal/.local/bin/catkin", line 7, in <module>
    from catkin_tools.commands.catkin import main
  File "/home/adarshsehgal/.local/lib/python3.5/site-packages/catkin_tools/commands/catkin.py", line 21, in <module>
    import pkg_resources
  File "/home/adarshsehgal/.local/lib/python3.5/site-packages/pkg_resources/__init__.py", line 124
    f"{v} is an invalid version and will not be supported in "
                                                             ^
SyntaxError: invalid syntax
```
solution
```
sudo gedit /home/adarshsehgal/.local/lib/python3.5/site-packages/_distutils_hack/__init__.py
change f'spec_for_{name}' to 'spec_for_'+name

sudo gedit /home/adarshsehgal/.local/lib/python3.5/site-packages/pkg_resources/__init__.py
change f"{v} is an invalid version and will not be supported in " to v+" is an invalid version and will not be supported in "
```

- Create catkin workspace (run all commands within conda environment)
```
conda create -n opensim-rl -c kidzik -c conda-forge opensim python=3.6.1
conda activate opensim-rl
sudo apt install gfortran libblas-dev liblapack-dev libatlas-dev
pip3 install rospkg
pip install pyassimp
pip3 install rotations
pip install matplotlib
pip install seaborn
pip install glob2
pip3 install -U 'mujoco-py<2.2,>=2.1'
sudo apt-get install patchelf
pip3 install torch==1.1.0 # torch-1.1.0
source /opt/ros/kinetic/setup.bash
mkdir -p ~/catkin_workspace/src
cd ~/catkin_workspace/
catkin build
cd src
git clone https://github.com/adarshsehgal/aubo_robot.git
cd aubo_robot
git checkout kinetic
cd ~/catkin_workspace/
catkin build # follow solution above for moveit error
export ROS_PACKAGE_PATH=/home/adarshsehgal/catkin_workspace/src:/opt/ros/kinetic/share:/opt/ros/kinetic/share/ros:$ROS_PACKAGE_PATH
```

- Install conda and create environment
```
conda create -n opensim-rl -c kidzik -c conda-forge opensim python=3.6.1
```
- Python 2.7
- Python verison >= 3.5 (this code was run on python 3.6.1)
- Aubo gym environment uses python2.7 with moveit
- Genetic Algorithm ga.py uses python3.7
- pip install gym==0.15.6
- Install the packages needed to install gym
```
sudo apt-get install python-scipy
pip install scipy
pip3 install scipy tqdm joblib cloudpickle click opencv-python
```
- pip3 install tensorflow_gpu==1.14.0
- openai_ros
  - IMPORTANT: run rosdep install openai_ros EACH time you run the code (for each terminal)
```
cd ~/catkin_workspace/src
git clone https://github.com/adarshsehgal/openai_ros
git clone https://bitbucket.org/theconstructcore/theconstruct_msgs/src/master/
cd openai_ros
git checkout kinetic_devel
cd ..
catkin build
rosdep update --include-eol-distros
source devel/setup.bash
rosdep install --from-paths src --ignore-src -y --rosdistro=kinetic
rosdep install openai_ros
```
- update pip3 to 21.0 or latest (if no errors)
```
pip3 install --upgrade pip
```

- To avoid error with installation of mpi4py package
```
sudo apt install libpython3.7-dev
pip3 install mpi4py
sudo apt-get install -y python3-mpi4py
sudo apt-get install --reinstall openmpi-bin libopenmpi-dev
```

- Upgrading version of MPI to 1.10.7 (Fixes errors with MPI when running train.py with GPU)
```
Download .rpm file from https://www.open-mpi.org/software/ompi/v1.10/
Extract files to $HOME directory
cd 
mkdir openmpi-1.10.7 # new empty folder
cd openmpi-1.10.7/ # extracted folder
mkdir build
cd build
../configure --prefix=/home/adarshsehgal/openmpi1.10.7/
make all install
sudo gedit ~/.bashrc
Add 'export PATH=/home/adarshsehgal/openmpi1.10.7/bin:$PATH'
Add 'export LD_LIBRARY_PATH=/home/adarshsehgal/openmpi1.10.7/lib:$LD_LIBRARY_PATH:'
source ~/.bashrc
```

Open MPI v4.1.4
```
Download .rpm file from https://www.open-mpi.org/software/ompi/v4.1/
Extract files to $HOME directory
cd 
mkdir openmpi4.1.4 # new empty folder
cd openmpi-4.1.4/ # extracted folder
mkdir build
cd build
../configure --prefix=/home/adarshsehgal/openmpi4.1.4/
make all install
sudo gedit ~/.bashrc
Add 'export PATH=/home/adarshsehgal/openmpi4.1.4/bin:$PATH'
Add 'export LD_LIBRARY_PATH=/home/adarshsehgal/openmpi4.1.4/lib:$LD_LIBRARY_PATH:'
source ~/.bashrc
```

Open MPI v3.0.6
```
Download .rpm file from https://www.open-mpi.org/software/ompi/v3.0/
Extract files to $HOME directory
cd 
mkdir openmpi3.0.6 # new empty folder
cd openmpi-3.0.6/ # extracted folder
mkdir build
cd build
../configure --prefix=/home/adarshsehgal/openmpi3.0.6/
make all install
sudo gedit ~/.bashrc
Add 'export PATH=/home/adarshsehgal/openmpi3.0.6/bin:$PATH'
Add 'export LD_LIBRARY_PATH=/home/adarshsehgal/openmpi3.0.6/lib:$LD_LIBRARY_PATH:'
source ~/.bashrc
mpirun -np 2 --bind-to core /home/adarshsehgal/anaconda3/envs/opensim-rl/bin/python3 train.py
```

- No need to install mujoco-py, since the code uses Rviz
- GPU packages installation (Ubuntu 16.04) - https://towardsdatascience.com/deep-learning-gpu-installation-on-ubuntu-18-4-9b12230a1d31
  - Make sure graphic card driver AND Cuda is installed
  - Use the link to find all the steps
  - Other link: https://medium.com/@kapilvarshney/how-to-setup-ubuntu-16-04-with-cuda-gpu-and-other-requirements-for-deep-learning-f547db75f227
  - Cuda download link: https://developer.nvidia.com/cuda-80-ga2-download-archive
  - cuda v10.0
  - cuDNN v7.6.5
```
pip3 install xgboost
sudo apt-get install python3-apt
```

## How to run the DDPG+HER training


**Before running roslaunch command, setup aubo robot repository with ros kinetic (link in pre requite section)**
```
conda activate opensim-rl
cd catkin_workspace
catkin build
rosdep update --include-eol-distros
source devel/setup.bash
rosdep install openai_ros
```
**Training**

First clone the repository
```
git clone <github url> 
```
Training without simulation first, allows for the use of multiple CPU cores. 
To begin training using default values from openai (make sure to comment out lines with sys.exit() in train.py inorder for the python file to work as intended): 
```
cd ~/workspace/multi-actor-critic-ddpg-with-aubo
python3 train.py
```
The best policy will be generated in the directory `/tmp/newlog` (OR the log directory you specify).

To begin training (command-line arguments can be passed to run train.py on specific parameter values)
```
python3 train.py --polyak_value=0.924 --gamma_value=0.949 --q_learning=0.001 --pi_learning=0.001 --random_epsilon=0.584 --noise_epsilon=0.232
```
**Launch rviz and moveit by either launch commands:** 

**For simulation:**
```
roslaunch aubo_i5_moveit_config demo.launch
```
For real robot:
```
roslaunch aubo_i5_robot_config moveit_planning_execution.launch robot_ip:=<your robot ip>
```

To run the connection between the robot gym environment and moveit run:
```
python2.7 moveit_motion_control.py
```
To make the program run faster, you can comment rviz below code in aubo robot repository:
```
cd ~/catkin_workspace/src/aubo_robot/aubo_i5_moveit_config/launch
gedit demo.launch (or just manually open demo.launch in any text editory)

 <!--<include file="$(find aubo_i5_moveit_config)/launch/moveit_rviz.launch">
    <arg name="config" value="true"/>
    <arg name="debug" value="$(arg debug)"/>
  </include> -->
```

## Gym Environments available for GA-DRL execution (can be changed in train.py):
- AuboReach-v0 - executes joint states with moveit
- AuboReach-v1 - only calculates actions but does not execute joint states (increased learning speed)
- AuboReach-v2 - only calculates actions but does not execute joint states (increased learning speed), reward fixes to converge the learning curve
- AuboReach-v3 - only calculates actions but does not execute joint states (increased learning speed), reward fixes to converge the learning curve, only 4 Aubo joints in action
- AuboReach-v4 - executes joint states with moveit, only run with first 4 joint states
- AuboReach-v5 - executes joint states with moveit, only run with first 4 joint states, runs training and testing with random initial and target joint states, CPU = 1, denser rewards
- AuboReach-v6 - executes joint states with moveit on robot (simulation/real), only run with first 4 joint states, runs training and testing with random initial and target joint states, CPU = 1, denser rewards
- FetchReacher-v1 - Door opening environment from the paper. Files used are fetch.py, reach.py, robot_env.py and aubo_i5.xml (this file has the configuration for DoorOpening env).



## How to train the environment manually
```
python3 -m train --env=AuboReach-v2 --logdir=/tmp/openaiGA --n_epochs=70 --num_cpu=6 --polyak_value=0.184 --gamma_value=0.88 --q_learning=0.001 --pi_learning=0.001 --random_epsilon=0.055 --noise_epsilon=0.774
```
Values of all the above parameters can differ. These parameters are generated by GA-DRL algorithm, as mentioned in the paper, reference of which is mentioned in the start of this readme.

## How to play the environment with any chosen policy file
You can see the environment in action by providing the policy file:
```
python3 play.py <file_path>
python3 play.py /tmp/openaiGA/policy_best.pkl
```
where file_path = /tmp/openaiGA/policy_best.pkl in our case.

## How to train the environment on Multi-Actor/Critic + HER setup

- New Configurations for ddpg_multi-actor-critic
  - 'rl_algo' in config.py file 
  - 'network_class' in config.py file
  - 'number_actors_main' in train.py
  - 'number_critics_main' in train.py
  - 'number_actors_target' in train.py
  - 'number_critics_target' in train.py
  - 'number_critics_target' in train.py # used to decide which measure of central tendency to be used (only mean implemented)

- New files for ddpg_multi-actor-critic
  - ddpg_multi_actor_critic.py
  - multi_actor_critic.py

- Some parameter values:
  - Episodes = 100
  - Cycles = 50

- Average is taken for both actor and critic
  - network weights are averaged to single actor/critic

- Each actor does not reuse (My solution has reuse false for all actors)
- critic network has reuse = true (My solution has reuse false for all critics) # reverted
- How to maintain network name after taking average of networks
- Q_grads_tf and pi_grads_tf network names in ddpg_multi_actor_critic.py?

## How to compare DDPG+HER with Multi Actor/Critic with HER (called AACHER algorithm)
- Run 20 times, and take average (20 independent trails)
- Average Q values over epochs 
  - also show scatter of values as background shadow
- Cumulative rewards over epochs
  - also show scatter of values as background shadow
- Average rewards over epochs
  - also show scatter of values as background shadow
- Average training loss over epochs
  - also show scatter of values as background shadow
- Try Loss as mean, median, mode etc from all networks in both actors and critics
- Try different number of actors/critics in main/target networks
- Try with GPU
- Try with 6 points for Aubo env
- Try to change n_cycles, n_batches, n_episodes, n_epochs
- Try with Aubo env-6, where robot actually moves to learn the task
- Try on door opening environment
- Try other openai baselines envs to run the code
- Changed n_cycles from 50 to 15
- Changed n_batches from 40 to 15
- Changed num_cpu from 4 to 2
- Try with different number of hidden layers (Currently set to 3)
- Try to plot loss per epoch

## Experiments performed with AACHER
- Increasing number of critics is increasing the performance (Number of actors is set to 1)
  - Tested with A1C3, A1C5, A1C7
  - A1C7 has the highest performance

## how to run the AACHER algorithm with different settings
- Use 'test_script_multi_actor_critic.py'
- Use this file to write any test cases
- Use plot files to compare various test cases in one plot

## How to plot results:
For one set of parameter values and for one DRL run, plot results using:
```
python3 plot.py <dir>
python3 plot.py /tmp/openaiGA
```
where, dir = /tmp/openaiGA in our case, as mentioned in ga.py file. You can provide any log directory.
- If you are testing one set of parameters, in train.py, comment out the code which stops the system as soon as it reaches threshold success rate. 
```
sys.exit()
```

To plot test_success_rate, test_reward and test_mean_Q for various settings
```
python plot-all-comparison.py <dir>
python plot.py /home/adarshsehgal/AACHER_logs
```
where, dir = /home/adarshsehgal/AACHER_logs in our case

## Aubo environment setup details:
**NOTE**: Some experiments are using less than 6 joints for learning. Please refer to environments section for details.

**Action**: Each action is a set of 4 joint states of Aubo i5 robot (not using two wrist joints)

**Action space**: Each joint state can take joint values between -1.7 and 1.7

**Goal**: Random reachable point (a set of 6 joint states), [-0.503, 0.605, -1.676, 1.391]

**Initial State**: [0, 0, 0, 0] (Some setups take random state)

**Reset state**: [0, 0, 0, 0] (Some setups take random state)

**Reward**: Computed as absolute distance between corresponding joint states

**Success**: A joint state is considered success if distance between the joint states is less than 0.1

**Step**: 1. Take an action governing by DRL algorithm 2. compute reward 3. decide if it is success or not

## How to run PPO, A2C and DDPG:

```
pip install stable-baselines3
```
