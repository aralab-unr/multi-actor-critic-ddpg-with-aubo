import os

# A1C3
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C3 '
          '--number_actors_main=1 '
          '--number_critics_main=3 '
          '--number_actors_target=1 '
          '--number_critics_target=3 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A1C5
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C5 '
          '--number_actors_main=1 '
          '--number_critics_main=5 '
          '--number_actors_target=1 '
          '--number_critics_target=5 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A1C7
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C7 '
          '--number_actors_main=1 '
          '--number_critics_main=7 '
          '--number_actors_target=1 '
          '--number_critics_target=7 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A1C8
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C8 '
          '--number_actors_main=1 '
          '--number_critics_main=8 '
          '--number_actors_target=1 '
          '--number_critics_target=8 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A1C10
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C10 '
          '--number_actors_main=1 '
          '--number_critics_main=10 '
          '--number_actors_target=1 '
          '--number_critics_target=10 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A3C3
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A3C3 '
          '--number_actors_main=3 '
          '--number_critics_main=3 '
          '--number_actors_target=3 '
          '--number_critics_target=3 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A3C5
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A3C5 '
          '--number_actors_main=3 '
          '--number_critics_main=5 '
          '--number_actors_target=3 '
          '--number_critics_target=5 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A5C7
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A5C7 '
          '--number_actors_main=5 '
          '--number_critics_main=7 '
          '--number_actors_target=5 '
          '--number_critics_target=7 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A7C7
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A5C7 '
          '--number_actors_main=7 '
          '--number_critics_main=7 '
          '--number_actors_target=7 '
          '--number_critics_target=7 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A8C8
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C8 '
          '--number_actors_main=8 '
          '--number_critics_main=8 '
          '--number_actors_target=8 '
          '--number_critics_target=8 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A7C10
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A7C10 '
          '--number_actors_main=7 '
          '--number_critics_main=10 '
          '--number_actors_target=7 '
          '--number_critics_target=10 '
          '--num_cpu=2 '
          '--n_epochs=20')

# A10C10
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/A1C8 '
          '--number_actors_main=10 '
          '--number_critics_main=10 '
          '--number_actors_target=10 '
          '--number_critics_target=10 '
          '--num_cpu=2 '
          '--n_epochs=20')
