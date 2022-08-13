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

Install ros kinetic
```
sudo apt-get install python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential
sudo rosdep init
rosdep update
cd ..
mkdir ~/ros_catkin_ws
cd ~/ros_catkin_ws
rosinstall_generator desktop_full --rosdistro kinetic --deps --wet-only --tar > kinetic-desktop-full-wet.rosinstall
wstool init -j8 src kinetic-desktop-full-wet.rosinstall 
rosdep install --from-paths src --ignore-src --rosdistro kinetic -y
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release 
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
