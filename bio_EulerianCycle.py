def checkUnbalancedNode(key, value):
    inCount = {}
    outCount = {}

    for i in xrange(len(key)):
        if key[i] not in outCount:
            outCount[key[i]] = 1
        else:
            outCount[key[i]] += 1

        if value[i] not in inCount:
            inCount[value[i]] = 1
        else:
            inCount[value[i]] += 1

    print key
    print value
    print inCount
    print outCount
    inEdgeLess = -1
    outEdgeLess = -1
    for key, value in inCount.iteritems():
        if key in outCount:
            if outCount[key] < value:
                outEdgeLess = key
            if outCount[key] > value:
                inEdgeLess = key
        else:
            outEdgeLess = key

    print "outEdgeLess: " + outEdgeLess
    print "inEdgeLess: " + inEdgeLess
    return inEdgeLess, outEdgeLess

def findEulerCycle(key, value):
    currentCycle = []
    currentCycle.append(key[0])
    currentCycle.append(value[0])
    key.pop(0)
    value.pop(0)

    print key
    print value
    print currentCycle
    print "=====before====="
    print

    while key:
        found = True
        while found:
            found = False
            for i in xrange(len(key)):
                if currentCycle[-1] == key[i]:
                    currentCycle.append(value[i])
                    key.pop(i)
                    value.pop(i)
                    found = True
                    break

        print "++++++++"
        print currentCycle
        print key
        print value
        print "-----------"

        if key:
            for i in xrange(1, len(currentCycle)-1):
                found = False
                for j in xrange(len(key)):
                    if currentCycle[i] == key[j]:
                        backupCurrentCycle = currentCycle[:]
                        currentCycle = backupCurrentCycle[i:len(backupCurrentCycle)] + backupCurrentCycle[1:i+1]
                        found = True
                        break

                if found:
                    break

        print currentCycle

    print "======answer======="
    output = ""
    for i in xrange(len(currentCycle)-1):
        output += (currentCycle[i] + "->")
    print ("%s%s" % (output, currentCycle[-1]))

with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
#with open('dataset_203_2.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
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

    # print key
    # print value

    #checkUnbalancedNode(key, value)
    findEulerCycle(key, value)