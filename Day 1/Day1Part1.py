f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 1/Day1input.txt","r")
frequency_changes = f.readlines()
f.close()

current_frequency = 0
for change in frequency_changes:
    current_frequency += int(change)
print(current_frequency)