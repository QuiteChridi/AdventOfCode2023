import re

# task 1
answer = 0
redCubes = 12
greenCubes = 13
blueCubes = 14

for line in open("input", "r"):
    gameNumber = re.search(string=line, pattern=r'\d+').group()

    blueDraws = re.findall(string=line, pattern=r'\d+ (?=blue)')
    redDraws = re.findall(string=line, pattern=r'\d+ (?=red)')
    greenDraws = re.findall(string=line, pattern=r'\d+ (?=green)')
    redPossible = max(list(map(int, redDraws))) <= redCubes
    greenPossible = max(list(map(int, greenDraws))) <= greenCubes
    bluePossible = max(list(map(int, blueDraws))) <= blueCubes

    if redPossible and bluePossible and greenPossible:
        answer += int(gameNumber)

print(answer)

# task 2
answer = 0

for line in open("input", "r"):
    blueDraws = re.findall(string=line, pattern=r'\d+ (?=blue)')
    redDraws = re.findall(string=line, pattern=r'\d+ (?=red)')
    greenDraws = re.findall(string=line, pattern=r'\d+ (?=green)')
    redCubesNeeded = max(list(map(int, redDraws)))
    greenCubesNeeded = max(list(map(int, greenDraws)))
    blueCubesNeeded = max(list(map(int, blueDraws)))
    answer += redCubesNeeded * blueCubesNeeded * greenCubesNeeded


print(answer)