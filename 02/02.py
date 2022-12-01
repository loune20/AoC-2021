course = []
forward = 0
depth = 0
aim = 0
with open("input.txt") as input:
    for i in input:
        course.append(i.strip())
for i in course:
    if "forward" in i:
        forward += int(i[-1:])
        depth += aim*int(i[-1:])
    elif "up" in i:
        aim -= int(i[-1:])
    elif "down" in i:
        aim += int(i[-1:])            
print(forward*depth)