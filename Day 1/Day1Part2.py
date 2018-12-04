import re 
import itertools as it

def frequency_change():
    frequency_tracker = 0
    frequencies = []
    f = open("/Users/mcneillc/Documents/Advent of Code/Day 1/Day1input.txt","r")
    for line in f:
        frequencies.append(line)
    f.close()
    frequencies = it.cycle(frequencies)
    duplicate_check = []
    for frequency in frequencies:
        frequnecy_integer = int(re.sub('[^0-9]','',frequency))
        if frequency[0] == '+':
            frequency_tracker += frequnecy_integer
            if frequency_tracker not in duplicate_check:
                duplicate_check.append(frequency_tracker)
            else:
                return frequency_tracker
        elif frequency[0] == '-':
            frequency_tracker -= frequnecy_integer
            if frequency_tracker not in duplicate_check:
                duplicate_check.append(frequency_tracker)
            else:
                return frequency_tracker
    return frequency_tracker, duplicate_check


print(frequency_change())