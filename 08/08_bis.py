entries = []
temp = []
count = 0

# For real input
"""with open("input.txt") as input:
	for i in input:
		temp.append(i.split(" | ")[1].strip())
for i in temp:
	entries.append(i.strip().split())"""

# For example input
with open("input2.txt") as input:
	for i in input:
		if "|" not in i:
			entries.append(i.strip().split())
# All
for i in entries:
	for j in i:
		if len(j) in (2,3,4,7):
			count+=1
print(count)

"""
pour chaque entry
pour chaque output values
si digit a une longueur de 2, 3, 4 ou 7 → compter
0 : 6
**1 : 2**
2 :  5
3 : 5
**4 : 4**
5 : 5
6 : 6
**7 : 3**
**8 : 7**
9 : 6
"""