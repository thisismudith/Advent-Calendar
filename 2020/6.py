# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "t" # Path of the input.txt provided from Advent Calendar (Replace '\' → '\\')
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
for o in data:
    if o == "\n":
        data[data.index(o)] = ' '
data = [o.replace('\n',';') for o in data]
if "'+" in data[-1]:
    del data[-1]
data = (''.join(data)).split(' ') #Separating Groups

def get_count(group): # Part 1
    group = list(map(str,(group.replace(';','')))) #Converting Each Group to A List
    unique_values = list(set.union(*map(set, group)))
    return len(unique_values)

def get_total_count(group): # Part 2
    group = (''.join(group.replace(';',' ')))[:-1].split(' ') #Separating Values for Per Person
    similar_values = list(set.intersection(*map(set, group)))
    return len(similar_values)   
    
def day6(part=1):
    if part not in [1,2]:
        part = 1
    if part == 1:
        value = 0
        for group in data:
             value += get_count(group)
        return value
    elif part == 2:
        value = 0
        for group in data:
            value += get_total_count(group)
        return value
print('Part 1: '+str(day6(part=1)))
print('Part 2: '+str(day6(part=2)))