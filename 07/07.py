with open("input.txt") as input:
	crabs = input.readline().strip().split(",")
for i in range(len(crabs)):crabs[i] = int(crabs[i])

def fuelCost(hpos):
	cost = 0
	for i in crabs:
		dist = abs(i-hpos)
		cost_i = dist*(dist+1)//2
		cost+= cost_i
		#cost+=dist pour la 1ère étoile
	return(cost)
maxx = []
for i in range(max(crabs)):
	maxx.append(fuelCost(i))
print(min(maxx))