# If you already have the data as an input use:
data = [] # Your Advent Calendar Input
# However, it is highly recommended to run this:
location = "" # Path of the input.txt provided from Advent Calendar (Replace '\' → '\\')
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
def day2(part=1):
    cond = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }
    res = 0
    for i in data:
        i = i.split(' ')
        if part == 1: 
            res += list(cond["A"].keys()).index(i[1])+1
            res += cond[i[0]][i[1]]
        elif part == 2:
            outcome = cond["B"][i[1]]
            res += [list(cond["A"].keys()).index(j)+1+outcome for j in cond[i[0]] if cond[i[0]][j] == outcome][0]
    return res
print('Part 1: '+str(day2(part=1)))
print('Part 2: '+str(day2(part=2)))