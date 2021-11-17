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


