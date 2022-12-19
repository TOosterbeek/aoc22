from util import readInput
import re
from math import sqrt, pow


def getPositions(data, headPos, tailPos):
    visited = set()
    visited.add((0, 0))

    rightRegex = r'^R (\d+)'
    leftRegex = r'^L (\d+)'
    upRegex = r'^U (\d+)'
    downRegex = r'^D (\d+)'
    for line in data:
        rightMatch = re.search(rightRegex, line)
        leftMatch = re.search(leftRegex, line)
        upMatch = re.search(upRegex, line)
        downMatch = re.search(downRegex, line)

        right = rightMatch and int(rightMatch.group(1))
        left = leftMatch and int(leftMatch.group(1))
        up = upMatch and int(upMatch.group(1))
        down = downMatch and int(downMatch.group(1))

        for i in range(right or 0):
            headPos = (headPos[0] + 1, headPos[1])
            if not isAdjacent(headPos, tailPos):
                tailPos = (headPos[0] - 1, headPos[1])
                visited.add(tailPos)

        for j in range(left or 0):
            headPos = (headPos[0] - 1, headPos[1])
            if not isAdjacent(headPos, tailPos):
                tailPos = (headPos[0] + 1, headPos[1])
                visited.add(tailPos)

        for k in range(up or 0):
            headPos = (headPos[0], headPos[1] + 1)
            if not isAdjacent(headPos, tailPos):
                tailPos = (headPos[0], headPos[1] - 1)
                visited.add(tailPos)

        for l in range(down or 0):
            headPos = (headPos[0], headPos[1] - 1)
            if not isAdjacent(headPos, tailPos):
                tailPos = (headPos[0], headPos[1] + 1)
                visited.add(tailPos)

    return visited


def solution2(data):
    visited = set()
    visited.add((0, 0))
    startPos = [(0, 0)]
    rope = startPos * 10

    rightRegex = r'^R (\d+)'
    leftRegex = r'^L (\d+)'
    upRegex = r'^U (\d+)'
    downRegex = r'^D (\d+)'
    for line in data:
        rightMatch = re.search(rightRegex, line)
        leftMatch = re.search(leftRegex, line)
        upMatch = re.search(upRegex, line)
        downMatch = re.search(downRegex, line)

        right = rightMatch and int(rightMatch.group(1))
        left = leftMatch and int(leftMatch.group(1))
        up = upMatch and int(upMatch.group(1))
        down = downMatch and int(downMatch.group(1))

        for i in range(right or 0):
            rope = moveRope(rope, (1, 0))
            visited.add(rope[-1])

        for j in range(left or 0):
            rope = moveRope(rope, (-1, 0))
            visited.add(rope[-1])

        for k in range(up or 0):
            rope = moveRope(rope, (0, 1))
            visited.add(rope[-1])

        for l in range(down or 0):
            rope = moveRope(rope, (0, -1))
            visited.add(rope[-1])

    return visited


def moveRope(rope, direction):
    if len(rope) == 1:
        # just the tail
        return rope

    rope[0] = (rope[0][0] + direction[0], rope[0][1] + direction[1])

    if not isAdjacent(rope[0], rope[1]):
        rope[1] = (rope[1][0] - direction[0], rope[1][1] - direction[1])

    # extend a result var probably
    rope[1:] = moveRope(rope[1:], direction)

    return rope


def isAdjacent(headPos, tailPos):
    horizontalTouch = headPos[0] - tailPos[0]
    verticalTouch = headPos[1] - tailPos[1]

    # What, maths????
    return sqrt(pow(horizontalTouch, 2) + pow(verticalTouch, 2)) < 2


data = readInput('data/9.txt')
print(len(getPositions(data, (0, 0), (0, 0))))
print(len(solution2(data)))
