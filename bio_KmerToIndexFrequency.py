def generateKmers(i, n, kmer):
    global index
    if i == n:
        kmerToIndex[kmer] = index
        index += 1
        return

    generateKmers(i+1, n, kmer+'A')
    generateKmers(i+1, n, kmer+'C')
    generateKmers(i+1, n, kmer+'G')
    generateKmers(i+1, n, kmer+'T')

with open('dataset_2994_5.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    genome = iF.readline().strip('\n')
    k = int(iF.readline().strip('\n'))

    index = 0
    kmerToIndex = {}
    generateKmers(1, k, 'A')
    generateKmers(1, k, 'C')
    generateKmers(1, k, 'G')
    generateKmers(1, k, 'T')

    num = 1
    for i in xrange(k):
        num *= 4

    frequency = []
    for i in xrange(num):
        frequency.append(0)

    for i in xrange(len(genome)-k+1):
        kmer = genome[i:i+k]
        frequency[kmerToIndex[kmer]] += 1

    for i in frequency:
        print i,