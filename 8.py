from util import readInput
from itertools import takewhile


def buildGrid(data):
    grid = []  # grid[row][col]

    for line in data:
        grid.append(list(line.strip()))

    return grid

# just iterate, whatever


def getVisible(grid):
    visible = set()
    # #ltr
    for rowIndex in range(len(grid)):
        highest = -1
        for colIndex in range(len(grid[0])):
            col = grid[rowIndex][colIndex]
            if int(col) > highest:
                highest = int(col)
                visible.add((rowIndex, colIndex))

    # rtl
    for rowIndex in range(len(grid)):
        highest = -1

        for colIndex in range(len(grid[0]) - 1, 0, -1):
            val = grid[rowIndex][colIndex]
            if int(val) > highest:
                highest = int(val)
                visible.add((rowIndex, colIndex))

    # top to bottom
    for colIndex in range(len(grid[0])):
        highest = -1

        for rowIndex in range(len(grid)):
            val = grid[rowIndex][colIndex]
            if int(val) > highest:
                highest = int(val)
                visible.add((rowIndex, colIndex))

    for colIndex in range(len(grid[0])):
        highest = -1

        for rowIndex in range(len(grid) - 1, 0, -1):
            val = grid[rowIndex][colIndex]
            if int(val) > highest:
                highest = int(val)
                visible.add((rowIndex, colIndex))

    return len(visible)


def getScenic(grid):
    scenic = list()

    # for rowIndex, row in enumerate(grid):
    #     for colIndex, col in enumerate(row):
    #         treeHeight = int(grid[rowIndex][colIndex])
    #         underHeight = lambda x: int(x) < treeHeight

    #         ltr = next(((abs(x - colIndex), grid[rowIndex][x]) for x in range(colIndex + 1, len(row)) if int(grid[rowIndex][x]) > treeHeight), (0, 0))
    #         rtl = next(((abs(colIndex - x), grid[rowIndex][x]) for x in range(colIndex - 1) if int(grid[rowIndex][x]) > treeHeight), (0, 0))

    #         ttp = next(((abs(rowIndex - x), grid[x][colIndex]) for x in range(rowIndex + 1, len(grid)) if int(grid[rowIndex][x]) > treeHeight),(0, 0))
    #         btp = next(((abs(x - rowIndex), grid[x][colIndex]) for x in range(rowIndex - 1) if int(grid[rowIndex][x]) > treeHeight), (0, 0))

    #         scenic.append(ltr[0] * rtl[0] * ttp[0] * btp[0])

    for rowIndex, row in enumerate(grid):
        for colIndex, col in enumerate(row):
            treeHeight = int(col)

            ltr = [grid[rowIndex][x] for x in range(colIndex + 1, len(row))]
            rtl = [grid[rowIndex][x] for x in range(colIndex - 1, -1, -1)]
            ttp = [grid[x][colIndex] for x in range(rowIndex + 1, len(grid))]
            btt = [grid[x][colIndex] for x in range(rowIndex - 1, -1, -1)]

            ltrCount = 0
            i = ''
            for i in ltr:
                ltrCount += 1
                if int(i) >= treeHeight:
                    break

            rtlCount = 0
            j = ''
            for j in rtl:
                rtlCount += 1
                if int(j) >= treeHeight:
                    break

            ttpCount = 0
            k = ''
            for k in ttp:
                ttpCount += 1
                if int(k) >= treeHeight:
                    break

            bttCount = 0
            l = ''
            for l in btt:
                bttCount += 1
                if int(l) >= treeHeight:
                    break

            scenic.append(ltrCount * rtlCount * ttpCount * bttCount)
    return scenic


data = readInput('data/8_old.txt')
grid = buildGrid(data)
print(getVisible(grid))
grid = buildGrid(data)
print(max(getScenic(grid)))
