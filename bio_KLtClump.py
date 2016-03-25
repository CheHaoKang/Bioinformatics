import time

with open('dataset_4_5.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    tStart = time.time()

    genome = iF.readline().strip('\n')
    k, l, t = iF.readline().split(' ')
    k = int(k)
    l = int(l)
    t = int(t)

    kmers = []
    for i in xrange(len(genome)-l+1):
        for j in xrange(i, i+l-k*t+1):
            kmer = genome[j:j+k]
            if kmers.count(kmer) > 0:
                continue

            count = 1
            for p in xrange(j+k, i+l-k+1):
                tmp = genome[p:p+k]
                if kmer == tmp:
                    count += 1
            if count == t and kmers.count(kmer) == 0:
                kmers.append(kmer)
    for i in kmers:
        print i,

    tEnd = time.time()
    print "Time usage:", float(tEnd-tStart)/60.0