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

with open('dataset_2994_5.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    Text = iF.readline().strip('\n')
    k = int(iF.readline().strip('\n'))
    print ComputingFrequencies(Text, k)