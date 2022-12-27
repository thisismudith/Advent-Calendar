# If you already have the data as an input use:
data = [] # Your Advent Calendar Input
# However, it is highly recommended to run this:
location = "  " # Path of the input.txt provided from Advent Calendar (Replace '\' → '\\')
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
def day4(part=1):
    res = 0
    for i in data:
        min1, max1, min2, max2 = *(int(x) for x in i.split(',')[0].split('-')), *(int(x) for x in i.split(',')[1].split('-'))
        if part == 1: 
            if (min1 <= min2 and max1 >= max2) or (min1 >= min2 and max1 <= max2):
                res += 1
        elif part == 2:
            if (min1 <= min2 <= max1) or (min2 <= min1 <= max2):
                res += 1
    return res
print('Part 1: '+str(day4(part=1)))
print('Part 2: '+str(day4(part=2)))