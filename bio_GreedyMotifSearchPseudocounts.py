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

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_160_9.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    input = iF.readline().strip('\n').split(' ')
    k = int(input[0])
    t = int(input[1])
    strings = []
    for i in xrange(t):
        strings.append(iF.readline().strip('\n'))

    BestMotifs = GreedyMotifSearch(strings, k, t)
    for i in BestMotifs:
        print i
    # for i in xrange(len(strings[0])-k+1):
    #     for j in xrange(len(strings[0])-k+1):
    #         for q in xrange(len(strings[0])-k+1):