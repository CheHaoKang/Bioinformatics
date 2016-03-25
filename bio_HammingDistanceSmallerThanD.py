def HammingDistance(Genome1, Genome2):
    count = 0
    for i in xrange(len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count

"""
#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_9_4.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    pattern = iF.readline().strip('\n')
    genome = iF.readline().strip('\n')
    d = int(iF.readline().strip('\n'))

    index = []
    for i in xrange(len(genome)-len(pattern)+1):
        count = HammingDistance(pattern, genome[i:i+len(pattern)])
        if count <= d:
            index.append(i)

    for i in index:
        print i,
"""