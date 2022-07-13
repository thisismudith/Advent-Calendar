# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "" # Path of the input.txt provided from Advent Calendar
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
if data[-1] == "'+":
    del data[-1]
def day1(part=1):
    done = False
    # Part 1
    if part not in [1,2]:
        part = 1 # Default Part
    if part == 1:
        for i in data:
            for j in data:
                if int(i) + int(j) == 2020:
                    done = True
                    return int(i)*int(j)
            if done:
                break
    else: # Part 2
        for i in data:
            for j in data:
                for k in data:
                    if int(i) + int(j) + int(k)== 2020:
                        done = True
                        return int(i)*int(j)*int(k)
                if done:
                    break
            if done:
                break
print('Part 1: '+day1(part=1))
print('Part 2: '+day1(part=2))