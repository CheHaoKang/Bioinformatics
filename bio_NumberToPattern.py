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

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_3010_4.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    index = int(iF.readline().strip('\n'))
    k = int(iF.readline().strip('\n'))
    print NumberToPattern(index, k)