with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
#with open('dataset_197_3.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:

    k = int(iF.readline().strip('\n'))
    string = iF.readline().strip('\n')

    kmers = []
    for i in xrange(len(string)-k+1):
        kmers.append(string[i:i+k])

    kmers.sort();
    for i in kmers:
        print i