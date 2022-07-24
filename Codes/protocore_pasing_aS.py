from collections import defaultdict as ddic
from Bio import SeqIO
import os
Dic_meta = {}
with open("/home/jjpark/Tools/Antismash/meta_antismash.txt") as x:
    lones = x.readlines()
    for lone in lones:
        lone = lone.rstrip()
        Dic_meta[lone.split('\t')[0]] = lone.split('\t')[-1]
genomelist = sorted(os.listdir('/espeon/analysis1/jjpark/Antismash'))
for genome in genomelist:
    les = [] # bgc.gbk만 모아놓음
    bgcs = sorted(os.listdir("/espeon/analysis1/jjpark/Antismash/%s" %genome))
    for bgc in bgcs:
        if ".gbk" in bgc and 'region' in bgc:
            les.append(bgc)
    for l in les:
        if l[0] == 'c':
            parse = SeqIO.parse('/espeon/analysis1/jjpark/Antismash/%s/%s'%(genome,l),'genbank')
            core_region_list = []
            locus_tag = []
            category = []
            bgc_id = (Dic_meta[genome])
            for record in parse:
                nucl_start = record.annotations['structured_comment']['antiSMASH-Data']['Orig. start'] 
                nucl_end = record.annotations['structured_comment']['antiSMASH-Data']['Orig. end']
                contigname_version = record.annotations['structured_comment']['antiSMASH-Data']['Original ID']
                contigname = contigname_version.split(' ')[0][0:-2]  
                for feat in record.features:
                    if feat.type == 'proto_core':
                        proto_core_start = feat.location.start
                        proto_core_end = feat.location.end
                        core_region_list.append(proto_core_start)
                        core_region_list.append(proto_core_end)
                core_region = range(int(sorted(core_region_list)[0]),int(sorted(core_region_list)[-1]))
                for feat in record.features:
                    if feat.type == 'gene':
                        lct = feat.qualifiers['locus_tag'][0]
                        gene_start = feat.location.start
                        if int(gene_start) in core_region:
                            locus_tag.append(lct)
                    if feat.type == 'protocluster':
                        ct = feat.qualifiers['category'][0]
                        category.append(ct)
                for i in range(len(core_region_list)):
                    core_region_list[i] = str(core_region_list[i]).replace('>','')
                    core_region_list[i] = str(core_region_list[i]).replace('<','')
                nucl_start = str(nucl_start).replace('>','')
                nucl_start = str(nucl_start).replace('<','')
                nucl_end = str(nucl_end).replace('>','')
                nucl_end = str(nucl_end).replace('<','')
                s = int(core_region_list[0]) + int(nucl_start)
                e = int(core_region_list[-1]) + int(nucl_start)
                print('ATPC'+'_'+str(Dic_meta[genome])+'_'+contigname+'_'+str(core_region_list[0])+'-'+str(core_region_list[-1])+'_'+str(nucl_start)+'-'+str(nucl_end)+'_'+str(s)+'-'+str(e)+'\t'+';'.join(category)+'\t'+';'.join(locus_tag))
        else:
            parse = SeqIO.parse('/espeon/analysis1/jjpark/Antismash/%s/%s'%(genome,l),'genbank')
            core_region_list = []
            locus_tag = []
            category = []
            bgc_id = (Dic_meta[genome])
            for record in parse:
                nucl_start = record.annotations['structured_comment']['antiSMASH-Data']['Orig. start'] 
                nucl_end = record.annotations['structured_comment']['antiSMASH-Data']['Orig. end']
                contigname = record.annotations['accessions'][0]  
                for feat in record.features:
                    if feat.type == 'proto_core':
                        proto_core_start = feat.location.start
                        proto_core_end = feat.location.end
                        core_region_list.append(proto_core_start)
                        core_region_list.append(proto_core_end)
                core_region = range(int(sorted(core_region_list)[0]),int(sorted(core_region_list)[-1]))
                for feat in record.features:
                    if feat.type == 'gene':
                        lct = feat.qualifiers['locus_tag'][0]
                        gene_start = feat.location.start
                        if int(gene_start) in core_region:
                            locus_tag.append(lct)
                    if feat.type == 'protocluster':
                        ct = feat.qualifiers['category'][0]
                        category.append(ct)
                for i in range(len(core_region_list)):
                    core_region_list[i] = str(core_region_list[i]).replace('>','')
                    core_region_list[i] = str(core_region_list[i]).replace('<','')
                nucl_start = str(nucl_start).replace('>','')
                nucl_start = str(nucl_start).replace('<','')
                nucl_end = str(nucl_end).replace('>','')
                nucl_end = str(nucl_end).replace('<','')
                s = int(core_region_list[0]) + int(nucl_start)
                e = int(core_region_list[-1]) + int(nucl_start)
                print('ATPC'+'_'+str(Dic_meta[genome])+'_'+contigname+'_'+str(core_region_list[0])+'-'+str(core_region_list[-1])+'_'+str(nucl_start)+'-'+str(nucl_end)+'_'+str(s)+'-'+str(e)+'\t'+';'.join(category)+'\t'+';'.join(locus_tag))
