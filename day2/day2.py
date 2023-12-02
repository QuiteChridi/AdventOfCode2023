import re

# task 1
sum = 0
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
        sum += int(gameNumber)

print(sum)

# task 2
sum = 0

for line in open("input", "r"):
    blueDraws = re.findall(string=line, pattern=r'\d+ (?=blue)')
    redDraws = re.findall(string=line, pattern=r'\d+ (?=red)')
    greenDraws = re.findall(string=line, pattern=r'\d+ (?=green)')
    redCubesNeeded = max(list(map(int, redDraws)))
    greenCubesNeeded = max(list(map(int, greenDraws)))
    blueCubesNedded = max(list(map(int, blueDraws)))
    sum += redCubesNeeded * blueCubesNedded * greenCubesNeeded


print(sum)