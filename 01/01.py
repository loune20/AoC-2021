report = []
mes = []
incr = 0
with open("input.txt") as input:
    for i in input:
        report.append(int(i.strip()))
for j in range(len(report)-2):
    mes.append(report[j] + report[j+1] + report[j+2])
for i in range(1,len(mes)):
    if mes[i]>mes[i-1]:
        incr += 1
print(incr)