<pre>
<code>
<pre>
<code>
Dic_meta = {}
db = []
a = []
with open("/home/jjpark/as_db_compare/meta_405.txt") as p:
    lones = p.readlines()
    for lone in lones:
        lone = lone.rstrip()
        Dic_meta[lone.split('\t')[-1]] = lone.split('\t')[0]
with open("/home/jjpark/as_db_compare/405_gbff.txt") as f:
    lines = f.readlines()
    name = []
    nucl_start = []
    nucl_end = []
    region = []
    NZs =[]
    for line in lines:
        line = line.rstrip()
        name.append(Dic_meta[line.split('_')[0]][:-7]+'bgc.gbk')
        NZs.append(line.split('_')[1]+'_'+line.split('_')[2])
        nucl_start.append(line.split('_')[3][:-2].split('-')[0])
        nucl_end.append(line.split('_')[3][:-2].split('-')[1])
    for i in range(len(name)):
        db.append([name[i],NZs[i],nucl_start[i],nucl_end[i],[]])
genomes = []
for n in range(len(db)):
    genomes.append(db[n][0])
genomes=list(set(genomes))
Dic_bgc_gene = {}
for i in range(len(genomes)):
    with open('/home/jjpark/as_db_compare/bgc_gbk/%s'%genomes[i]) as s:
        ls = s.readlines()
        accession = [] 
        accession_line = []
        locustags = []
        for line in ls:
            line = line.lstrip()
            if line.startswith('ACCESSION'): 
                accession_line.append(ls.index(line))
                accession_line.sort()
            if line.startswith('gene  '): 
                n = ls.index('     '+str(line))
                loctag = ls.index(''.join([s for s in ls[n+1:n+3] if '/locus_tag=' in s]))
                locustags.append(loctag)
        last_gene_cluster = []
        lgc_lct = []
        for m in locustags:
            if int(m)>accession_line[-1]:
                last_gene_cluster.append(int(m))
        for w in last_gene_cluster:
            lgc_lct.append(ls[w].split('"')[-2])
        Dic_bgc_gene[ls[int(accession_line[-1])][12:-3]] = lgc_lct
        for acs in accession_line[:-1]:#accession_line이 1개의 BGC가 될 것 
            gene_cluster = []
            for k in locustags:#locustag들은 locusgene있는 line들
                if int(k) > int(acs):
                    if int(k) < int(accession_line[accession_line.index(acs)+1]):
                        gene_cluster.append(ls[int(k)].split('"')[-2])
                    else:
                        pass
                else:
                    pass
            Dic_bgc_gene[ls[int(acs)][12:-3]] = gene_cluster
for k,v in Dic_bgc_gene.items():
    print(k,v)
</code>
</pre>
</code>
</pre>
