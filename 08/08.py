entries = []
temp = []
count = 0
with open("input.txt") as input:
	for i in input:
		temp.append(i.split(" | ")[1].strip())
for i in temp:
	entries.append(i.strip().split())

for i in entries:
	for j in i:
		if len(j) in (2,3,4,7):
			count+=1
print(count)