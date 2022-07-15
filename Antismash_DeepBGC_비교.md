# Antismash-DeepBGC(gbff) 
## 기본적 통계
### Antismash 통계 
Antismash의 최종 output candidate cluster의 기능을 통계냈다. 아래 표기한 표와 같고, multi function이 있는 경우, 각 function에 더하여 전체 BGC 개수 5045개보다 count의 합이 많다.

|function|count|
|-|-|
|cyclic-lactone-autoinducer|37|
|betalactone|7|
|NRPS-like|6|
|lanthipeptide-class-ii|52|
|PKS-like|1|
|RRE-containing|32|
|RaS-RiPP|30|
|fatty_acid|431|
|saccharide|4068|
|lanthipeptide-class-iii|12|
|arylpolyene|6|
|ladderane|1|
|butyrolactone|3|
|hglE-KS|2|
|lanthipeptide-class-iv|16|
|T3PKS|195|
|LAP|27|
|RiPP-like|269|
|lanthipeptide-class-i|79|
|furan|8|
|terpene|24|
|T1PKS|6|
|halogenated|4|
|phosphonate|1|
|sactipeptide|1|
|NRPS|34|
|transAT-PKS|2|
|lanthipeptide-class-v|1|
|thiopeptide|11|
|lassopeptide|10|
|phenazine|10|
|ranthipeptide|3|



||DeepBGC|AntiSmash|
|-|-|-|
|BGCs per genome(median)|11.82(10)|12.46(12)|
|length_bp(median)|48-429148(3068)|1093-103712(24227)|
|number of genes(median)|1-407(3)|1-92(22)|

아래 그래프는 종 당 detected된 BGC의 개수를 x좌표 Antismash output, y좌표 DeepBGC output으로 나타냈다. 

<img width="628" alt="as_bgc_db_bgc_ggeompoint" src="https://user-images.githubusercontent.com/97942772/178883455-bf243db2-75fd-472b-9841-2cd8603ad598.png">

DeepBGC Output에서 Lacticaseibacillus jixianensis, Lactobacillus mulieris는 특이적으로 BGC가 각각 62개, 76개 detected 되어 그래프 가시성을 목적으로 제외했다. 
BGC detecting의 편차가 Antismash보다 DeepBGC가 더 크다.

https://github.com/Park-JungJoon/Antismash-DeepBGC-gbff- 에서 두 프로그램 간 Detected 된 BGC의 locus tag 구성을 jaccard similarity를 통해 유사도를 측정한 txt를 만들었다.
해당 데이터는 Antismash가 detecting한 5045개의 BGC와 DeepBGC가 detecting한 4786개의 BGC 중, 1824개의 BGC는 같은 종의 같은 contig의 같은 locus tag을 공유하였다. 
아래 히스토그램은 각각 1824개의 겹치는 region을 갖는 BGC에 대한 locus tag/region jaccard similarity에 대한 밀도 분포표이다.

![image](https://user-images.githubusercontent.com/97942772/178940537-9002037c-7777-4f7e-82d3-7bfaf624de01.png)

![image](https://user-images.githubusercontent.com/97942772/178940469-0b7031c8-85d0-4621-a645-600c59f37813.png)


이 중 75개의 BGC의 경우 75개의 BGC는 모든 locus tag이 일치해 같았고, 상위 10퍼센트의 BGC는 82% 이상의 locus tag의 일치도를 보였다. 
