def findEulerCycle(key, value, currentList, now, numOfRelations):
    global printOnce

    # print
    # print ("currentList:")
    # print currentList

    if now == numOfRelations:
        output = ""
        if printOnce == False:
            for i in xrange(len(currentList)-1):
                output += (currentList[i] + "->")
            print ("%s%s" % (output, currentList[-1]))
            #printOnce = True
        return
    if not key:
        return

    backupKey = key[:]
    backupValue = value[:]
    backupCurrentList = currentList[:]
    for i in xrange(len(key)):
        if currentList[-1] == key[i]:
            # print ("key:")
            # print (key)
            # print ("value:")
            # print (value)
            # print ("backupKey:")
            # print (backupKey)
            # print ("backupValue:")
            # print (backupValue)
            currentList.append(value[i])
            key.pop(i)
            value.pop(i)
            # print ("After appenindg:")
            # print (currentList)
            # print ("Remove key:")
            # print (key)
            # print ("Remove value:")
            # print (value)
            now += 1

            findEulerCycle(key, value, currentList, now, numOfRelations)

            key = backupKey[:]
            value = backupValue[:]
            currentList = backupCurrentList[:]
            now -= 1

with open('dataset_203_2.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    printOnce = False
    adjacentList = {}
    key = []
    value = []
    while True:
        input = iF.readline().strip('\n')
        if not input:
            break
        splitString = input.replace(' ', '').split("->")
        for each in splitString[1].split(','):
            #print splitString[0], each
            key.append(splitString[0])
            value.append(each)

    numOfRelations = len(key)
    backupKey = key[:]
    backupValue = value[:]
    # for i in xrange(len(key)):
    #     backupKey.append(key[i])
    #     backupValue.append(value[i])
    # print backupKey
    # print backupValue

    for i in xrange(len(key)):
        currentList = []
        currentList.append(key[i])
        currentList.append(value[i])
        key.pop(i)
        value.pop(i)

        findEulerCycle(key, value, currentList, 1, numOfRelations)

        key = backupKey[:]
        value = backupValue[:]
        # print backupKey
        # print backupValue