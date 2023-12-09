import re
import math


class Node:
    name: str
    leftInstruction: str
    rightInstruction: str

    def __init__(self, name, leftInstruction, rightInstruction):
        self.name = name
        self.leftInstruction = leftInstruction
        self.rightInstruction = rightInstruction


def computeTask1():
    nodes: list[Node] = []

    input = open("input", "r")
    instructions: list[chr] = list(input.readline())
    instructions.remove('\n')
    input.readline()

    for line in input:
        values: list[str] = re.findall(r"\w{3}", line)
        node: Node = Node(name=values[0], leftInstruction=values[1], rightInstruction=values[2])
        nodes.append(node)

    instructionIndex: int = 0
    answer: int = 0
    nextNodeName: str = "AAA"

    while nextNodeName != "ZZZ":
        if instructionIndex == len(instructions):
            instructionIndex = 0

        for node in nodes:
            if node.name == nextNodeName:
                if instructions[instructionIndex] == 'L':
                    nextNodeName = node.leftInstruction
                    break
                else:
                    nextNodeName = node.rightInstruction
                    break

        instructionIndex += 1
        answer += 1
    print(answer)


def computeTask2():
    nodes: list[Node] = []

    input = open("input", "r")
    instructions: list[chr] = list(input.readline())
    instructions.remove('\n')
    input.readline()

    for line in input:
        values: list[str] = re.findall(r"\w{3}", line)
        node: Node = Node(name=values[0], leftInstruction=values[1], rightInstruction=values[2])
        nodes.append(node)

    instructionIndex: int = 0
    answers: list[int] = []

    nextNodeNames: list[str] = list(map(lambda n: n.name, filter(lambda n: n.name[2] == "A", nodes)))

    for nextNodeName in nextNodeNames:
        answer = 0
        while nextNodeName[2] != "Z":

            if instructionIndex == len(instructions):
                instructionIndex = 0

            for node in nodes:
                if node.name == nextNodeName:
                    if instructions[instructionIndex] == 'L':
                        nextNodeName = node.leftInstruction
                        break
                    else:
                        nextNodeName = node.rightInstruction
                        break

            instructionIndex += 1
            answer += 1
        answers.append(answer)

    print(math.lcm(*answers))


computeTask1()
computeTask2()