#with open('bioinformatics_in.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
#with open('dataset_198_3.txt') as iF, open('bioinformatics_out.txt', 'w+') as oF:
kmers = []
while True:
    try:
        s = input()
        kmers.append(s)
    except:
        break
# while True:
#     enter = input()
#     if not enter:
#         break
#     kmers.append(enter)

dna = kmers[0]
for i in range(1, len(kmers)):
    dna += kmers[i][len(kmers[i])-1]
    #print dna

print (dna)
