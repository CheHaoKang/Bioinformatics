import sys

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

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    sum = 0
    for Text in Dna:
        #print Text
        #print "Pattern: ", Pattern
        distance = sys.maxint
        for i in xrange(len(Text)-len(Pattern)+1):
            PatternPrime = Text[i:i+len(Pattern)]
            #print PatternPrime
            count = 0
            for j in xrange(len(Pattern)):
                if PatternPrime[j] != Pattern[j]:
                    count += 1

            if count < distance:
                distance = count

        sum += distance

    return sum

def MedianString(Dna, k):
    distance = sys.maxint
    for i in xrange(4**k):
        Pattern = NumberToPattern(i, k)
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern

    return Median

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_158_9.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    Dna = []
    k = int(iF.readline().strip('\n'))

    while True:
        line = iF.readline().strip('\n')
        if not line: break
        Dna.append(line)

    print k
    print Dna

    print MedianString(Dna, k)