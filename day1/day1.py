import re


def parseStringToInt(string):
    strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, 9):
        if string == strings[i]:
            return str(i+1)
    return string


# task 1
answer = 0
for line in open("input", "r"):
    numbers = re.findall(r"\d", line)
    answer += int(numbers[0] + numbers[-1])
print(answer)

# task 2
regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
answer = 0
for line in open("input", "r"):
    numbers = re.findall(regex, line)
    print(numbers)
    numbers = list(map(parseStringToInt, numbers))
    print(numbers)
    answer += int(numbers[0] + numbers[-1])
print(answer)
