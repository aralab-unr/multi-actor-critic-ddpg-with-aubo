import os

# A1C3
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A1C3 '
          '--number_actors_main=1 '
          '--number_critics_main=3 '
          '--number_actors_target=1 '
          '--number_critics_target=3 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A1C5
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A1C5 '
          '--number_actors_main=1 '
          '--number_critics_main=5 '
          '--number_actors_target=1 '
          '--number_critics_target=5 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A1C7
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A1C7 '
          '--number_actors_main=1 '
          '--number_critics_main=7 '
          '--number_actors_target=1 '
          '--number_critics_target=7 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A1C10
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A1C10 '
          '--number_actors_main=1 '
          '--number_critics_main=10 '
          '--number_actors_target=1 '
          '--number_critics_target=10 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A3C3
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A3C3 '
          '--number_actors_main=3 '
          '--number_critics_main=3 '
          '--number_actors_target=3 '
          '--number_critics_target=3 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A3C5
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A3C5 '
          '--number_actors_main=3 '
          '--number_critics_main=5 '
          '--number_actors_target=3 '
          '--number_critics_target=5 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A5C7
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A5C7 '
          '--number_actors_main=5 '
          '--number_critics_main=7 '
          '--number_actors_target=5 '
          '--number_critics_target=7 '
          '--num_cpu=4 '
          '--n_epochs=20')

# A7C10
os.system('python3 -m train '
          '--logdir=/home/adarshsehgal/AACHER_logs/multi-ac-logs-A7C10 '
          '--number_actors_main=7 '
          '--number_critics_main=10 '
          '--number_actors_target=7 '
          '--number_critics_target=10 '
          '--num_cpu=4 '
          '--n_epochs=20')