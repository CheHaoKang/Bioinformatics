#delimiter = ','
#mylist = ['Brazil', 'Russia', 'India', 'China']
#print delimiter.join(mylist)

pairs = []
match = False
with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    d = 1
    input = iF.readline().strip('\n')
    input = input[1:-1]
    k = input.index('|') #k-mer
    input = input.replace('|', 'X')
    pairs.append(input)
    pairLen = len(input)
    #print input[-pairLen+1:]

    while True:
        input = iF.readline().strip('\n')
        if not input:
            break
        input = input.replace('|', 'X')
        pairs.append(input[1:-1])
        #print input
    #print pairs
    totalCount = len(pairs)
    nowCount = 1
    genome = pairs[0]
    #tmpStr = ''
    #print pairs[0][0:-1]
    #for tmpStr in pairs[0]:
    #    print tmpStr
    # for tmpStr in pairs[0][:-1]:
    #     print tmpStr
    while nowCount != totalCount:
        for i in xrange(1, totalCount):
            if pairs[i] != '':
                match = True

                for j in xrange(pairLen-1):
                    if (pairs[i][j] != genome[-pairLen+1+j]) and (pairs[i][j] != 'X' and genome[-pairLen+1+j] != 'X'):
                        match = False
                        break

                print "aaa", genome
                if match == True:
                    print "First Original genome:", genome
                    genomeLen = len(genome)
                    for j in xrange(pairLen-1):
                        if genome[-pairLen+1+j] == 'X' and pairs[i][j] != 'X':
                            tmpList = list(genome)
                            tmpList[genomeLen-pairLen+1+j] = pairs[i][j]
                            genome = ''.join(tmpList)
                            #genome[-pairLen+1+j] = pairs[i][j]
                    genome += pairs[i][-1]
                    # tmpList = list(genome)
                    # tmpList[genomeLen-pairLen+1+j] = pairs[i][j]
                    # genome = ''.join(tmpList)
                    print pairs[i]
                    pairs[i] = ''
                    nowCount += 1
                    print "First genome:", genome
                    break
                else:
                    match = True
                    for j in xrange(1, pairLen):
                        if (pairs[i][j] != genome[j-1]) and (pairs[i][j] != 'X' and genome[j-1] != 'X'):
                            match = False
                            break

                    if match == True:
                        print "Second genome:", genome
                        genomeLen = len(genome)
                        for j in xrange(1, pairLen):
                            if genome[j-1] == 'X' and pairs[i][j] != 'X':
                                tmpList = list(genome)
                                tmpList[j-1] = pairs[i][j]
                                genome = ''.join(tmpList)
                            #genome[-pairLen+1+j] = pairs[i][j]
                        tmpGenome = genome
                        genome = ''
                        genome += pairs[i][0]
                        print "pair:", pairs[i]
                        print genome
                        genome += tmpGenome
                        print "Second ----genome:", genome
                        pairs[i] = ''
                        nowCount += 1

    print "\nFinal Genome:", genome