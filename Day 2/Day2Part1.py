def ID_scan():
    IDs = []
    f = open("/Users/mcneillc/Documents/Advent of Code/Day 2/Day2input.txt","r")
    for line in f:
        IDs.append(line)
    f.close()
    for ID in IDs:
        ID.strip('\n')
    return IDs

print(ID_scan())