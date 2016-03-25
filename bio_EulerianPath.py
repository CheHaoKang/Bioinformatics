def checkUnbalancedNode(key, value):
    inCount = {}
    outCount = {}
    inEdgeLess = -1
    outEdgeLess = -1

    for i in xrange(len(key)):
        if key[i] not in outCount:
            outCount[key[i]] = 1
        else:
            outCount[key[i]] += 1

        if value[i] not in inCount:
            inCount[value[i]] = 1
        else:
            inCount[value[i]] += 1

    #print "inCount, outCount"
    for key, value in inCount.iteritems():
        # print key, value,
        # if key not in outCount:
        #     print "0",
        # else:
        #     print outCount[key]
        if key not in outCount:
            print key + " in inCount NOT in outCount"
            outEdgeLess = key
    print "======================"
    for key, value in outCount.iteritems():
        # print key,
        # if key not in inCount:
        #     print "0",
        # else:
        #     print inCount[key],
        # print value
        if key not in inCount:
            print key + " in outCount NOT in inCount"
            inEdgeLess = key

    #return

    print key
    print value
    print inCount
    print outCount

    for key, value in inCount.iteritems():
        if key in outCount:
            if outCount[key] < value:
                outEdgeLess = key
            if outCount[key] > value:
                inEdgeLess = key
        else:
            outEdgeLess = key

    print "outEdgeLess: " + str(outEdgeLess)
    print "inEdgeLess: " + str(inEdgeLess)
    return inEdgeLess, outEdgeLess

def findEulerPath(key, value):
    inEdgeLess, outEdgeLess = checkUnbalancedNode(key, value)
    print "findEulerPath: " + str(inEdgeLess), str(outEdgeLess)
    key.append(outEdgeLess)
    value.append(inEdgeLess)

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

        # print "++++++++"
        # print currentCycle
        # print key
        # print value
        # print "-----------"

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

        #print currentCycle

    print "======answer======="
    # output = ""
    # for i in xrange(len(currentCycle)-1):
    #     output += (currentCycle[i] + "->")
    # print ("%s%s" % (output, currentCycle[-1]))

    for i in xrange(len(currentCycle)):
        if currentCycle[i] == outEdgeLess:
            currentCycle = currentCycle[i+1:] + currentCycle[1:i+1]
            break

    output = ""
    for i in xrange(len(currentCycle)-1):
        output += (currentCycle[i] + "->")
    print ("%s%s" % (output, currentCycle[-1]))

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_203_5.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    '''
    edges = {}
    for edge in [line.strip().split(' -> ') for line in iF.readlines()]:
        if ',' in edge[1]:
            edges[int(edge[0])] = map(int,edge[1].split(','))
        else:
            edges[int(edge[0])] = [int(edge[1])]

    print edges
    # Determine the unbalanced edges.
    out_values = reduce(lambda a,b: a+b, edges.values())
    for node in set(out_values+edges.keys()):
        out_value = out_values.count(node)
        if node in edges:
            in_value = len(edges[node])
        else:
            in_value = 0

        if in_value < out_value:
            unbalanced_from = node
        elif out_value < in_value:
            unbalanced_to = node
    print unbalanced_from, unbalanced_to
    print "____________________"
    '''
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

    # for i in xrange(len(key)):
    #     print key[i] + "->" + value[i]

    #checkUnbalancedNode(key, value)
    findEulerPath(key, value)