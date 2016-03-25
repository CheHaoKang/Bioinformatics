def StringReconstruction(kmers, currentString, now, numOfKmers):
    if now == numOfKmers:
        print ("%s" % (currentString))
        return
    if not kmers:
        return

    backupKmers = kmers[:]
    backupCurrentString = currentString
    # print kmers[0]
    # print kmers[0][:len(kmers[0])-1]
    # print
    for i in xrange(len(kmers)):
        if currentString[1-len(kmers[0]):] == kmers[i][:len(kmers[0])-1]:
            # print ("key:")
            # print (key)
            # print ("value:")
            # print (value)
            # print ("backupKey:")
            # print (backupKey)
            # print ("backupValue:")
            # print (backupValue)
            currentString += kmers[i][-1]
            kmers.pop(i)
            # print ("After appenindg:")
            # print (currentList)
            # print ("Remove key:")
            # print (key)
            # print ("Remove value:")
            # print (value)
            now += 1

            StringReconstruction(kmers, currentString, now, numOfKmers)

            kmers = backupKmers[:]
            currentString = backupCurrentString
            now -= 1

    # currentString += (kmers[-1][-1])
    # print currentString

    # print "++++++++++++"
    # print "backupCurrentString:" + backupCurrentString
    # print "currentString:" + currentString
    #
    # currentString = "aaa"
    #
    # print
    # print "backupCurrentString:" + backupCurrentString
    # print "currentString:" + currentString
    # print "-----------------"

with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    k = int(iF.readline().strip('\n'))
    kmers = []
    # adjacentList = {}
    # key = []
    # value = []
    while True:
        input = iF.readline().strip('\n')
        if not input:
            break
        kmers.append(input)

    numOfKmers = len(kmers)
    backupKmers = kmers[:]
    for i in range(len(kmers)):
        currentString = kmers[i]
        kmers.pop(i)

        StringReconstruction(kmers, currentString, 1, numOfKmers)

        kmers = backupKmers[:]