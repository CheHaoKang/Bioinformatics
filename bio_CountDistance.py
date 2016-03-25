with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    numStrings, numKmers = iF.readline().split(' ')
    numStrings = int(numStrings)
    numKmers = int(numKmers)

    strings = []
    for i in xrange(numStrings):
        strings.append(iF.readline().strip('\n'))
        #print strings

    kmers = []
    for i in xrange(numKmers):
        kmers.append(iF.readline().strip('\n'))
        #print kmers

    #print len(strings[0])
    #print len(kmers[0])
    distance = 0
    k = 0
    minimum = 100000
    sumList = []
    sum = 0
    for m in xrange(numKmers):
        sum = 0
        for p in xrange(numStrings):
            minimum = 100000
            for i in xrange(len(strings[p])-len(kmers[m])+1):
                distance = 0
                k = 0
                for j in xrange(i, i+len(kmers[m])):
                    if strings[p][j] != kmers[m][k]:
                        distance += 1
                    k += 1
                if distance < minimum:
                    minimum = distance
            sum += minimum
        sumList.append(sum)

    print sumList
    # whi
    # input = iF.readline().strip('\n')
    # input = input[1:-1]
    # k = input.index('|') #k-mer
    # input = input.replace('|', 'X')
    # pairs.append(input)
    # pairLen = len(input)
    #print input[-pairLen+1:]


        #print input
        # input = input.replace('|', 'X')
        # pairs.append(input[1:-1])
        #print input
