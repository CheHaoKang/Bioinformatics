kmers = []
deBruijn = {}
while True:
    try:
        enter = input()
        if enter[:len(enter)-1] not in deBruijn:
            deBruijn[enter[:len(enter)-1]] = [enter[1:len(enter)]]
        else:
            deBruijn[enter[:len(enter)-1]].append(enter[1:len(enter)])
    except:
        break

for i in deBruijn:
    rightSide = ""
    for j in deBruijn[i]:
        rightSide +=  j + ','
    print ("%s -> %s" % (i, rightSide[:-1]))