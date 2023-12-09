
def getNextDiffSequence(values: list[int]) -> list[int]:
    result = []
    for i in range (0, len(values)-1):
        result.append(values[i+1] - values[i])
    return result



def computeTask1():
    sequences: list[list[int]] = []
    answer: int = 0

    for line in open("input"):
        line.replace("\n","")
        sequence: list[int] = list(map(int, line.split(" ")))
        sequences.append(sequence)

    for sequence in sequences:
        subsequences: list[list[int]] = []
        subsequences.append(sequence)
        while not all(x == 0 for x in sequence):
            sequence = getNextDiffSequence(sequence)
            subsequences.append(sequence)

        subsequences.reverse()
        subsequences[0].append(0)
        for i in range(1, len(subsequences)):
            subsequences[i].append(subsequences[i][-1] + subsequences[i-1][-1])
        answer += subsequences[-1][-1]
    print(answer)


computeTask1()