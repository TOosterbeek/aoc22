from util import readInput
from util import fasterExtend
import re

stacks = {
    1: list(),
    2: list(),
    3: list(),
    4: list(),
    5: list(),
    6: list(),
    7: list(),
    8: list(),
    9: list(),
}


def loadStacks(data):
    for line in data:
        i = 0
        increment = 4
        while i < 9 * 4:
            letter = (line[i:i+increment].replace('[', '')
                      ).replace(']', '').strip()

            if (letter.strip().isnumeric()):
                break

            if (letter != ''):
                stacks[(i // 4) + 1].append(letter)

            i += increment

    for v in stacks.values():
        v.reverse()


# move <amount> from <fromStack> to <toStack>
# ex: move 3 from 6 to 2
def moveCrates(data):
    resultTopCrates = []
    for line in data:
        amount, fromStack, toStack = re.search(
            r"move (\d+) from (\d+) to (\d+)", line).groups()

        for i in range(int(amount)):
            toMove = stacks[int(fromStack)].pop()
            stacks[int(toStack)].append(toMove)

    for v in stacks.values():
        if (len(v) > 0):
            resultTopCrates.append(v.pop())

    return ''.join(resultTopCrates)

def moveCratesMultiple(data):
    resultTopCrates = []

    for line in data:
        amount, fromStack, toStack = re.search(
            r"move (\d+) from (\d+) to (\d+)", line).groups()

        toMove = stacks[int(fromStack)][-int(amount):]
        stacks[int(fromStack)] = stacks[int(fromStack)][:-int(amount)]

        stacks[int(toStack)].extend(toMove)

    for v in stacks.values():
        if (len(v) > 0):
            resultTopCrates.append(v.pop())

    return ''.join(resultTopCrates)
        


data = readInput('data/5.txt')
loadStacks(data[:9])
print(moveCrates(data[10:]))

for v in stacks.values():
    v.clear()

loadStacks(data[:9])
print(moveCratesMultiple(data[10:]))
