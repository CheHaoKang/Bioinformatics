def checkFinished(CurrentString):
#    print "+++++++++++++++++++"
    backupKmers = kmers[:]
 #   print "CurrentString:" + CurrentString
    for i in range(len(CurrentString)-k+1):
        delete = []
        for j in range(len(backupKmers)):
            if CurrentString[i:i+k] == backupKmers[j]:
  #              print "CurrentString[i:i+k]:" + CurrentString[i:i+k]
   #             print "backupKmers[j]:" + backupKmers[j]
                delete.append(j)
        for index in delete:
            backupKmers.pop(index)
    #print backupKmers
    #print "----------------------------"
    if not backupKmers:
        return True
    else:
        return False

def checkCircularString(kmers, currentString):
    k = len(kmers[0])
    testCurrentString = currentString[1-k:] + currentString[:k-1]
    backupKmers = kmers[:]
    #print "currentString:" + currentString
    #print "testCurrentString:" + testCurrentString
    for i in range(len(testCurrentString)-k+1):
        #print "testCurrentString[i:i+k]:" + testCurrentString[i:i+k]
        delete = []
        for j in range(len(backupKmers)):
            if testCurrentString[i:i+k] == backupKmers[j]:
                delete.append(j)
        for ele in delete:
            backupKmers.pop(ele)
    if not backupKmers:
        return True
    else:
        return False

def StringReconstruction(kmers, currentString):
    # if now == numOfKmers:
    #     print ("%s" % (currentString))
    #     return
    if not kmers:
        return

    #print "currentString:" + currentString
    k = len(kmers[0])
    backupKmers = kmers[:]
    backupCurrentString = currentString
    for i in range(len(kmers)):
        if currentString[1-k:] == kmers[i][:k-1]:
            currentString += kmers[i][-1]
            kmers.pop(i)

            # print "++++"
            # print kmers
            # print currentString
            if len(kmers) == k-1:
                result = checkCircularString(kmers, currentString)

                if result == True:
                    #if checkFinished(currentString):
                    print currentString
                    return
                else:
                    return
            # print kmers
            # print currentString
            # print "-----"
            StringReconstruction(kmers, currentString)

            kmers = backupKmers[:]
            currentString = backupCurrentString

with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    # k = 4
    # test = "0000100110101111"
    # test += test[:k-1]
    # print test
    # for i in range(len(test)-k+1):
    #     print test[i:i+k]
    k = int(iF.readline().strip('\n'))

    kmers = []
    kmers.append("".zfill(k))

    num = 1
    while num < 2**k:
        kmers.append(bin(num)[2:].zfill(k))
        num += 1

    refKmers = kmers[:]
    print refKmers

    currentString = kmers[0]
    kmers.pop(0)
    StringReconstruction(kmers, currentString)