from util import readInput
from util import intersection

items = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def getPriorities(data):
    prioSum = 0
    for line in data:
        firstCompartment = set(list(line[:(len(line) // 2)]))
        secondCompartment = set(list(line[(len(line) // 2):]))

        inBoth = firstCompartment.intersection(secondCompartment)
    
        prioSum += sum(map(lambda char: items.index(char) + 1, inBoth))

    return prioSum

def getBadges(data):

    i = 0
    increment = 3
    prioSum = 0
    while i < len(data):
        if data[i] == '':
            i+=1
            continue

        elf1 = set(list(data[i].strip()))
        elf2 = set(list(data[i+1].strip()))
        elf3 = set(list(data[i+2].strip()))

        badge = elf1.intersection(elf2).intersection(elf3)
        prioSum += sum(map(lambda char: items.index(char) + 1, badge))

        i += increment

    return prioSum

data = readInput('data/3.txt')
print(getPriorities(data))
print(getBadges(data))