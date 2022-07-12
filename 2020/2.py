data = [] # Your Advent Input
data = [o.rstrip('\n') for o in data]
del data[-1]
def day2(part=1):
    count = 0
    if part not in [1,2]:
        part == 1 #Default Part
    for i in data:
        i = i.split(' ')
        start = int(i[0].split('-')[0])
        end = int(i[0].split('-')[-1])
        letter = i[1].rstrip(':')
        pwd = i[-1]
        if (start <= pwd.count(letter) <= end) and part == 1: # Part 1
            count+=1
        if part == 2: # Part 2
            if (pwd[start-1] == letter and pwd[end-1] != letter) or (pwd[start-1] != letter and pwd[end-1] == letter):
                count += 1
    return count
print(day2(part=1))
print(day2(part=2))