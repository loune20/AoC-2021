with open("input2.txt") as input:
	fish = input.readline().strip().split(",")
for i in range(len(fish)):fish[i] = int(fish[i])

def simDay():
	for i in range(len(fish)):
		if fish[i] == 0:
			fish.append(8)
			fish[i] = 6
		else:
			fish[i] = fish[i]-1

def simDay2(fishes):
	for i in range(len(fish)):
		if fishes[i] == 0:
			fishes.append(8)
			fishes[i] = 6
		else:
			fishes[i] = fishes[i]-1
	return(fishes)

"""for i in range(18): #5 = gives results after 5 days
	simDay()
print(len(fish))
"""
fishes = fish
for i in range(80):
	fishes = simDay2(fishes)
print(len(fishes))
# peut pas run avec 256 : pb de perf pour 2ème étoile