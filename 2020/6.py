# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "C:\\Users\dagam\downloads\\input.txt" # Path of the input.txt provided from Advent Calendar
try:
    with open(location,'r') as f:
        data = f.readlines()
        f.close()
except:
    pass
data = [o.rstrip('\n') for o in data]
if data[-1] == "'+":
    del data[-1]