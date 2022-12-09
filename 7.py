from util import readInput
import re


def buildTree(data):
    fileSystem = {
        '/': dict()
    }

    # Regex for commands
    lsRegex = r"^\$ ls"
    cdRegex = r"^\$ cd (.*)" # Group1 = dir name
    dirRegex = r"^dir (.*)" # Group1 = dir name
    fileRegex = r"(\d+) (.*)" # Group1 = filesize; Group2 = fileName

    curPath = []
    for line in data:
        line = line.strip()

        if(re.match(lsRegex, line)):
            # Dont have to do anything for ls
            continue

        cdMatch = re.search(cdRegex, line)
        if (cdMatch):
            # Move to dir
            dirName = cdMatch.group(1)
            if (dirName == '..'):
                curPath.pop()
                continue

            curPath.append(dirName)

            # Inefficient way of making sure the path is or will exist but whatever
            setDictFromFileSystemPath(fileSystem, curPath, dict())

        dirMatch = re.search(dirRegex, line)
        if(dirMatch):
            dirName = dirMatch.group(1)
            setDictFromFileSystemPath(fileSystem, [*curPath, dirName], dict())

        fileMatch = re.search(fileRegex, line)
        if(fileMatch):
            fileSize, fileName = fileMatch.groups()

            # Flipped from input data as using name as key feels better, watch this bite me in the ass as I keep working on this
            setDictFromFileSystemPath(fileSystem, [*curPath, fileName], fileSize)

    return fileSystem

def setDictFromFileSystemPath(dict, path, value):
    if (len(path) == 1):
        dict[path[0]] = value
        return

    setDictFromFileSystemPath(dict[path[0]], path[1:], value)


def getDirSize(directory):
    size = 0

    if(not isinstance(directory, dict)):
        return int(directory)

    for key in directory.keys():
        if(isinstance(directory[key], dict)):
            size += getDirSize(directory[key])
            continue

        size += int(directory[key])
    
    return size

def getAllDirsInDir(directory):
    dirs = []

    if not containsDir(directory):
        return []

    for key in directory.keys():
        if(isinstance(directory[key], dict)):
            dirs.append((key, getDirSize(directory[key])))
            dirs.extend(getAllDirsInDir(directory[key]))
    
    return dirs
            
def containsDir(dir):
    for value in dir.values():
        if isinstance(value, dict):
            return True
    
    return False

def findDirToDelete(fileSystem):
    requiredSpace = 30_000_000
    usedSpace = getDirSize(fileSystem)
    unusedSpace = 70_000_000 - usedSpace
    spaceToDelete= requiredSpace - unusedSpace

    allDirs = getAllDirsInDir(fileSystem)
    
    return min([tuple[1] for tuple in allDirs if tuple[1] >= spaceToDelete])


data = readInput('data/7.txt')
fs = buildTree(data)

justDirs = getAllDirsInDir(fs)
print(sum([tuple[1] for tuple in justDirs if tuple[1] <= 100_000]))
print(findDirToDelete(fs))
