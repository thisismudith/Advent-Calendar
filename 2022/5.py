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
def day5(part=1):
    import re
    moves = data[data.index('')+1:]
    _crates = [c.replace('    ',' ').split(' ') for c in data[:data.index('')-1]]
    _crates = [''.join([_crates[j][i] for j in range(len(_crates))]) for i in range(len(_crates[0]))]
    crates = [re.findall('([A-Z])+', crate)[::-1] for crate in _crates]
    for m in moves:
        a, b, c = map(int, re.findall(r'\d+', m))
        if part == 1: 
            for _ in range(a):
                crates[c-1].append(crates[b-1].pop())
        elif part == 2:
            crates[c-1] = crates[c-1] + crates[b-1][-a:]
            crates[b-1] = crates[b-1][:-a]
    return ''.join(c[-1] for c in crates if len(c) > 0)
print('Part 1: '+str(day5(part=1)))
print('Part 2: '+str(day5(part=2)))