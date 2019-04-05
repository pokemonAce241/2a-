import sys

allowedSym = '?><$!'
isFirst = True
colSymDict = {}
table = []
highestValDict = {}
lowestValDict = {}

# def domScore():
    
def spreadsheet(val, t, currentPos, length):
    if (currentPos != 0):
        # if t is '?':
            # Remove that column from the highestValDict

        tLength = len(table) - 1 if len(table) - 1 >= 0 else 0
        if (currentPos < (length - 1)):
            if (len(table) is 0):
                newList = []
                newList.append(val)
                table.append(newList)
            else:
                table[tLength].append(val)
        elif (currentPos == (length - 1)):
            table[tLength].append(val)
            # append the dom score
            domScore = '0'
            # TODO: Call domScore() and append it instead of 0
            table[tLength].append(domScore)
            newList = []
            table.append(newList)


    else:
        if t is not '?':
            # create new list in table[] and add to that
            newCell = []
            newCell.append(val)
            table.append(newCell)

def buildCell(val, t, currentPos, length):
    """ Function which looks at colSymDict to tell what to do with column """
    
    spreadsheet(val, t, currentPos, length)


def lineIterator(line):
    cols = [x.strip() for x in line.split(',')]
    if (len(cols) is len(colSymDict)):
        colCount = 0
        for col in cols:
            if (float(col) > float(highestValDict[colCount])):
                highestValDict[colCount] = col
            if (float(col) < float(lowestValDict[colCount])):
                lowestValDict[colCount] = col
            buildCell(col, colSymDict[colCount], colCount, len(cols))
            colCount = colCount + 1

for line in sys.stdin:
    cols = [x.strip() for x in line.split(',')]
    # Special case of first line
    if isFirst:
        # Create dict associating symbol with column number
        colCount = 0
        for item in cols:
            firstChar = item[0]
            if firstChar in allowedSym:
                colSymDict[colCount] = item[0]
            else:
                colSymDict[colCount] = 'n'
            # initialize the dict to keep track of highest val
            highestValDict[colCount] = -sys.maxsize
            # initialize the dict to keep track of lowest val
            lowestValDict[colCount] = sys.maxsize
            colCount = colCount + 1
        isFirst = False
    else:
        lineIterator(line)

# Had extra empty at the end
for item in table:
    if len(item) is 0:
        table.remove(item)

# Only for Testing, TAKE OUT 
for item in table:
    print(item)

