#homework assignment to parse genes of a Ensembl file completed Fall 2018
#Claire Menard
#


ensGeneDict = {}
refGeneDict = {}
def parserEnsRef(inEns, inRef): 
    infileEns = open(inEns)
    for line in infileEns.readlines():
        line=line.rstrip()
        if line.startswith('ENSG'):
            parts= line.split('\t')
            ensGene = parts[0]
            id = parts[4]
            ensGeneDict[id] = ensGene
    infileEns.close()

    infileRef = open(inRef)
    for line in infileRef.readlines():
        line=line.rstrip()
        if line.startswith('RefSeq'):
            continue
        else:
            parts= line.split('\t')
            refGene = parts[0]
            id = parts[1]
            refGeneDescription = parts[2]
            refGeneInfo = refGene + ',' + refGeneDescription
            refGeneDict[id] = refGeneInfo
    infileRef.close()

    outfile = open('gene.csv', 'w')
    for id in ensGeneDict:
        ens = ensGeneDict[id]
        ref = refGeneDict[id]
        lineOut = ens + ',' + ref + '\n'
        outfile.write(lineOut)
    outfile.close()

parserEnsRef('Ensembl.txt', 'RefSeq.txt')
