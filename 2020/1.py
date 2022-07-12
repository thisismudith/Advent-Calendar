data = [] # Your Advent Input as a proper list.
# Recommended to run this for input:
with open(location,'r') as f: #Replace location with the input.txt file location of your Advent Input
    data = f.readlines()
    f.close()
data = [o.rstrip('\n') for o in data]
del data[-1]
def day1(part=1):
    done = False
    if part not in [1,2]:
        part == 1 # Default Part
    if part == 1: # Part 1
        for i in data:
            for j in data:
                if i + j == 2020:
                    return i*j
                    done = True # To stop the code after retrieving first value.
            if done:
                break
    elif part == 2: # Part 2
        for i in data:
            for j in data:
                for k in data:
                    if i + j + k == 2020:
                        return i*j*k
                        done = True # To stop the code after retrieving first value.
                if done:
                    break
            if done:
                break
print(day1(part=1))
print(day1(part=2))
