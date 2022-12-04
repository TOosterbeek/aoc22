from util import readInput


def mostCalorieElf(data):
    currentMostCalories = 0

    currentCalorieCount = 0
    for line in data:
        if (line.strip() == ''):
            currentMostCalories = currentCalorieCount if currentCalorieCount > currentMostCalories else currentMostCalories
            currentCalorieCount = 0
            continue

        currentCalorieCount = currentCalorieCount + int(line)

    return currentCalorieCount if currentCalorieCount > currentMostCalories else currentMostCalories


def topThreeCalorieElfs(data):
    curTopThree = list()

    currentCalorieCount = 0
    for line in data:
        if (line.strip() == ''):
            curTopThree.append(currentCalorieCount)
            curTopThree.sort(reverse=True)
            curTopThree = curTopThree[:3]
            currentCalorieCount = 0

            continue

        currentCalorieCount = currentCalorieCount + int(line)

    curTopThree.append(currentCalorieCount)
    curTopThree.sort(reverse=True)
    curTopThree = curTopThree[:3]

    return sum(curTopThree)


data = readInput('data/1_1.txt')

print(mostCalorieElf(data))
print(topThreeCalorieElfs(data))
