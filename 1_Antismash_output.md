Probiotics 405종에 대한 Antismash output  
==============================
* DepBGC와 Antismash의 결과를 비교 분석하여 신뢰성이 높은 BGC를 찾아내는 것을 연구의 목적으로 한다.  

# 1. Antismash running
## 1-1. Input data 선정 
* 고시형 균주 19종이 포함된 9속(Enterococcus, Lactobacillus, Limosilactobacillus,Bifidobacterium, Lacticaseibacillus, Lactococcus, Streptococcus, Lactiplantibacillus, Ligilactobacillus) 중, NCBI representative genome에 해당하는 405종의 gbff 데이터를 사용함.
* 종이 분류가 불분명한  경우 Taxid를 기반으로 분류하여 사용하였음. 
* gbff format을 사용하는 이유는, fna format의 경우  

## 1-2. Running option
Antismash Running에 사용한 option은 아래와 같다. 

    antismash --output-dir --genefinding-tool none --hmmdetection-strictness loose --asf --pfam2go --rre --clusterhmmer

+ hmmdetection strictness의 loose/relaxed와 clusterhmmer/fullhmmer 옵션의 선택 필요.
+ Output의 개수가 DeepBGC와 유사하여 비교의 편의를 목적으로 함. 

연구 목적에 적합한 옵션의 선택을 위해 DeepBGC에서 detecting한 BGC가 10개 이상인 genome 6개를 선정하였고, 그 결과는 아래 표와 같음.


||DeepBGC|loose,clusterhmmer|relaxed,clusterhmmer|loose,fullhmmer|
|-|-|-|-|-|
|Bifidobacterium aesculapii|32|15|2|15|
|Bifidobacterium micronisargentati|12|13|0|13|
|Lacticaseibacillus chiayiensis|17|13|5|13|
|Lactococcus hircilactis|18|17|5|17|
|Streptococcus downei|13|21|10|21|
|Streptococcus loxodontisalivarius|21|19|3|19|
|time(sec)|-|851|361|3423|

각 칸은 option에서 detecting한 BGC의 개수를 의미하고, 최하단 행에 소요시간(sec)을 표기함.

**DeepBGC output과 가장 유사한 개수의 BGC를 반환하며, 소요시간이 적은 loose,clusterhmmer 옵션을 선택하였다.**

# 2. Antismash Output
+ 405개의 genome에서 총 5045개의 BGC가 detected 되었다. 
## 2-1. BGC에 대한 결과 
||AVG/Min-Max|Median|
|-|-|-|
|BGC per genome|12.46|12|
|Length(bp)|1093-103712|24227|
|Number of genes|1-92|11|

## 2-2. Antismash에서 반환하는 product class에 대한 결과
+ [Antismash](https://docs.antismash.secondarymetabolites.org/glossary/)에서 반환하는 결과는 링크와 같다. 
+ 405종에 대한 product의 종류는 총 32개이고, 일부는 multi function을 가진다. 
+ Multi function의 조합으로 405종에 대한 function 결과는 총 85개이다. 
+ [Outputs]https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/blob/main/AS_DB_outputs)는 링크와 같다. 
+ 32개의 종류를 RiPP, NRP, Saccharide, PKS, terpene, Others 총 6개의 종류로 재분류하였고, 기준은 Antismash output중 proto cluster의 category에 해당하는 값(fatty acid의 경우 Other를 반환함.)으로 하였다. 
+ Others에 carbon cyclic compounds, fatty acid들이 해당했다. 



# 3. Output Parsing
+ Parsing의 결과로 Output에 포함하고자 하는 정보는 종명(meta)/기능/locus tag/protein ID이다. 
+ Parsing을 위한 [code](https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/blob/main/codes)
