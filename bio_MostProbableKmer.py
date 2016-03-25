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

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_159_3.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    Text = iF.readline().strip('\n')
    k = int(iF.readline().strip('\n'))

    probabilities = []
    for i in xrange(4):
        probabilities.append([])

    nucleotides = ['A', 'C', 'G', 'T']
    dictlist = [dict() for x in range(k)]
    for i in nucleotides:
        input = iF.readline().strip('\n').split(' ')
        for j in xrange(k):
            dictlist[j].update({i:input[j]})

    print MostProbableKmer(Text, k, dictlist)