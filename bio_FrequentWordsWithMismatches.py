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

def HammingDistance(Genome1, Genome2):
    count = 0
    for i in xrange(len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count

def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in xrange(len(Text)-len(Pattern)+1):
        HD = HammingDistance(Pattern, Text[i:i+len(Pattern)])
        if HD <= d:
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

def ReverseComplement(Text):
    nucleotideMapping = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    complement = []
    for i in xrange(len(Text)):
        complement.append(nucleotideMapping[Text[i]])

    return ''.join(complement)

def FrequentWordsWithMismatches(Text, k ,d):
    FrequentPatterns = []
    num = 1
    for i in xrange(k):
        num *= 4

    Close = []
    ReverseClose = []
    FrequenyArray = []
    for i in xrange(num):
        Close.append(0)
        FrequenyArray.append(0)

    for i in xrange(len(Text)-k+1):
        Neighborhood = Neighbors(Text[i:i+k], d)
        for j in Neighborhood:
            index = PatternToNumber(j)
            Close[index] = 1

    maxCount = -100
    for i in xrange(num):
        if Close[i]==1:
            Pattern = NumberToPattern(i, k)
            #print "Text, Pattern, d: ", Text, Pattern, d
            FrequenyArray[i] = ApproximatePatternCount(Text, Pattern, d)
            #print "FrequencyArray: ", FrequenyArray[i]

            if FrequenyArray[i] > maxCount:
                maxCount = FrequenyArray[i]

    for i in xrange(num):
        if FrequenyArray[i] == maxCount:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)

    return FrequentPatterns

# Website : https://stepic.org/lesson/CS-Solving-the-Frequent-Words-with-Mismatches-Problem-3013/step/2?unit=undefined

with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
#with open('dataset_9_7.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    Text = iF.readline().strip('\n')
    k, d = iF.readline().split(' ')
    k = int(k)
    d = int(d)
    # Pattern = iF.readline().strip('\n')
    # Text = iF.readline().strip('\n')
    # d = iF.readline().strip('\n')
    # d = int(d)
    # print ApproximatePatternCount(Text, Pattern, d)

    words = FrequentWordsWithMismatches(Text, k, d)
    for i in words:
        print i,

    #print '\n', ReverseComplement("AGCTAG")