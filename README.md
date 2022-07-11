# Antismash-DeepBGC(gbff)
## 1. gbff파일을 DeepBGC 프로그램 사용의 결과물과 Antismash 결과 비교를 위한 Antismash 옵션 탐색
사용하는 Antismash 옵션은 아래와 같다. 
<pre>
<code>
antismash --output-dir --hmmdetection-strictness loose --asf --pfam2go --rre --clusterhmmer
</code>
</pre>
이 중, DeepBGC의 결과물에 대한 비교 분석을 위해 hmmdetection strictness의 loose/relaxed와 clusterhmmer/fullhmmer 옵션의 선택이 필요하였다.
아래는 6개의 genome에 대한 각 옵션별 통계이다. 추가적으로, Antismash 프로그램에 대한 소요시간을 마지막 행에 표기하였다. 
||DeepBGC|loose,clusterhmmer|relaxed,clusterhmmer|loose,fullhmmer|
|-|-|-|-|-|
|Bifidobacterium aesculapii|32|15|2|15|
|Bifidobacterium micronisargentati|12|13|0|13|
|Lacticaseibacillus chiayiensis|17|13|5|13|
|Lactococcus hircilactis|18|17|5|17|
|Streptococcus downei|13|21|10|21|
|Streptococcus loxodontisalivarius|21|19|3|19|
|time(sec)|-|851|361|3423|

DeepBGC output과 가장 유사한 개수의 BGC를 반환하며, 소요시간이 적은 loose,clusterhmmer 옵션을 선택하였다. 

## 2. Antismash output parsing
DeepBGC output과 효과적인 비교를 위해 DeepBGC에서 가공한 table과 형식이 유사한 table을 만들고자 했다. 포함하는 정보는 종명(숫자로 대체함)/candidate cluster의 기능/locus tag/protein id이다. parsing을 위한 코드는 아래와 같다. 

<pre>
<code>
import os
Dic_meta = {}
with open("/home/jjpark/Tools/Antismash/meta_antismash.txt") as x:
    lones = x.readlines()
    for lone in lones:
        lone = lone.rstrip()
        Dic_meta[lone.split('\t')[0]] = lone.split('\t')[-1]
genomelist = sorted(os.listdir('/home/jjpark/NCBI_dataset_Download/Antismash'))
for genome in genomelist:
    les = [] # bgc.gbk만 모아놓음
    bgcs = sorted(os.listdir("/home/jjpark//NCBI_dataset_Download/Antismash/%s" %genome))
    for bgc in bgcs:
        if ".gbk" in bgc:
            les.append(bgc)
        else:
            pass
    for i in les:
        if "genomic.gbk" in bgc:
            les.remove(bgc)
        else:
            pass
    ls = set(les)
    for l in ls:
        if l[0] == 'c':
            with open('/home/jjpark//NCBI_dataset_Download/Antismash/%s/%s' %(genome,l)) as f:
                bgc_id = str(Dic_meta[genome])
                locus_tag = []
                protein_id = []
                function = []
                category = []
                lines = f.readlines()
                for line in lines:
                    lin = line.lstrip()
                    li = lin.rstrip()
                    if li.startswith('Original ID'):
                        k = lines.index(line)
                        bgc_id = bgc_id + '_' + lines[k][28:-1]
                    if li.startswith('Orig. start'):
                        bgc_id = bgc_id + '_' + li[16:]
                    if li.startswith('Orig. end'):
                        bgc_id = bgc_id + '-' + li[16:]
                    if li.startswith('gene'):
                        n = lines.index(line)
                        loc_tag = [s for s in lines[n+1:n+5] if '/locus_tag' in s]
                        for lt in loc_tag:
                            lt = lt.lstrip()
                            locus_tag.append(lt[12:-2])
                    if li.startswith('/protein_id'):
                        protein_id.append(li[13:-1])
                    if li.startswith('/rules'):
                        n = lines.index(line)
                        func = [s for s in lines[n-5:n+5] if '/product' in s]
                        for fun in func:
                            fun = fun.lstrip()
                            function.append(fun[10:-2])
                function = set(function)
                locus_tag = sorted(set(locus_tag))
                protein_id = sorted(set(protein_id))
                with open("/home/jjpark/Tools/Antismash/antismash_table2.txt",'a') as p:
                    p.write('AT'+'_'+bgc_id +'\t'+';'.join(function) +'\t'+ ';'.join(locus_tag) + '\t' + ';'.join(protein_id)+'\n')
        else:
            with open('/home/jjpark//NCBI_dataset_Download/Antismash/%s/%s' %(genome,l)) as f:
                locus_tag = []
                protein_id = []
                function = []
                category = []
                for line in lines:
                    lin = line.lstrip()
                    li = lin.rstrip()
                    if li.startswith('Orig. start'):
                        bgc_id = bgc_id + '_' + li[16:]
                    if li.startswith('Orig. end'):
                        bgc_id = bgc_id + '-' + li[16:]
                    if li.startswith('gene'):
                        n = lines.index(line)
                        loc_tag = [s for s in lines[n+1:n+5] if '/locus_tag' in s]
                        for lt in loc_tag:
                                lt = lt.lstrip()
                                locus_tag.append(lt[12:-2])
                    if li.startswith('/protein_id'):
                        protein_id.append(li[13:-1])
                    if li.startswith('ACCESSION'):
                        bgc_id = bgc_id +'_'+li[12:]
                    if li.startswith('/rules'):
                        n = lines.index(line)
                        func = [s for s in lines[n-5:n+5] if '/product' in s]
                        for fun in func:
                            fun = fun.lstrip()
                            function.append(fun[10:-2])
                function = set(function)
                locus_tag = sorted(set(locus_tag))
                protein_id = sorted(set(protein_id))
            with open("/home/jjpark/Tools/Antismash/antismash_table2.txt",'a') as p:
                p.write('AT'+'_'+bgc_id +'\t'+';'.join(function) +'\t'+  ';'.join(locus_tag) + '\t' + ';'.join(protein_id)+'\n') 
