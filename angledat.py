# This file is from Angle Data
def read_dict(filename):
    try:
        filedat = open(filename, 'r')
        file = filedat.readlines()
        filedat.close()
    except:
        raise OSError("ERROR: Not able to open file!")
    values = {}
    #loop start
    for line in file:
        inp = line.strip()
        # comments
        if inp.startswith("$") or inp == "":
            continue
        else:
            if not "^" in inp:
                raise OSError("ERROR: Data assigned wrong!")
            if inp.count("^") > 1:
                raise OSError("ERROR: To many assign symbols!")
            valuename, valuevalue = inp.split("^")
            values[valuename.strip()] = valuevalue.strip()
    return values

def getinhistory(filename, defin=0):
    value = None
    counter = 0
    dict = read_dict(filename)
    for name, value in dict:
        if counter == defin:
            value = value
        counter += 1
