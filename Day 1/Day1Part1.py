import re 

def frequency_change():
    initial_frequency = 0
    frequencies = []
    f = open("/Users/mcneillc/Documents/Advent of Code/Day 1/Day1input.txt","r")
    for line in f:
        frequencies.append(line)
    f.close()
    for frequency in frequencies:
        if frequency[0] == '+':
            initial_frequency += int(re.sub('[^0-9]','',frequency))
        elif frequency[0] == '-':
            initial_frequency -= int(re.sub('[^0-9]','',frequency))
    return initial_frequency

print(frequency_change())