# s = "string"
# s = "".join((lambda x:(x.sort(),x)[1]) (list(s)))
# print s
# print (lambda x:(x.sort(), x)[1]) (list(s))

with open('dataset_2_9.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    #iF.readline().strip('\n')
    genome = iF.readline().strip('\n')
    k = int(iF.readline().strip('\n'))

    #pattern = "GCG"

    kmers = []
    # kmers.append([])
    # kmers[0].append("AGCT")
    # kmers[0].append(4)
    #
    # print len(kmers)
    # print len(kmers[0][0])
    # print kmers[0][1]

    maxCount = -1
    for i in xrange(len(genome)-k+1):
        kmer = genome[i:i+k]

        same = False
        for j in xrange(len(kmers)):
            if kmers[j][0] == kmer:
                same = True
                break
        if same == True:
            continue

        count = 1
        for j in xrange(i+1, len(genome)-k+1):
            tmp = genome[j:j+k]
            if tmp == kmer:
                count += 1

        if count > maxCount:
            maxCount = count

        kmers.append([])
        kmers[len(kmers)-1].append(kmer)
        kmers[len(kmers)-1].append(count)
        #print kmer
    #print genome
    #print pattern
    longestKmers = []
    for j in xrange(len(kmers)):
        if kmers[j][1] == maxCount:
            longestKmers.append(kmers[j][0])

    #print longestKmers
    for i in xrange(len(longestKmers)-1):
        for j in xrange(i, len(longestKmers)):
            if longestKmers[i] > longestKmers[j]:
                tmp = longestKmers[j]
                longestKmers[j] = longestKmers[i]
                longestKmers[i] = tmp
    print longestKmers
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
