kmers = []
while True:
    try:
        s = input()
        kmers.append(s)
    except:
        break

for i in range(len(kmers)):
    for j in range(len(kmers)):
        if kmers[i] != kmers[j] and kmers[i][1:len(kmers[i])] == kmers[j][:len(kmers[j])-1]:
            print ("%s -> %s" % (kmers[i], kmers[j]))
        #if kmers[i][1:len(kmers[i])-1]