def polymer_scanner(polymer):
    # if polymer is not str:
    #     polymer = str(polymer)
    for char in polymer:
    if i in range(0, len(polymer) - 1):
        if polymer[i] == polymer[i+1]:
            i+=1
        elif polymer[i] != polymer[i+1]:
            if polymer[i].casefold() == polymer[i+1].casefold():
                polymer.replace(polymer[i:i+2],"")
                if i != 0:
                    i -=1
            else:
                i+=1
    elif i == len(polymer) - 1:
        return polymer

def blah(polymer):
    i = 0
    while i in range(0, len(polymer)):
        polymer_scanner(polymer, i)
    
print(blah('dabAcCaCBAcCcaDA'))



# def polymer_scanner(polymer):
#     i = 0
#     while i in range(0, len(polymer) - 1):
#         if polymer[i] == polymer[i+1]:
#             i += 1
#             polymer_scanner(polymer)
#         elif polymer[i] != polymer[i+1]:
#             if polymer[i].casefold() == polymer[i+1].casefold():
#                 polymer.replace(polymer[i:i+2],"")
#                 if i == 0:
#                     polymer_scanner(polymer, i)
#                 else:
#                     polymer_scanner(polymer, i-1)
#             else:
#                 polymer_scanner(polymer, i+1)
#     return polymer


