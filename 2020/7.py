# If you already have the data as an input use:
data = [] # Your Advent Calendar Input
# However, it is highly recommended to run this:
location = "C:\\Users\\dagam\\Downloads\\input.txt" # Path of the input.txt provided from Advent Calendar (Replace '\' → '\\')
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
if data[-1] == "'+":
    del data[-1]

def day7(part=1):
    if part not in [1,2]:
        part = 1 # Default Part
    if part == 1:
        return data
    elif part == 2:
        return 'Not now, later!'
print('Part 1: '+str(day7(part=1)))
print('Part 2: '+str(day7(part=2)))