def frequency_change():
    initial_frequency = 0
    frequencies = []
    f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 1/Day1input.txt","r")
    for line in f:
        frequencies.append(line)
    f.close()
    for frequency in frequencies:
        initial_frequency += int(frequency)
    return initial_frequency

print(frequency_change())