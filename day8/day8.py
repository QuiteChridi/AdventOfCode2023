import re


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


def startNodeFilter(node: Node):
    return node.name[2] == "A"


def computeTask2():
    nodes: list[Node] = []

    input = open("input", "r")
    instructions: list[chr] = list(input.readline())
    instructions.remove('\n')
    input.readline()

    for line in input:
        values: list[str] = re.findall(r"\w{3}", line)
        node: Node = Node(name=values[0], leftInstruction=[1], rightInstruction=[2])
        nodes.append(node)

    instructionIndex: int = 0
    answer: int = 0

    print(filter(startNodeFilter, nodes))

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


computeTask1()
