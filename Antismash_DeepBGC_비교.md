# Antismash-DeepBGC(gbff) 
## 기본적 통계
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
해당 데이터는 Antismash가 detecting한 5045개의 BGC와 DeepBGC가 detecting한 4801개의 BGC 중, 1823개의 BGC는 같은 종의 같은 contig의 같은 locus tag을 공유하였다. 
아래 그래프는 1823 종의 BGC에 대한 jaccard similarity에 대한 밀도 분포표이다. 

![image](https://user-images.githubusercontent.com/97942772/178886144-e9becd79-31d6-4d0d-b066-e5ea188214f8.png)

이 중 75개의 BGC의 경우 75개의 BGC는 모든 locus tag이 일치해 같았고, 상위 10퍼센트의 BGC는 82% 이상의 locus tag의 일치도를 보였다. 
