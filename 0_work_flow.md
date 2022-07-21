# antiSMASH & DeepBGC ouput 비교 및 통합
## 1. 목적
+ antiSMASH와 DeepBGC의 결과를 비교하여, 신뢰성 높은 BGC로 통합함을 목적으로 한다.

## 2. 데이터 수집
+ 데이터는 NCBI refseq 데이터 중, 고시형 균주 19종이 포함되는 9속에 해당하는 genome 중 representative genome의 gbff 파일을 사용하였다. 
+ 연구에 사용된 9속 : Lactobacillus,Lacticaseibacillus,Lactiplantibacillus,Limosilactobacillus,Ligilactobacillus,Bifidobacterium,Enterococcus,Lactococcus,Streptococcus
+ 총 405개의 genome gbff 파일이 사용되었으며, 두 프로그램 모두 같은 데이터를 사용하였다. 

## 3. antiSMASH
### 3.1 antiSMASH running option
+ running option
<pre>
<code>
antismash --output-dir --genefinding-tool none --hmmdetection-strictness loose --asf --pfam2go --rre --clusterhmmer
</code>
</pre>
+ 연구의 목적이 DeepBGC와의 비교이므로, BGC와 유사한 개수의 BGC를 detecting하는 loose,clusterhmmer 옵션을 선택하였다. [옵션 선택을 위한 test running](https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/edit/main/1_Antismash_output.md)
### 3.2 antiSMASH output
+ 연구에 사용된 genome의 결과로 405개 genome에서 5045개의 BGC를 얻었다. 
+ 전체 BGC에 대한 통계 

||AVG/Min-Max|Median|
|-|-|-|
|BGC per genome|12.46|12|
|Length(bp)|1093-103712|24227|
|Number of genes|1-92|11|

