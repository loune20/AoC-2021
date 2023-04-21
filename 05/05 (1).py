data = []
datap = []
vent = [[]]
print("→")

with open("input2.txt") as input:
	for i in input:
		data.append(i.strip().split(" -> "))
for i in range(len(data)):
	tempp = []
	for j in range(2):
		temp = []
		for d in data[i][j].split(","):temp.append(int((d)))
		tempp.append(temp)
	datap.append(tempp)		
	#if i == 0:break

# Create matrix of appropriate size
for i in range(len(datap)):
	while len(vent) < max(datap[i][0][0], datap[i][1][0])+1: #taille en x
		vent.append([])
	#print("taille X ok, proceed!")
	for j in range(len(vent)):
		while len(vent[j]) < max(datap[i][0][1], datap[i][1][1])+1: #taille en y
			vent[j].append([])
	#print("taille Y ok, proceed")

# Fill matrix
for i in range(len(datap)):
	# fill x
	for j in range(min(datap[i][0][0], datap[i][1][0]), max(datap[i][0][0], datap[i][1][0])+1):
		if vent[datap[i][0][1]-1][j] == []:
			vent[datap[i][0][1]-1][j] = 1
		else:
			vent[datap[i][0][1]-1][j] += 1
	#if i == 0:break
for i in vent:print(i)
