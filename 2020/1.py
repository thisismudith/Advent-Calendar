data = [] # Your Advent Input
data = [o.rstrip('\n') for o in data]
del data[-1]
def day1(part=1):
    done = False
    # Part 1
    if part not in [1,2]:
        part == 1 # Default Part
    if part == 1:
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] + data[j] == 2020:
                    return data[i]*data[j]
                    done = True # To stop the code after retrieving first value.
            if done:
                break

        # Part 2
    elif part == 2:
        for i in range(len(data)):
            for j in range(len(data)):
                for k in range(len(data)):
                    if data[i] + data[j] + data[k]== 2020:
                        return data[i]*data[j]*data[k]
                        done = True # To stop the code after retrieving first value.
                if done:
                    break
            if done:
                break
print(day1(part=1))
print(day1(part=2))
