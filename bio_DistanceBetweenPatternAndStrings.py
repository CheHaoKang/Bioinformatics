import sys

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

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_5164_1.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    Dna = []
    Pattern = iF.readline().strip('\n')
    Dna = iF.readline().split(' ')

    print DistanceBetweenPatternAndStrings(Pattern, Dna)