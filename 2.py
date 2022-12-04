from util import readInput

#Disgusting code coming up, brace, brace, brace

# Bunch of dictionaries because fuck it
rules = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}  # Only really works for the first solution

losing = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

pointsInbound = {
    'A': 1,
    'B': 2,
    'C': 3,
}

optionMap = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

convertTable = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}


def calculateScore(data):
    totalWinPoints = 0
    for line in data:
        inbound, outbound = line.strip().split(' ')

        winPoints = 0
        if (optionMap[inbound] == outbound):
            winPoints = 3
        elif rules[inbound] == outbound:
            winPoints = 6

        totalWinPoints += points[outbound] + winPoints

    return totalWinPoints


def calculateScore2(data):
    totalWinPoints = 0
    for line in data:
        inbound, result = line.strip().split(' ')
        
        winPoints = 0
        if (result == 'Y'):
            winPoints = 3 + points[convertTable[inbound]]
        elif (result == 'Z'):
            winPoints = 6 + points[rules[inbound]]
        else:
            winPoints = pointsInbound[losing[inbound]]

        totalWinPoints += winPoints

    return totalWinPoints


data = readInput('data/2.txt')
print(calculateScore(data))
print(calculateScore2(data))
