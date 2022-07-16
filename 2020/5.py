# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "C:\\Users\\dagam\\Downloads\\input.txt" # Path of the input.txt provided from Advent Calendar
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
    row_pos = string[:8]
    print(row_pos)
def day5(part=1):
    if part not in [1,2]:
        part = 1
    if part == 1:
        for i in data:
            get_row_column(i)