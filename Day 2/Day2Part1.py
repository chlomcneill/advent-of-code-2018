import string

def letter_repeats_exactly_2_times(n):
    alphabet = list(string.ascii_lowercase)
    repeats = []
    for letter in alphabet:
        if n.count(letter) == 2:
            repeats.append(letter)
            return repeats

def letter_repeats_exactly_3_times(n):
    alphabet = list(string.ascii_lowercase)
    repeats = []
    for letter in alphabet:
        if n.count(letter) == 3:
            repeats.append(letter)
            return repeats

IDs = []

f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 2/Day2input.txt","r")
for line in f:
    IDs.append(line)
f.close()

IDs = [ID.strip('\n') for ID in IDs]
double = 0
triple = 0

for ID in IDs:
    if letter_repeats_exactly_2_times(ID) != None:
        double += 1
for ID in IDs:
    if letter_repeats_exactly_3_times(ID) != None:
        triple += 1

checksum = double * triple

print(checksum)