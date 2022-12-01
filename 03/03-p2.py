report = []

with open("input.txt") as input:
    for i in input:
        report.append(i.strip())
def oxyRate(nbr, pos):
    tpstr = ""
    itr_pos = ""
    extract = []
    for i in range(len(nbr)):
        tpstr += nbr[i][pos]
    if tpstr.count('1')>=len(nbr)/2:
        itr_pos = "1"
    else:
        itr_pos = "0"
    for i in range(len(nbr)):
        if nbr[i][pos] == itr_pos:
            extract.append(nbr[i])
    if len(extract) == 1:
        print(int(extract[0],2))
    else:
        oxyRate(extract, pos+1)

def CORate(nbr, pos):
    tpstr = ""
    itr_pos = ""
    extract = []
    for i in range(len(nbr)):
        tpstr += nbr[i][pos]
    if tpstr.count('0')<=len(nbr)/2:
        itr_pos = "0"
    else:
        itr_pos = "1"
    for i in range(len(nbr)):
        if nbr[i][pos] == itr_pos:
            extract.append(nbr[i])
    if len(extract) == 1:
        print(int(extract[0],2))
    else:
        CORate(extract, pos+1)

oxyRate(report, 0)
CORate(report, 0)

    
