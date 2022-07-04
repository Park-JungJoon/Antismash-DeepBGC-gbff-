# Antismash-DeepBGC-gbff-
## 1. gbff파일을 DeepBGC 프로그램 사용의 결과물과 Antismash 결과 비교를 위한 Antismash 옵션 탐색
사용하는 Antismash 옵션은 아래와 같다. 
<pre>
<code>
antismash --output-dir --hmmdetection-strictness loose --asf --pfam2go --rre --clusterhmmer
</code>
</pre>
이 중, DeepBGC의 결과물에 대한 비교 분석을 위해 hmmdetection strictness의 loose/relaxed와 clusterhmmer/fullhmmer 옵션의 선택이 필요하였다.
아래는 6개의 genome에 대한 각 옵션별 통계이다. 추가적으로, Antismash 프로그램에 대한 소요시간을 마지막 행에 표기하였다. 
||DeepBGC|loose,clusterhmmer|relaxed,clusterhmemr|relaxed,clusterhmmer|
|-|-|-|-|-|
|Bifidobacterium aesculapii|32|15|2|15|
|Bifidobacterium micronisargentati|12|13|0|13|
|Lacticaseibacillus chiayiensis|17|13|5|13|
|Lactococcus hircilactis|18|17|5|17|
|Streptococcus downei|13|21|10|21|
|Streptococcus loxodontisalivarius|21|19|3|19|
|time(sec)|-|851|361|3423|

DeepBGC output과 가장 유사한 개수의 BGC를 반환하며, 소요시간이 적은 loose,clusterhmmer 옵션을 선택하였다. 
