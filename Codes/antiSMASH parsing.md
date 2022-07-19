## Antismash output parsing
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
