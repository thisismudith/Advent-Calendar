import json #Required to convert str → dict
# If you already have the data as an input use:
data = [] # Your Advent Input
# However, it is highly recommended to run this:
location = "C:\\Users\\dagam\\Downloads\\input.txt" # Path of the input.txt provided from Advent Calendar
try:
    with open(location,'r') as f:
        data = (''.join(f.readlines())).split('\n\n')
        f.close()
except:
    pass
if data[-1] == "'+":
    del data[-1]

def convert_to_json(data:str):
    keys, values = data.split(':'), data.split(':')
    del keys[-1]
    del values[0]
    new_dict = {}
    for i in keys:
        get_key = i.replace('\n',' ')
        keys[keys.index(i)] = get_key.rsplit(' ')[-1]
    for i in values:
        get_value = i.replace('\n',' ')
        values[values.index(i)] = get_value.split(' ')[0]
    for k, v in zip(keys,values):
        new_dict[k] = v
    return new_dict
    
def range_values(data:dict):
    byr = 1920 <= data["byr"] <= 2002
    iyr = 2010 <= data["iyr"] <= 2020
    eyr = 2020 <= data["eyr"] <= 2030
    hgt_unit = data["hgt"][-2:]
    if hgt_unit == "cm":
        hgt = 150 <= int(data["hgt"][:-2]) <= 193
    elif hgt_unit == "in":
        hgt = 59 <= int(data["hgt"][:-2]) <= 76
    hcl, ecl = True, True
    if len(data["hcl"]) == 7:
        hcl_hex = data["hcl"][1:]
        for h in hcl_hex.lower():
            if h not in "0123456789abcdef":
                hcl = False
    if data["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        ecl = False
def day4(part=1):
    count = 0
    sep_list = [] #Separated List
    if part not in [1,2]:
        part = 1
    for i in data:
        sep_list.append(convert_to_json(i))
    if part == 1:
        for key in sep_list:
            if all(values in key.keys() for values in['byr','iyr','eyr','hgt','hcl','ecl','pid']):
                count += 1
        return count
    else:
        for i in sep_list:
            print(len(i["pid"]), i["pid"], i)
            # range_values(i)
print(f"Part 1: {day4(part=1)}")
print(f"Part 2: {day4(part=2)}")