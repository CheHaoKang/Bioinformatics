with open('dataset_2_6.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    #iF.readline().strip('\n')
    genome = iF.readline().strip('\n')
    pattern = iF.readline().strip('\n')

    #genome = "GCGCG"
    #pattern = "GCG"

    count = 0
    for i in xrange(len(genome)-len(pattern)+1):
        found = True
        #print "+++"
        for j in xrange(i, i+len(pattern)):
            #print j, j-i
            if genome[j] != pattern[j-i]:
                found = False
                break
        if found == True:
            count += 1
        #print "---"

    print count
    #print genome
    #print pattern

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
