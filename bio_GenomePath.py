#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_198_3.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    kmers = []
    while True:
        input = iF.readline().strip('\n')
        if not input:
            break
        kmers.append(input)

    dna = kmers[0]
    for i in xrange(1, len(kmers)):
        dna += kmers[i][len(kmers[i])-1]
        #print dna

    print dna
