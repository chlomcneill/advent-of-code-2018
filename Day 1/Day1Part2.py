import itertools as it

f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 1/Day1input.txt","r")
frequency_changes = f.readlines()
f.close()

current_frequency = 0
frequency_changes = it.cycle(frequency_changes) #Cycle through list until result is reached
duplicate_check = []
for change in frequency_changes:
    current_frequency += int(change)
    if current_frequency not in duplicate_check:
        duplicate_check.append(current_frequency)
    else:
        print(current_frequency)

