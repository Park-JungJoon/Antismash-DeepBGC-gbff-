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
        name.append(line.split('_')[0])
        NZs.append(line.split('_')[1]+'_'+line.split('_')[2])
        nucl_start.append(line.split('_')[3][:-2].split('-')[0])
        nucl_end.append(line.split('_')[3][:-2].split('-')[1])
    for i in range(len(name)):
        db.append([name[i],NZs[i],nucl_start[i],nucl_end[i],[]])
dic_db = {}
for z in range(len(db)):
    dic_db[db[z][1]+'_'+db[z][2]+'-'+db[z][3]] = db[z][0]
dic_lt = {}
answer = []
with open("/home/jjpark/as_db_compare/44.txt") as f:
    lines = f.readlines()
    lost = []
    for line in lines:
        line = line.rstrip()
        lost.append(line.split(' '))
for i in range(len(lost)):
    if len(lost[i]) == 2:
        answer.append(dic_db[lost[i][0]]+'_'+lost[i][0]+'\t'+lost[i][1]) 
    else:
        pass
for t in range(len(answer)):
    print(answer[t])
