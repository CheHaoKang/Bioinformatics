"""
1. A collection of strings with (k, d)
2. find all k-mers with at most d mutations so that each this kind of k-mers appears in every string

https://stepic.org/lesson/Motif-Finding-Is-More-Difficult-Than-You-Think-156/step/7?unit=undefined
Sample Input:
     3 1
     ATTTGGC
     TGCCTTA
     CGGTATC
     GAAAATT

Sample Output:
     ATA ATT GTT TTT
"""

from bio_NeighborsWithDistanceD import Neighbors
from bio_HammingDistanceSmallerThanD import HammingDistance

def MOTIFENUMERATION(Dna, k, d):
    patterns = []
    for i in xrange(len(Dna[0])-k+1):
        pattern = Dna[0][i:i+k]
        Neighborhood = Neighbors(pattern, d)

        for j in Neighborhood:
            #if j == "ATT":
            #    print j
            everyoneHas = True
            for r in xrange(1, len(Dna)):
                found = False
                for p in xrange(len(Dna[r])-len(j)+1):
                    genome1 = Dna[r][p:p+len(j)]
                    #print "genome1:", genome1
                    if HammingDistance(genome1, j) <= d:
                        found = True
                        break
                    #genome2 = Dna[k][p:p+k]
                    # for q in xrange(p, p+len(j)):
                    #      if Dna[k][q] != j[q-p]:
                    #         found = False
                    #         break

                if found == False:
                    everyoneHas = False
                    break
            if everyoneHas == True:
                same = False
                for tmp in patterns:
                    if tmp == j:
                        same = True
                        break
                if same == False:
                    patterns.append(j)

    return patterns

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_156_7.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    k, d = iF.readline().split(' ')
    k = int(k)
    d = int(d)

    genomes = []
    while True:
        line = iF.readline().strip('\n')
        if not line: break
        genomes.append(line)

    patterns = MOTIFENUMERATION(genomes, k, d)
    for i in patterns:
        print i,
