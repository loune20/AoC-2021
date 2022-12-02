temp_boards = []
rnum = [] #random numbers to be marked on temp_boards
boards = [] #list of bingo boards
marks = [] #same but with status (marked/unmarked)
temp_marks = []
w_boards = []

with open("input.txt") as input:
	rnum = [int(i) for i in input.readline().split(",")]
	for i in input:
		if i != "\n":
			temp_boards.append(i.strip())
# Populate boards and marks
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
		victoire=False
		#colonne
		for j in range(5):
			compteur = 0
			for k in range(len(boards[i])):
				if marks[i][k][j] == 1:
					compteur+=1
			if compteur == 5:
				victoire=True
		#ligne (board = i, ligne = l)
		for l in range(len(boards[i])):
			if marks[i][l] == [1, 1, 1, 1, 1]:
				victoire=True
		if victoire:
			if i not in w_boards:
				w_boards.append(i)

def calcBoardScore(board):
	board_score = 0
	for i in range(len(boards[board])):
		for j in range(len(boards[board][i])):
			if marks[board][i][j] == 0:
				board_score += boards[board][i][j]
	return(board_score)


for i in range(len(rnum)):
	markNumber(rnum[i])
	checkIfWin()
	if len(w_boards) == len(boards):
		print("tous les boards ont gagné")
		print("score final", calcBoardScore(w_boards[-1])*rnum[i])
		break