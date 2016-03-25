import time

def SymbolToNumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3

def PatternToNumber(pattern):
    if pattern=='':
        return 0

    symbol = pattern[-1]
    prefix = pattern[0:-1]
    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)

def NumberToSymbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)

    preIndex = int(index / 4)
    symbol = NumberToSymbol(index % 4)
    prefixPattern = NumberToPattern(preIndex, k-1)

    return prefixPattern + symbol

def ComputingFrequencies(Text , k):
    num = 1
    for i in xrange(k):
        num *= 4

    frequencyArray = []
    for i in xrange(num):
        frequencyArray.append(0)

    for i in xrange(len(Text)-k+1):
        pattern = Text[i:i+k]
        j = PatternToNumber(pattern)
        frequencyArray[j] = frequencyArray[j] + 1

    return frequencyArray

def BetterClumpFinding(Genome, k, t, L):
    FrequentPatterns = []

    num = 1
    for i in xrange(k):
        num *= 4

    Clump = []
    for i in xrange(num):
        Clump.append(0)

    Text = Genome[0:L]
    frequencyArray = []
    frequencyArray = ComputingFrequencies(Text, k)
    for i in xrange(num):
        if frequencyArray[i] >= t:
            Clump[i] = 1

    #print Genome[len(Genome)-L]
    for i in xrange(1, len(Genome)-L+1):
        FirstPattern = Genome[i-1:i-1+k]
        index = PatternToNumber(FirstPattern)
        frequencyArray[index] -= 1
        LastPattern = Genome[i+L-k:i+L]
        #print "FP: ", FirstPattern
        #print "LP:", LastPattern
        index = PatternToNumber(LastPattern)
        frequencyArray[index] += 1
        if frequencyArray[index] >= t:
            Clump[index] = 1

        for i in xrange(num):
            if Clump[i] == 1:
                Pattern = NumberToPattern(i, k)
                if FrequentPatterns.count(Pattern) == 0:
                    FrequentPatterns.append(Pattern)

    return FrequentPatterns


with open('dataset_4_5.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    tStart = time.time()

    genome = iF.readline().strip('\n')
    k, l, t = iF.readline().split(' ')
    k = int(k)
    l = int(l)
    t = int(t)

    frequentPatterns = BetterClumpFinding(genome, k, t, l)
    for i in frequentPatterns:
        print i,


    print
    tEnd = time.time()
    print "Time usage: ", float(tEnd-tStart) / 60.0