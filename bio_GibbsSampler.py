import random
import numpy as np
from scipy import stats

def Score(motifs, profile):
    nucleotides = ['C', 'G', 'T']
    Consensus = []

    for i in xrange(len(motifs[0])):
        highest = 'A'
        highestPro = profile[i]['A']
        for j in nucleotides:
            if profile[i][j] > highestPro:
                highest = j
                highestPro = profile[i][j]
        Consensus.append(highest)

    score = 0
    for i in motifs:
        distance = 0
        for j in xrange(len(i)):
            if i[j] != Consensus[j]:
                distance += 1
        score += distance

    return score

def MostProbableKmer(Text, k, Profile):
    mostProbableKmer = ""
    mostProbableChance = -1
    for i in xrange(len(Text)-k+1):
        probability = 1
        for j in xrange(k):
            probability *= float(Profile[j][Text[i+j]])
        if probability > mostProbableChance:
            mostProbableChance = probability
            mostProbableKmer = Text[i:i+k]

    return mostProbableKmer

def Profile(motifs):
    nucleotides = ['A', 'C', 'G', 'T']
    nucleotidesDict = [dict() for x in range(len(motifs[0]))]
    for i in xrange((len(motifs[0]))):
        for j in nucleotides:
            nucleotidesDict[i].update({j:1})

    for i in xrange((len(motifs[0]))):
        for j in xrange(len(motifs)):
            nucleotidesDict[i][motifs[j][i]] += 1
        for j in nucleotides:
            nucleotidesDict[i][j] = float(nucleotidesDict[i][j]) / float(len(motifs)+4)

    #print nucleotidesDict
    return nucleotidesDict

def randomKmerSelection(k, t, dna):
    motifs = []
    for i in xrange(t):
        position = random.randint(0, len(dna[0])-k)
        motifs.append(dna[i][position:position+k])
    return motifs

def prgkst(kmers, probabilities):
    s = sum(probabilities)
    probabilities = map(lambda x: x/float(s), probabilities)
    #print probabilities
    l = len(probabilities)
    xk = np.arange(l)
    custm = stats.rv_discrete(name='custm',values=(xk, probabilities))
    R = custm.rvs(size=1)
    index = R[0]
    return kmers[index]

def GibbsSampler(k, t, N, dna):
    bestMotifs = randomKmerSelection(k, t, dna)
    motifs = randomKmerSelection(k, t, dna)

    for j in xrange(N):
        i = random.randint(0, t-1)
        #motifs = randomKmerSelection(k, t, N, dna)
        motifs.pop(i)

        profileDic = Profile(motifs)
        possibilities = []
        kmers = []
        #bestProbability = -1.0
        #bestKmer = ""
        for p in xrange(len(dna[i])-k+1):
            probability = 1
            for q in xrange(p, p+k):
                probability *= profileDic[q-p][dna[i][q]]

            # if probability > bestProbability:
            #     bestProbability = probability
            #     bestKmer = dna[i][p:p+k]
            possibilities.append(probability)
            kmers.append(dna[i][p:p+k])
            #possibleKmers[dna[i][p:p+k]] = probability # Just do it in advance (not used)

        motifs.insert(i, prgkst(kmers, possibilities))
        if Score(motifs, Profile(motifs)) < Score(bestMotifs, Profile(bestMotifs)):
            bestMotifs = motifs

    return bestMotifs, Score(bestMotifs, Profile(bestMotifs))

def RandomStartGibbsSampler(k, t, N, dna):
    if N > 1000:
        N = 1000
    lowest_bestscore = float('inf')
    lowest_motifs = []

    i = 0
    while True:
        # print 'i: '+str(i)
        # print 'lowest_bestscore: ' + str(lowest_bestscore)
        # print 'lowest_motifs: ' + str(lowest_motifs)
        bestmotifs,bestscore = GibbsSampler(k,t,N, dna)
        if bestscore < lowest_bestscore:
            lowest_bestscore = bestscore
            lowest_motifs = bestmotifs
            i = 0
        else:
            i += 1
        if i == 20:
            break
    return lowest_motifs

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_163_4.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    input = iF.readline().strip('\n').split(' ')
    k = int(input[0])
    t = int(input[1])
    N = int(input[2])
    dna = []
    for i in xrange(t):
        dna.append(iF.readline().strip('\n'))

    result = RandomStartGibbsSampler(k, t, N, dna)
    for motif in result:
        print motif