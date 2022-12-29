import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-bright')

def Game():
    car_door = random.randint(1,3)
    player_door = random.randint(1,3)

    # We are testing each door to see if it can be revealed by the host 
    door_revealed = 1
    while (car_door == door_revealed or player_door == door_revealed):
        door_revealed += 1
    
    # Then we switch
    new_choice_door = list(set(range(1, 4)) - set([player_door, door_revealed]))[0]

    if new_choice_door == car_door:
        return 1
    else:
        return 0

current_try = 1
nb_win = 0
win_pc = list()

while current_try <= 1000:
    nb_win += Game()
    win_pc.append(nb_win/current_try)
    current_try +=1

plt.plot(range(1000), win_pc)
plt.show()
