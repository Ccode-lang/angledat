def read_dict(filename):
    try:
        filedat = open(filename, 'r')
        file = filedat.readlines()
        filedat.close()
    except:
        print("ERROR: Not able to open file!")
        quit()
    values = {}
    #loop start
    for line in file:
        inp = line.strip()
        # comments
        if inp.startswith("$") or inp == "":
            continue
        else:
            if not "^" in inp:
                print("ERROR: Data assigned wrong!")
                quit()
            if inp.count("^") > 1:
                print("ERROR: To many assign symbols!")
                quit()
            valuename, valuevalue = inp.split("^")
            values[valuename] = valuevalue
    return values


