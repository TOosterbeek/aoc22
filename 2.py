from util import readInput
# A = ROCK = 1p
# B = PAPER = 2p
# C = SCISSORS = 3p

# X = ROCK = 1p
# Y = PAPER = 2p
# Z = SCISSORS 3p

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# key loses from value
losesFrom = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

# key loses from value
losesFromSimplified = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}


def totalScore_1(data):
    score = 0

    for line in data:
        incoming, outgoing = line.strip().split(' ')

        index = 25 - (2 - alphabet.index(incoming))  # ABC -> XYZ
        if (losesFrom[incoming] == outgoing):
            score += 6
        elif (alphabet[index] == outgoing):
            score += 3

        indexBackwards = (alphabet.index(outgoing) + 3) % 26  # XYZ->ABC
        score += indexBackwards + 1

    return score


def totalScore_2(data):
    score = 0

    invertedMap = inv_map = {v: k for k, v in losesFromSimplified.items()}

    for line in data:
        incoming, result = line.strip().split()

        if (result == 'X'):
            # Lose
            losingAnswer = invertedMap[incoming]
            score += alphabet.index(losingAnswer) + 1
        if (result == 'Y'):
            # Draw
            score += 3 + alphabet.index(incoming) + 1
        if (result == 'Z'):
            # Win
            score += 6 + alphabet.index(losesFromSimplified[incoming]) + 1

    return score


data = readInput('data/2.txt')
print(totalScore_1(data))
print(totalScore_2(data))
