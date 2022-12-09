from util import readInput

def findMarker(data, markerLength):
    curChars = []
    charCount = 0
    for char in data:
        charCount += 1

        curChars.append(char)
        if(len(curChars) >= markerLength):
            curChars = curChars[-markerLength:]

        if (len(curChars) == markerLength and len(set(curChars)) == len(curChars)):
            # Set is unique and has same length, so we got a marker yaay
            return charCount

data = readInput('data/6.txt') 
print(findMarker(data[0].strip(), 4))
print(findMarker(data[0].strip(), 14))