
def determineHandType(cards):
    matches = [0,0,0,0]

    for i in range (0, 4):
        for j in range(i+1,5):
            if cards[i] == cards [j]:
                matches[i] += 1
    return sum(matches)

def handSortKey(hand):
    key = hand[0] * 10**10

    i = 8
    for card in hand[1]:
        key += card * 10**i
        i -= 2
    return key


#task 1
answer = 0
hands = []
for line in open("input", "r"):
    cards, bid = line.replace("\n", "").split(" ")

    cards = list(cards)
    for i in range(0,len(cards)):
        card = cards[i]
        if card == "A":
            cards[i] = 14
        elif card == "K":
            cards[i] = 13
        elif card == "Q":
            cards[i] = 12
        elif card == "J":
            cards[i] = 11
        elif card == "T":
            cards[i] = 10
        else:
            cards[i] = int(card)

    type = determineHandType(cards)
    hands.append([type,cards,bid])

hands.sort(key=handSortKey)

for i in range(0, len(hands)):
    answer += (i+1)*int(hands[i][2])

print(answer)


