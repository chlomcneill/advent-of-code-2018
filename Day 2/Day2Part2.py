import itertools as it

def differ_by_1_char(a, b):
    differ_count = 0
    length = len(a) #Assume strings a and b are equal in length
    for i in range(length):
        if a[i] != b[i]:
            differ_count += 1
    if differ_count == 1:
        return True
    else:
        return False

IDs = []

f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 2/Day2input.txt","r")
for line in f:
    IDs.append(line)
f.close()

IDs = [ID.strip('\n') for ID in IDs]

correct_box_IDs = []
for ID1, ID2 in it.combinations(IDs, 2):
    if differ_by_1_char(ID1, ID2) == True:
        correct_box_IDs.extend([ID1, ID2])

result = ''
a = correct_box_IDs[0]
b = correct_box_IDs[1]

for i in range(len(a)):
    if a[i] == b[i]:
        result += a[i]
        
print(result)
