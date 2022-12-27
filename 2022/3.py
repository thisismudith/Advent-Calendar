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
def day3(part=1):
    import string
    res = 0
    if part == 1:
        for i in data:
            one, two = i[len(i)//2:], i[:len(i)//2]
            common = ''.join(set.intersection(set(one), set(two)))
            res += string.ascii_letters.index(common)+1
    elif part == 2:
        grouped = zip(*(iter(data),)*3)
        for i in grouped:
            common = ''.join(set.intersection(set(i[0]), set(i[1]), set(i[2])))
            res += string.ascii_letters.index(common)+1            
    return res
print('Part 1: '+str(day3(part=1)))
print('Part 2: '+str(day3(part=2)))