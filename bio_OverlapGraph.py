#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_198_9.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    kmers = []
    while True:
        input = iF.readline().strip('\n')
        if not input:
            break
        kmers.append(input)

    for i in xrange(len(kmers)):
        for j in xrange(len(kmers)):
            if kmers[i] != kmers[j] and kmers[i][1:len(kmers[i])] == kmers[j][:len(kmers[j])-1]:
                print kmers[i] + " -> " + kmers[j]
            #if kmers[i][1:len(kmers[i])-1]