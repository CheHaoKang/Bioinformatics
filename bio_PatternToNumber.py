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

with open('dataset_3010_2.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    genome = iF.readline().strip('\n')
    print PatternToNumber(genome)