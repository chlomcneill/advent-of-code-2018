f = open("/Users/mcneillc/Documents/advent-of-code-2018/Python/Day 1/Day1input.txt","r")
frequency_changes = f.readlines()
f.close()

frequency_changes = [int(i) for i in frequency_changes]
print(sum(frequency_changes))
