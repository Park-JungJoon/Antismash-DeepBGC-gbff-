<pre>
<code>
from collections import defaultdict
with open("C:/Users/jungj/Desktop/antismash_table.txt") as f:
    asls = []
    lines = f.readlines()
    for line in lines:
        line=line.rstrip()
        asls.append(line.split('\t'))
with open("C:/Users/jungj/Desktop/lct_deepbgc.txt") as p:
    dbls = []
    lanes = p.readlines()
    for lane in lanes:
        lane = lane.rstrip()
        dbls.append(lane.split('\t'))

for i in range(len(dbls)):
    dbls[i][0] = dbls[i][0].replace('.1','')
    dbls[i][0] = dbls[i][0].replace('.2','')
for n in range(len(asls)):
    asls[n][0] = asls[n][0].replace('>','')
    asls[n][0] = asls[n][0].replace('.1','')
    asls[n][0] = asls[n][0].replace('<','')

Das = defaultdict(dict)
Ddb = defaultdict(dict)
#locustag 키 = Das[k] / 벨류 풀네임(nucl start1-end100/200)
for i in range(len(asls)):
    Das['_'.join(asls[i][0].split('_')[1:4])][asls[i][0]] = set(asls[i][2].split(';'))

for i in range(len(dbls)):
    Ddb['_'.join(dbls[i][0].split('_')[0:3])][dbls[i][0]]=set(dbls[i][1].split(','))

for k,v in Das.items():
    if k not in Ddb:
        for k1 in v.keys():
            print("%s\tX\tnone"%k1)
            continue
    for k1,v1 in v.items(): #v1 antsismash의 locustag의 list (이중리스트)
        for k2,v2 in Ddb[k].items(): #v2 deepbgc의 locustag의 list
            if len(v1-v2) == 0:
                print("%s\t%s\tdia"% (k1,k2))
                continue
            if len(v2-v1) == 0:
                print("%s\t%s\taid"% (k1,k2))
                continue
            intersection = v1 & v2
            jac = len(intersection)/len(v1|v2)
            print("%s\t%s\t%s"% (k1,k2,jac))
            
            
for k,v in Ddb.items():
    if k not in Das:
        for k1 in v.keys():
            print("X\t%s\tnone"%k1)
</code>
</pre>
