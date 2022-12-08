from util import readInput

def findSubsets(data):
    count = 0
    for line in data:
        numbers1, numbers2 = line.strip().split(',')
        lower1, upper1 = numbers1.split('-')
        lower2, upper2 = numbers2.split('-')
        range1 = set(range(int(lower1), int(upper1) + 1))
        range2 = set(range(int(lower2), int(upper2) + 1))

        count += range1.issubset(range2) or range2.issubset(range1)

    return count

def findOverlaps(data):
    count = 0
    for line in data:
        numbers1, numbers2 = line.strip().split(',')
        lower1, upper1 = numbers1.split('-')
        lower2, upper2 = numbers2.split('-')
        range1 = set(range(int(lower1), int(upper1) + 1))
        range2 = set(range(int(lower2), int(upper2) + 1))

        count += len(range1.intersection(range2)) > 0 or len(range2.intersection(range1)) > 0

    return count

data  = readInput('data/4.txt')
print(findSubsets(data))
print(findOverlaps(data))