</code>
</pre>
gbk format의 파일 parsing이 처음이라 어려운 점이 있었다. 

## 3. DeepBGC-Antismash output 결과 비교 데이터 전처리
### 3-1. 비교를 위한 지표 설정
BGC의 상관 관계를 1) 동치 2) split 3) component  4) difference 5) none 으로 나눴다. 
동치의 경우, contig에서 detected된 BGC가 같은 locus tag으로 구성되었을 때, split은 1개 프로그램의 결과가 다른 프로그램에서 2개의 연속된 BGC에 나눠져있을 때, component는 1개 프로그램의 결과가 다른 프로그램의 BGC에 일부일 때, difeerence는 같은 contig에 대해 시행된 BGC에서 일부 locus tag이 다를 때, none은 1개 프로그램에서 검출된 BGC가 다른 프로그램에서는 검출되지 않았을 때를 의미한다. 
사용할 수 있는 데이터는 Protein ID, Nucleotide region, Locus tag이 있다.
비교의 대상이 gene인데, Nucleotide region은 같은 gene을 detecting 하였어도 Nucleotide region이 다를 수 있기에 사용하지 않았다. 
Protein ID는 같은 서열로 구성된 Protein은 같은 Protein ID를 갖게되는데, 같은 종에서 2개 이상의 BGC에 같은 Protein ID를 갖는 서열이 등장할 때, 다른 프로그램과 비교에서 통계적 오류가 나타날 수 있다. 
예를 들어, DeepBGC의 A종에 대한 Output이 1번 BGC가  WP1/WP2/WP3, 2번 BGC가 WP1/WP4/WP5가 나타났을 때, Antismash의 A종에 대한 Output의 1번 BGC가 WP1/WP4/WP5를 검출했을 때 Antismash의 output을 DeepBGC의 2번과 정확한 동치이며, 1번과 관련 없지만, 관련도가 있게 나오게 된다. 앞서 말한 이유로, 연관성의 지표로 사용하는 것을 locus tag으로 정했다.

### 3-2 Locus tag을 위한 DeepBGC 데이터 재가공
DeepBGC의 정보를 압축적으로 담은 table은 bgc.tsv 파일을 raw data로 사용했다. tsv파일에서 locus tag 정보를 포함하지 않아, locus tag 정보를 포함하는 데이터를 위해 bgc.gbk 파일을 새롭게 parsing할 필요가 있었다. 파싱하는 코드는 아래와 같다.
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
종명 - 숫자의 정보를 포함하는 meta file과 작성한 DeepBGC output table, DeepBGC output.bgc.gbk 파일 3개 간의 연관을 지어 코딩하는 부분에 어려움이 있었다. 
