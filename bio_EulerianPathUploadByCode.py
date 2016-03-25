import sys

def findEulerPath(key, value, currentList, now, numOfRelations):
    global printOnce

    if now == numOfRelations:
        output = ""
        for i in range(len(currentList)-1):
           output += (currentList[i] + "->")
        print ("%s%s" % (output, currentList[-1]))
        return
    if not key:
        return

    backupKey = key[:]
    backupValue = value[:]
    backupCurrentList = currentList[:]
    for i in range(len(key)):
        if currentList[-1] == key[i]:
            currentList.append(value[i])
            key.pop(i)
            value.pop(i)
            now += 1

            findEulerPath(key, value, currentList, now, numOfRelations)

            key = backupKey[:]
            value = backupValue[:]
            currentList = backupCurrentList[:]
            now -= 1

printOnce = False
adjacentList = {}
key = []
value = []
while True:
    try:
        s = input()
        splitString = s.replace(' ', '').split("->")
        for each in splitString[1].split(','):
            #print splitString[0], each
            key.append(splitString[0])
            value.append(each)
    except:
        break

sys.setrecursionlimit(len(key) + 1)
numOfRelations = len(key)
backupKey = key[:]
backupValue = value[:]
# for i in range(len(key)):
#     backupKey.append(key[i])
#     backupValue.append(value[i])
# print backupKey
# print backupValue

for i in range(len(key)):
    currentList = []
    currentList.append(key[i])
    currentList.append(value[i])
    key.pop(i)
    value.pop(i)

    findEulerPath(key, value, currentList, 1, numOfRelations)

    key = backupKey[:]
    value = backupValue[:]
    # print backupKey
    # print backupValue