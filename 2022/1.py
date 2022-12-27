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
def day1(part=1):
    res = []
    count = 0
    for i in data:
        if i == '': 
            res.append(count)
            count = 0
        else: count += int(i)
        
    if part == 1: return max(res)
    elif part == 2:
        total = 0
        for _ in range(3):
            total += max(res)
            del res[res.index(max(res))]
        return total
print('Part 1: '+str(day1(part=1)))
print('Part 2: '+str(day1(part=2)))