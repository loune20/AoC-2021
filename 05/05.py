# Following : https://aoc.just2good.co.uk/2021/5
import re
import numpy as np
from dataclasses import dataclass

@dataclass
class Line:
	x1:int
	y1:int
	x2:int
	y2:int

	@property
	def is_orthogonal(self):
		return(self.x1==self.x2 or self.y1 == self.y2)
	@property
	def diagonal_down(self):
		assert not self.is_orthogonal, "Must no be orthogonal"
		return(self.x1-self.x2 == self.y1-self.y2)
	@property
	def min_x(self):
		return(min(self.x1, self.x2))
	@property
	def min_y(self):
		return(min(self.y1, self.y2))
	@property
	def max_x(self):
		return(max(self.x1, self.x2))
	@property
	def max_y(self):
		return(max(self.y1, self.y2))

# Parsing input
vents = []
with open("input.txt") as input:
	for i in input:
		x1, y1, x2, y2 = map(int, re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", i)[0])
		vents.append(Line(x1, y1, x2, y2))

# Main
max_x = max([l.max_x for l in vents])
max_y = max([l.max_y for l in vents])

field = np.zeros(shape=(max_y+1, max_x+1), dtype=np.int8)

for line in vents:
	if line.is_orthogonal:
		field[line.min_y:line.max_y+1, line.min_x:line.max_x+1] += 1
danger_vent = (field>=2).sum()
print(f"Part 1 : {danger_vent}")

# Part 2
for line in vents:
	if not line.is_orthogonal:
		for i in range(line.max_y-line.min_y+1):
			if line.diagonal_down:
				field[line.min_y+i, line.min_x+i] += 1
			else:
				field[line.max_y-i, line.min_x+i] += 1

danger_vent = (field>=2).sum()
print(f"Part 2 : {danger_vent}")