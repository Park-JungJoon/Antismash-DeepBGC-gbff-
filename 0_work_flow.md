# antiSMASH & DeepBGC ouput 비교 및 통합
## 1. 목적
+ antiSMASH와 DeepBGC의 결과를 비교하여, 신뢰성 높은 BGC로 통합함을 목적으로 한다.
## 2. 연구 과정
### 2.1 데이터 수집
+ 데이터는 NCBI refseq 데이터 중, 고시형 균주 19종이 포함되는 9속에 해당하는 genome 중 representative genome의 gbff 파일을 사용하였다. 
+ 연구에 사용된 9속 : Lactobacillus,Lacticaseibacillus,Lactiplantibacillus,Limosilactobacillus,Ligilactobacillus,Bifidobacterium,Enterococcus,Lactococcus,Streptococcus
### 2.2 antiSMASH
#### 2.2.1 antiSMASH running option
+ running option
<pre>
<code>
antismash --output-dir --genefinding-tool none --hmmdetection-strictness loose --asf --pfam2go --rre --clusterhmmer
</code>
</pre>
+ 연구의 목적이 DeepBGC와의 비교이므로, BGC와 유사한 개수의 BGC를 detecting하는 loose,clusterhmmer 옵션을 선택하였다. [옵션 선택을 위한 test running](https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff-/edit/main/1_Antismash_output.md)
#### 2.2.2 antiSMASH output
+ 연구에 사용된 genome의 결과로 405개 genome에서 5045개의 BGC를 얻었다. 
+ 전체 BGC에 대한 통계 

||AVG/Min-Max|Median|
|-|-|-|
|BGC per genome|12.46|12|
|Length(bp)|1093-103712|24227|
|Number of genes|1-92|11|

+ antiSMASH는 결과로 product의 세부적인 class를 반환한다. [antiSMASH output 종류](https://docs.antismash.secondarymetabolites.org/glossary/)
+ 5045개의 BGC는 그 중, 32개의 product class를 가졌고, 일부는 multi class를 가졌다. 총 85개의 조합이 결과로서 반환되었다. 
+ DeepBGC output과 수월한 비교를 위해 32개의 class를 총 6개의 category로 분류하였다. 
+ 분류 기준은 antiSMASH의 gbk 파일의 proto cluster catergory를 참고하였다. 
+ Category : RiPP, NRP, Saccharide, PKS, terpene, Others 

|function|count|
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

### 2.3 DeepBGC
+ 연구에 사용된 genome의 결과로 405개 genome에서 4815개의 BGC를 얻었다. 
+ 전체 BGC에 대한 통계 

||DeepBGC|
|-|-|
|BGCs per genome(median)|11.82(10)|
|length_bp(median)|48-429148(3068)|
|number of genes(median)|1-407(3)|

+ DeepBGC의 경우, 
