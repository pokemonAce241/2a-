import sys

highestValDict = {}
lowestValDict = {}
colSymDict = {}
currentLine = []
firstLine = []
nextLine = []
table = []
inp = []
lastDomScore = 0
numRows = 0
isFirst = True
allowedSym = '?><$!'

def domScore(idx):
    """ 
    s1,s2 = 0,0
    w is either 1 or -1, default to 1
    get passed two lines, get the first element of both of them (a0 and b0)
        a, b = send current column and val to numNorm for a0, then for b0
        s1math = w * (a - b)/n
        s2math = w * (b - a)/n
        s1 = s1 - pow(10, s1math)
        s2 = s2 - pow(10, s2math)
    return s1 < s2
    
    """
    isLast = False
    result = -1
    if (nextLine == None):
        isLast = True
    if not isLast:
        s1,s2 = 0,0
        n = numRows / 2
        currCols = [x.strip() for x in currentLine.split(',')]
        nextCols = [x.strip() for x in nextLine.split(',')]
        for i in range(0, len(cols) - 1):
            w = -1 if colSymDict[i] is '>' else 1
            if colSymDict[i] is not '?':
                a0 = currCols[i]
                b0 = nextCols[i]
                a = numNorm(i, a0)
                b = numNorm(i, b0)
                # s1math = w * (a - b) / n
                # s2math = w * (b - a) / n
                # s1 = s1 - pow(10, s1math)
                # s2 = s2 - pow(10, s2math)
                print('a: ' + str(a))
                print('b: ' + str(b))
                if a < b:
                    result = 1
                else: 
                    result = 0
                return result
    else:
        return lastDomScore

def numNorm(currentCol, val):
    """
    (val - lowestValDict[currentCol])/(highestValDict[currentCol] - lowestValDict[currentCol] + (pow(10,-32)))
    """
    currentLow = float(lowestValDict[currentCol])
    currentHigh = float(highestValDict[currentCol])
    return (float(val) - currentLow)/((currentHigh - currentLow) + pow(10,-32))
def spreadsheet(val, t, currentPos, length, idx):
    if (currentPos != 0):

        tLength = len(table) - 1 if len(table) - 1 >= 0 else 0
        if (currentPos < (length - 1)): # not the last column
            if (len(table) is 0):
                newList = []
                newList.append(val)
                table.append(newList)
            else:
                table[tLength].append(val)
        elif (currentPos == (length - 1)):
            table[tLength].append(val)
            # append the dom score
            domSc = domScore(idx)
            lastDomScore = domSc
            # TODO: Call domScore() and append it instead of 0
            table[tLength].append(domSc)
            newList = []
            table.append(newList)
    else:
        if t is not '?':
            # create new list in table[] and add to that
            newCell = []
            newCell.append(val)
            table.append(newCell)

def buildCell(val, t, currentPos, length, idx):
    """ Function which looks at colSymDict to tell what to do with column """
    spreadsheet(val, t, currentPos, length, idx)


def lineIterator(line, idx):
    cols = [x.strip() for x in line.split(',')]

    # accounts for jagged input
    if (len(cols) is len(colSymDict)):
        colCount = 0
        for col in cols:
            try:
                if (float(col) > float(highestValDict[colCount])):
                    highestValDict[colCount] = col
                if (float(col) < float(lowestValDict[colCount])):
                    lowestValDict[colCount] = col
                colCount = colCount + 1
            except ValueError:
                # Nothing, means there was a strange character like a ? instead of a value
                colCount = colCount + 1
        colCount = 0
        for col in cols:
            buildCell(col, colSymDict[colCount], colCount, len(cols), idx)
            colCount += 1

for line in sys.stdin:
    inp.append(line)
    numRows += 1

for idx,line in enumerate(inp):
    cols = [x.strip() for x in line.split(',')]
    # Special case of first line
    if isFirst:
        # Create dict associating symbol with column number
        colCount = 0
        for item in cols:
            firstChar = item[0]
            if firstChar in allowedSym:
                if firstChar is not '?':
                    firstLine.append(item)
                colSymDict[colCount] = item[0]
            else:
                colSymDict[colCount] = 'n'
                firstLine.append(item)
            # initialize the dict to keep track of highest val
            highestValDict[colCount] = -sys.maxsize
            # initialize the dict to keep track of lowest val
            lowestValDict[colCount] = sys.maxsize
            colCount = colCount + 1
        isFirst = False
    else:
        currentLine = inp[idx]
        if idx == len(inp) - 1:
            nextLine = None
        else:
            nextLine = inp[idx + 1]
        lineIterator(line, idx)

# Had extra empty at the end
for item in table:
    if len(item) is 0:
        table.remove(item)


# Printing the output with the appended dom column
firstLine.append('dom')
print('\t'.join([str(cell) for cell in firstLine]))
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table]))
