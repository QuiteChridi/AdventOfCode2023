
#task 1
sum = 0
input = []

for line in open("testinput", "r"):
    input.append(line)

for j in range(0,len(input)):
    for i in range(0, len(input[j])):
        if input[j][i] != r'[\.\d]':

