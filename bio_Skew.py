import sys

def Skew(Genome):
    SkewNum = []
    SkewNum.append(0)
    count = 0

    for i in Genome:
        if i == 'C':
            count -= 1
            SkewNum.append(count)
        elif i == 'G':
            count += 1
            SkewNum.append(count)
        else:
            SkewNum.append(count)

    return SkewNum

#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('Salmonella_enterica.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    genome = []

    while True:
        line = iF.readline().strip('\n')
        if not line: break
        genome.append(line)
    genome = ''.join(genome)
    #print genome
    oF.write(genome[3764355:3765355])

    SkewNum = Skew(genome)

    minimum = sys.maxint
    for i in SkewNum:
        if i < minimum:
            minimum = i

    index = 0
    for i in SkewNum:
        if i == minimum:
            print index,
        index += 1