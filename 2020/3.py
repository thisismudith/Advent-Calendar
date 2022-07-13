# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "C:\\Users\\dagam\\Downloads\\temp-files\\input.txt" # Path of the input.txt provided from Advent Calendar
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
if data[-1] == "'+":
    del data[-1]

def tree_at_cord(x,y):
    x_map = x % len(data[0]) # We need to repeat the tree data throughout the whole hill.
    return data[y][x_map] == "#"
def increment(x_incr,y_incr):
    x_cord, y_cord, trees = 0,0,0
    while y_cord < len(data):
        if tree_at_cord(x_cord,y_cord):
            trees += 1
        x_cord += x_incr
        y_cord += y_incr
    return trees
def day3(part=1):
    if part not in [1,2]:
        part = 1 # Default Part
    if part == 1:
        return increment(3,1)
    else:
        return increment(1,1)*increment(3,1)*increment(5,1)*increment(7,1)*increment(1,2)
print('Part 1: '+str(day3(part=1)))
print('Part 2: '+str(day3(part=2)))
    
