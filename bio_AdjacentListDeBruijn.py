#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_200_7.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    kmers = []
    deBruijn = {}
    while True:
        input = iF.readline().strip('\n')
        if not input:
            break
        if input[:len(input)-1] not in deBruijn:
            deBruijn[input[:len(input)-1]] = [input[1:len(input)]]
        else:
            deBruijn[input[:len(input)-1]].append(input[1:len(input)])

    for i in deBruijn:
        rightSide = ""
        for j in deBruijn[i]:
            rightSide +=  j + ','
        print i + ' -> ' + rightSide[:-1]