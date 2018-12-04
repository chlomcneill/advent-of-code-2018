import itertools as it

current_frequency = 0
frequency_changes = []
f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 1/Day1input.txt","r")
for line in f:
    frequency_changes.append(line)
f.close()
frequency_changes = it.cycle(frequency_changes) #Cycle through list until result is reached
duplicate_check = []
for change in frequency_changes:
    current_frequency += int(change)
    if current_frequency not in duplicate_check:
        duplicate_check.append(current_frequency)
    else:
        print(current_frequency)

