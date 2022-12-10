from util import readInput

def buildGrid(data):
    grid = [] # grid[row][col]

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

        for colIndex in range(len(grid[0]) -1, 0, -1):
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

            
data = readInput('data/8.txt')
grid = buildGrid(data)
print(getVisible(grid))