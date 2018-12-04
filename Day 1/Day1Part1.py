current_frequency = 0
frequency_changes = []

f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 1/Day1input.txt","r")
for line in f:
    frequency_changes.append(line)
f.close()

for change in frequency_changes:
    current_frequency += int(change)
print(current_frequency)