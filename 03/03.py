report = []
gamma = ""
epsilon = ""
with open("input.txt") as input:
    for i in input:
        report.append(i.strip())

for j in range(len(report[0])):
    tpstr = ""
    for i in range(len(report)):
        tpstr += report[i][j]
    if tpstr.count('0')>len(tpstr)/2:
        gamma+="0"
    else:
        gamma+="1"
for i in gamma:
    if i=="0": epsilon += "1"
    else: epsilon += "0"
print(int(gamma, 2)*int(epsilon, 2))
