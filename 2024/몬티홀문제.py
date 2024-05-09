import time
import random

def populate_doors(): # put a car behind one door, populate 채우다
	door=['goat', 'goat', 'goat']
	door[random.randint(0,2)]='car'
	return door

wins = 0
losses = 0
time_start = time.time()

# playing the game 100,000 times:
for x in range(100000):
	doors=populate_doors()
	first_choice=random.randint(0,2) # choose a random door
	for y in range(3): # reveal first losing, unchosen door
		if doors[y] != 'car' and y != first_choice:
			doors[y] = 'out'
			break
	if doors[first_choice] == 'car':
		losses = losses + 1 # contestant switched to losing door
	else:
		wins = wins + 1 # contestant switched to winning door
time_finish = time.time()

print("All choices were switched.")
print("Wins: ", wins)
print("Losses: ", losses)
print("Elapsed time: ", time_finish-time_start)

