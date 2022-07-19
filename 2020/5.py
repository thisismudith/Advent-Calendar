# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "" # Path of the input.txt provided from Advent Calendar (Replace '\' → '\\')
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
if data[-1] == "'+":
    del data[-1]

def get_row_column(string):
    row_pos, col_pos = string[:7], string[-3:]
    row_start, col_start = 0, 0
    row_end, col_end = 127, 7
    row, col = 0, 0
    for i in row_pos:
        if i == "F":
            row_end -= round((row_end-row_start)/2)
        elif i == "B":
            row_start += round((row_end-row_start)/2)
    if row_pos[-1] == "F":
        row = row_start
    else:
        row = row_end
    for i in col_pos:
        if i == "L":
            col_end -= round((col_end-col_start)/2)
        elif i == "R":
            col_start += round((col_end-col_start)/2)
    if col_pos[-1] == "L":
        col = col_start
    else:
        col = col_end
    return row, col
def day5(part=1):
    if part not in [1,2]:
        part = 1
    row_and_column = []
    for string in data:
        row_and_column.append(get_row_column(string))
    if part == 1:
        for i in row_and_column:
            row_and_column[row_and_column.index(i)] = i[0]*8 + i[1]
        return max(row_and_column)
    elif part == 2: #Part 2
        for i in row_and_column:
            row_and_column[row_and_column.index(i)] = i[0]*8 + i[1]
        row_and_column.sort()
        for seat_1 in range(len(row_and_column)-1):
            if row_and_column[seat_1+1] - row_and_column[seat_1] > 1: #Check for missing seat
                return int((row_and_column[seat_1+1]+row_and_column[seat_1])/2) 

print("Part 1: "+str(day5(part=1)))
print("Part 2: "+str(day5(part=2)))
