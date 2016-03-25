#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
with open('dataset_199_6.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
    k = int(iF.readline().strip('\n'))
    text = iF.readline().strip('\n')

    deBruijn = {}
    for i in xrange(len(text)-(k-1)):
        if text[i:i+(k-1)] not in deBruijn:
            deBruijn[text[i:i+(k-1)]] = [text[i+1:i+1+(k-1)]]
        else:
            deBruijn[text[i:i+(k-1)]].append(text[i+1:i+1+(k-1)])

    for i in deBruijn:
        rightSide = ""
        for j in deBruijn[i]:
            rightSide +=  j + ','
        print i + ' -> ' + rightSide[:-1]

    # deBruijn['AGT'] = ['GTT', 'ATT']
    # deBruijn['AGT'].append('GGG')
    # print deBruijn['AGT']