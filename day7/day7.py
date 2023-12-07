def determineHandType(cards: list[int]) -> int:
    matches: list[int] = [0, 0, 0, 0]
    JOKER_VALUE = 1

    for currentCard in range(0, len(cards)-1):
        for nextCard in range(currentCard + 1, len(cards)):
            if cards[currentCard] == cards[nextCard] and cards[currentCard] != JOKER_VALUE:
                matches[currentCard] += 1
    return sum(matches)


def handSortKey(hand):
    HAND_TYPE_INDEX: int = 0
    CARDS_INDEX: int = 1

    exponent: int = 10
    key: int = 0

    key += hand[HAND_TYPE_INDEX] * (10 ** exponent)

    for card in hand[CARDS_INDEX]:
        exponent -= 2
        key += card * (10 ** exponent)

    return key


def computeTask1():
    answer: int = 0
    hands: list = []

    for line in open("input", "r"):
        lineSplit: list[str] = line.replace("\n", "").split(" ")

        cards: list = list(lineSplit[0])
        bid: int = int(lineSplit[1])

        for i in range(0, len(cards)):
            card = cards[i]
            match card:
                case "A":
                    cards[i] = 14
                case "K":
                    cards[i] = 13
                case "Q":
                    cards[i] = 12
                case "J":
                    cards[i] = 11
                case "T":
                    cards[i] = 10
                case _:
                    cards[i] = int(card)

        handType: int = determineHandType(cards)
        hands.append([handType, cards, bid])

    hands.sort(key=handSortKey)

    for i in range(0, len(hands)):
        answer += (i + 1) * int(hands[i][2])

    print(answer)


def computeTask2():
    answer: int = 0
    hands: list = []

    for line in open("input", "r"):
        lineSplit: list[str] = line.replace("\n", "").split(" ")

        cards: list = list(lineSplit[0])
        bid: int = int(lineSplit[1])

        for i in range(0, len(cards)):
            card = cards[i]
            match card:
                case "A":
                    cards[i] = 14
                case "K":
                    cards[i] = 13
                case "Q":
                    cards[i] = 12
                case "J":
                    cards[i] = 1
                case "T":
                    cards[i] = 10
                case _:
                    cards[i] = int(card)

        handType = determineHandType(cards)

        for card in cards:
            if card == 1:
                if handType == 0:
                    handType = 1
                elif handType == 1:
                    handType = 3
                elif handType == 3:
                    handType = 6
                elif handType == 6:
                    handType = 10
                elif handType == 2:
                    handType = 4

        hands.append([handType, cards, bid])

    hands.sort(key=handSortKey)

    for i in range(0, len(hands)):
        answer += (i + 1) * int(hands[i][2])

    print(answer)


computeTask1()
computeTask2()

