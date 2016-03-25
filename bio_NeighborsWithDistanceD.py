def HammingDistance(Genome1, Genome2):
    count = 0
    for i in xrange(len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count

def Neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    Neighborhood = []
    SuffixNeighbors = Neighbors(pattern[1:len(pattern)], d)
    for i in SuffixNeighbors:
        if HammingDistance(pattern[1:len(pattern)], i) < d:
            Neighborhood.append('A' + i)
            Neighborhood.append('C' + i)
            Neighborhood.append('G' + i)
            Neighborhood.append('T' + i)
        else:
            Neighborhood.append(pattern[0] + i)

    return Neighborhood

# with open('dataset_3014_3.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
# #with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
#     pattern = iF.readline().strip('\n')
#     d = int(iF.readline().strip('\n'))
#
#     #print pattern[1:len(pattern)]
#
#     Neighborhood = Neighbors(pattern, d)
#     for i in Neighborhood:
#         print i