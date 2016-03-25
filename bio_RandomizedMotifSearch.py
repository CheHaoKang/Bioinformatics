import random

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

    print nucleotidesDict
    return nucleotidesDict

def GreedyMotifSearch(strings, k, t):
    BestMotifs = []
    for i in xrange(t):
        BestMotifs.append(strings[i][0:k])

    #print BestMotifs, Score(BestMotifs, Profile(BestMotifs))

    for i in xrange(len(strings[0])-k+1):
        motifs = []
        motifs.append(strings[0][i:i+k])
        for j in xrange(1, t):
            newKmer = MostProbableKmer(strings[j], k, Profile(motifs))
            motifs.append(newKmer)

        if Score(motifs, Profile(motifs)) < Score(BestMotifs, Profile(BestMotifs)):
            BestMotifs = motifs

    return BestMotifs

def randomKmerSelection(k, t, strings):
    motifs = []
    for i in xrange(t):
        position = random.randint(0, len(strings[0])-k)
        motifs.append(strings[i][position:position+k])
    return motifs

def RandomizedMotifSearch(k, t, strings):
    BestMotifs = randomKmerSelection(k, t, strings)
    initialMotifs = randomKmerSelection(k, t, strings)

    while True:
        motifs = []
        for j in xrange(t):
            newKmer = MostProbableKmer(strings[j], k, Profile(initialMotifs))
            motifs.append(newKmer)

        if Score(motifs, Profile(motifs)) < Score(BestMotifs, Profile(BestMotifs)):
            BestMotifs = motifs
            initialMotifs = motifs
        else:
            return BestMotifs
    #return BestMotifs

def TimesRandomizedMotifSearch(k, t, strings, times):
    lowestBestscore = float('inf')
    lowestMotifs = []
    i = 0
    while True:
        bestMotifs = RandomizedMotifSearch(k, t, strings)
        bestScore = Score(bestMotifs, Profile(bestMotifs))
        if bestScore < lowestBestscore:
            lowestBestscore = bestScore
            lowestMotifs = bestMotifs
            i = 0
        else:
            i += 1
        if i > times:
            break

    return lowestMotifs

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_161_5.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    input = iF.readline().strip('\n').split(' ')
    k = int(input[0])
    t = int(input[1])
    strings = []
    for i in xrange(t):
        strings.append(iF.readline().strip('\n'))

    lowestMotifs = TimesRandomizedMotifSearch(k, t, strings, 1000)

    #print lowestMotifs
    for i in lowestMotifs:
        print i