+ antiSMASH는 결과로 product의 세부적인 class를 반환한다. [antiSMASH output 종류](https://docs.antismash.secondarymetabolites.org/glossary/)
+ 5045개의 BGC는 32개의 product class를 가졌고, 일부는 multi class를 가졌다. 총 85개의 조합이 결과로서 반환되었다. 
+ DeepBGC output과 수월한 비교를 위해 32개의 class를 총 6개의 category로 분류하였다. 
+ 분류 기준은 antiSMASH의 gbk 파일의 proto cluster catergory를 참고하였다. 
+ Category : RiPP, NRP, Saccharide, PKS, terpene, Others 

|category|count|
|-|-|
|saccharide|3864|
|RiPP|409|
|Other|352|
|PKS|163|
|terpene|20|
|NRP|17|
|Other;saccharide|107|
|RiPP;saccharide|52|
|PKS;saccharide|30|
|NRP;PKS|6|
|NRP;saccharide|5|
|Other;RiPP|4|
|saccharide;terpene|4|
|Other;RiPP;saccharide|2|
|NRP;RiPP|2|
|PKS;RiPP;saccharide|2|
|PKS;RiPP|2|
|NRP;Other;saccharide|1|
|NRP;Other;PKS|1|
|NRP;RiPP;saccharide|1|
|NRP;Other|1|
|sum|5045|

+ antiSMASH raw data가  transAT-PKS;PKS-like일 때, 변환은 PKS;PKS로 이뤄졌다. 같은 category에 해당하는 세부 class가 중복될 때, 중복을 무시하고 PKS에 분류하였다. 

## 4 DeepBGC
### 4.1 DeepBGC running option
<pre>
<code>
deepbgc pipeline --prodigal-meta-mode %s
</code>
</pre>

### 4.2 DeepBGC output filtering 
+ 연구에 사용된 genome의 결과로 405개 genome에서 4815개의 BGC를 얻었다. 
+ 짧은 contig에서 detected된 일부 BGC의 경우, gene predicting을 통해 gene을 추가하여 BGC라고 detect하였다. NCBI에 등록된 gene이 없어 gene locus tag을 갖지 못했다.
+ 이 경우, CDS에 BGC의 이름을 붙힌 후 locus tag을 임의로 부여했다. 
+ 아래는 29개의 BGC.
<pre>
<code>
NZ_CP074378.1_2073356-2074103,NZ_LOCM01000063.1_207-339,NZ_BOCI01000551.1_0-407,NZ_JACJJQ010000105.1_0-273,NZ_BLLI01000138.1_173-839,NZ_AZGI01000037.1_8-436,NZ_JAHBBF010000030.1_233-1016,NZ_CP014835.1_1251662-1252895,NZ_UFXU01000003.1_468401-469361,NZ_PDCG01000049.1_11-431,NZ_BMAY01000047.1_2-92,NZ_BMAY01000084.1_1-97,NZ_BMAY01000094.1_112-199,NZ_BMAY01000108.1_2-200,NZ_BMAY01000110.1_0-120,NZ_AWWH01000062.1_43-1429,NZ_WSRS01000186.1_298-520,NZ_JABASA010000009.1_35302-36406,NZ_AZDU01000130.1_0-548,NZ_VFSG01000001.1_907958-908819,NZ_AZGM01000048.1_2-119,NZ_AZEU01000017.1_1-376,NZ_AZEU01000308.1_0-235,NZ_AZEU01000317.1_0-402,NZ_AZEU01000320.1_0-326,NZ_FMIX01000004.1_722704-723511,NZ_JAFBEH010000092.1_271-1063,NZ_JAFBEH010000093.1_98-1052,NZ_VFJA01000003.1_212209-218212
</code>
</pre>
위의 29개의 BGC는 연구에서 제외하고 4786의 BGC를 연구 대상으로 사용하였다. 

### 4.3 DeepBGC output 
 
+ BGC에 대한 통계 

||DeepBGC|
|-|-|
|BGCs per genome(median)|11.82(10)|
|length_bp(median)|48-429148(3068)|
|number of genes(median)|1-407(3)|

+ DeepBGC의 경우, Output을 Product activity와 Product class로 나타낸다.
+ Product activity : antibacterial, antifungal, cytotoxic, inhibitor, unknown activity
+ Product class : Alkaloid, NRP, RiPP, Terpene, Saccharide, Polyketide, Other, unknown class
+ DeepBGC는 BGC detecting을 먼저 한 후, 기능을 부여하기 때문에 unknown activity와 unknown class가 존재한다. 
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
|Unknown class|2753|
|Polyketide;Terpene|9|
|NRP;Polyketide|17|
|Saccharide;Terpene|1|
|RiPP;other|1|
|sum|4815|

## 5. antiSMASH & DeepBGC output comparing 
+ DeepBGC와 antiSMASH에서 detected된 BGC의 기본적 정보 비교

||DeepBGC|antiSMASH|
|-|-|-|
|BGCs per genome(median)|11.82(10)|12.46(12)|
|length_bp(median)|48-429148(3068)|1093-103712(24227)|
|number of genes(median)|1-407(3)|1-92(22)|

+ genome당 detected된 BGC개수를 나타낸 그래프. x좌표 Antismash output count, y좌표 DeepBGC output count으로 나타냈다. 

<img width="628" alt="as_bgc_db_bgc_ggeompoint" src="https://user-images.githubusercontent.com/97942772/178883455-bf243db2-75fd-472b-9841-2cd8603ad598.png">

+ DeepBGC Output에서 Lacticaseibacillus jixianensis, Lactobacillus mulieris는 특이적으로 BGC가 각각 62개, 76개 detected 되어 그래프 가시성을 목적으로 제외했다. 







+ 각 프로그램에서 detected된 BGC간의 유사도를 측정하고자 gene의 lous tag을 지표로서 사용하였다. 
+ BGC의 locus tag의 구성을 jaccard similarity를 통해 측정하였다. 
+ DeepBGC 4786개, antiSMASH 5045개 중, 같은 종의 같은 contig의 같은 locus tag을 공유하는 BGC는 1824개이다. [jaccard similarity](https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/blob/main/Supplementary%20data/result_region_lct_processed.txt).

+ 아래 히스토그램은 각각 1824개의 BGC에 대한 locus tag의 jaccad similarity 값을 표시하였다.

![image](https://user-images.githubusercontent.com/97942772/178940537-9002037c-7777-4f7e-82d3-7bfaf624de01.png)

+ 아래 히스토그램은 각각 1824개의 BGC에 대한 region의 jaccad similarity 값을 표시하였다.

![image](https://user-images.githubusercontent.com/97942772/178940469-0b7031c8-85d0-4621-a645-600c59f37813.png)


+ 75개의 BGC의 경우 모든 locus tag이 일치해 같았고, 상위 10퍼센트의 BGC는 82% 이상의 locus tag의 일치도를 보였다. 

# 6. antiSMASH, DeepBGC intergrating
