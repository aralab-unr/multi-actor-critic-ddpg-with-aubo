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
Ubuntu 18.04

Install ros kinetic from source - did not work
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

Install ros melodic - if installation from source did not work for kinetic
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

Other requirements
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

How to run training
```
python train.py
```
