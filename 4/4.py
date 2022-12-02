temp_boards = []
rnum = [] #random numbers to be marked on temp_boards
boards = [] #list of bingo boards
marks = [] #same but with status (marked/unmarked)
temp_marks = []

with open("input_2.txt") as input:
	rnum = [int(i) for i in input.readline().split(",")]
	for i in input:
		if i != "\n":
			temp_boards.append(i.strip())

for i in range(0, len(temp_boards), 5):
	boards.append([i.split() for i in temp_boards[i:i+5]])
temp_boards = boards.copy()
boards = []
temp_boards_bis = []
for j in range(len(temp_boards)):
	for i in temp_boards[j]:
		temp_boards_bis.append([int(x) for x in i])
for i in range(0, len(temp_boards_bis), 5):
	boards.append([i for i in temp_boards_bis[i:i+5]])

for i in boards:
	j = 0
	while (j<5): temp_marks.append([0,0,0,0,0]);j+=1

for i in range(0, len(temp_marks), 5):
	marks.append([i for i in temp_marks[i:i+5]])

def markNumber(number):
	for i in range(len(boards)):
		for j in range(len(boards[i])):
			if number in boards[i][j]:
				index = boards[i][j].index(number)
				marks[i][j][index] = 1

def checkIfWin():
	for i in range(len(boards)):
		#verticalement
		for j in range(5):
			compteur = 0
			for k in range(len(boards[i])):
				if marks[i][k][j] == 1:
					compteur+=1
			if compteur == 5:
				print("colonne")
		#horizontalement
		for l in range(len(boards[i])):
			if marks[i][l] == [1, 1, 1, 1, 1]:
				print("ligne", "board:",i+1, "ligne:",l+1)


		

for i in range(13):
	#print(rnum[i])
	markNumber(rnum[i])
checkIfWin()

print("→")
#for i in boards:print(i)
for i in marks:print(i)
print("→")

"""
0-1-2-3-4
5-6-7-8-9
10-11-12-13-14
15-16-17-18-19
20-21-22-23-24

0-5-10-15-20
1-6-etc.
"""

"""
h = 0
		while h<=20:
			print(h)
			if marks[i][h] == marks[i][h+1] == marks[i][h+2] == marks[i][h+3] == marks[i][h+4]:
				print("ligne!")
			else: 
				h+=5
"""