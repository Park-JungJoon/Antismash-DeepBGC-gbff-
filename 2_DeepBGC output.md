# 1. DeepBGC running
## 1-1. Input data 선정 
* 고시형 균주 19종이 포함된 9속(Enterococcus, Lactobacillus, Limosilactobacillus,Bifidobacterium, Lacticaseibacillus, Lactococcus, Streptococcus, Lactiplantibacillus, Ligilactobacillus) 중, NCBI representative genome에 해당하는 405종의 gbff 데이터를 사용함.
* 종이 분류가 불분명한  경우 Taxid를 기반으로 분류하여 사용하였음. 
* gbff format을 사용하는 이유는, fna format의 경우 DeepBGC에서 protein prediction 과정에서 정확하지 않은 정보로 가공될 가능성이 있기 때문에, NCBI에서 제공하는 정보를 토대로 분석을 실시하고자함. 

## 1-2. Running option
DeepBGC Running에 사용한 option은 아래와 같다. 
<pre>
<code>
deepbgc pipeline --prodigal-meta-mode %s
</code>
</pre>

# 2. DeepBGC Output
+ 405개의 genome에서 총 4815개의 BGC가 detected 되었다. 
## 2-1. BGC output filtering 
+ DeepBGC가 detecting한 일부 BGC들의 경우 gene의 locus tag이 없는 경우가 있었음.
+ DeepBGC가 짧은 contig를 gene predicting을 통해 BGC라고 detect한 경우, NCBI에 등록된 gene이 없어 gene locus tag을 갖지 못했음.
+ 이 경우, CDS에 BGC의 이름을 붙힌 후 기능을 임의로 부여했음. 
+ 아래는 29개의 BGC.
<pre>
<code>
NZ_CP074378.1_2073356-2074103,NZ_LOCM01000063.1_207-339,NZ_BOCI01000551.1_0-407,NZ_JACJJQ010000105.1_0-273,NZ_BLLI01000138.1_173-839,NZ_AZGI01000037.1_8-436,NZ_JAHBBF010000030.1_233-1016,NZ_CP014835.1_1251662-1252895,NZ_UFXU01000003.1_468401-469361,NZ_PDCG01000049.1_11-431,NZ_BMAY01000047.1_2-92,NZ_BMAY01000084.1_1-97,NZ_BMAY01000094.1_112-199,NZ_BMAY01000108.1_2-200,NZ_BMAY01000110.1_0-120,NZ_AWWH01000062.1_43-1429,NZ_WSRS01000186.1_298-520,NZ_JABASA010000009.1_35302-36406,NZ_AZDU01000130.1_0-548,NZ_VFSG01000001.1_907958-908819,NZ_AZGM01000048.1_2-119,NZ_AZEU01000017.1_1-376,NZ_AZEU01000308.1_0-235,NZ_AZEU01000317.1_0-402,NZ_AZEU01000320.1_0-326,NZ_FMIX01000004.1_722704-723511,NZ_JAFBEH010000092.1_271-1063,NZ_JAFBEH010000093.1_98-1052,NZ_VFJA01000003.1_212209-218212
</code>
</pre>

## 2-2. DeepBGC에서 반환하는 product class에 대한 결과
+ BGC에 대한 결과

||DeepBGC|
|-|-|
|BGCs per genome(median)|11.82(10)|
|length_bp(median)|48-429148(3068)|
|number of genes(median)|1-407(3)|

+ DeepBGC는 Product class, Product activity를 결과로서 반환한다.
+ Product activity : antibacterial, antifungal, cytotoxic, inhibitor, unknown activity
+ Product class : Alkaloid, NRP, RiPP, Terpene, Saccharide, Polyketide, Other, unknown class
+ 일부 종은 multi function을 갖는다. 
+ antiSMASH와 비교를 위해 class만 표기하였다. 

|class|count|
|-|-|
|Alkaloid|0|
|NRP|135|
|RiPP|534|
|other|77|
|Polyketide|394|
|Saccharide|846|
|Terpene|48|
|NAC|2753|
|Polyketide;Terpene|9|
|NRP;Polyketide|17|
|Saccharide;Terpene|1|
|RiPP;other|1|
|sum|4815|



# 3. Output Parsing
+ Parsing의 결과로 Output에 포함하고자 하는 정보는 종명(meta)/기능/locus tag/protein ID이다. 
+ Parsing을 위한 [code]([https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/blob/main/codes](https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/blob/main/Codes/DeepBGC%20locustag%20parsing.md)), 추가적으로 비교를 위한 Table로 가공하는 [code](https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/blob/main/Codes/db%20locus%20tag%20parsing%20file%20reprocessing.md)
