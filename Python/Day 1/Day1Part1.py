f = open("/Users/mcneillc/Documents/advent-of-code-2018/Python/Day 1/Day1input.txt","r")
frequency_changes = f.readlines()
f.close()

# current_frequency = 0
# for change in frequency_changes:
#     current_frequency += int(change)
# print(current_frequency)

frequency_changes = [int(i) for i in frequency_changes]

total = sum(frequency_changes)

print(total)
