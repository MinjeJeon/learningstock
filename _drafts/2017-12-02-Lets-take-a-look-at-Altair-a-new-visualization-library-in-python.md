---
title: python의 새로운 시각화 라이브러리 Altair 살펴보기
date: 2017-12-02 21:53 +0900
categories:
- python
tags:
- 시각화
layout: post
image: 20171203_altair_cars.png
published: true
---

데이터 사이언스에서 R과 파이썬은 영원한 라이벌이죠. R이 좋냐 파이썬이 좋냐는 업계에서 "엄마가 좋니 아빠가 좋니?" 급의 논쟁거리입니다. 이런 종류의 글만 나오면 R언어 신봉자와 파이썬 언어 신봉자들이 득달같이 달려들어서 클릭 수를 올리려는 낚시성 글도 많이 올라온다고 하네요. 이 주제에 대해 파이썬의 우세를 점치는 최근 몇 가지의 흥미로운 글이 있습니다.

* [캐글 블로그 - 2016년 제출된 Kernel 수에서 파이썬은 명백한 승자](http://blog.kaggle.com/2017/01/05/your-year-on-kaggle-most-memorable-community-stats-from-2016/#kernels-datasets)
* [KDnuggets - Python이 R을 추월하고 데이터 과학, 기계학습 플랫폼의 리더가 되다.](https://www.kdnuggets.com/2017/08/python-overtakes-r-leader-analytics-data-science.html)

그럼에도 불구하고 R의 장점/파이썬의 단점으로 많이 언급되는 부분이 파이썬의 시각화 라이브러리는 R의 기본 plot이나 ggplot2에 비해 작성하기 어렵다는 점입니다. '[R vs Python for Data Science: Summary of Modern Advances](https://elitedatascience.com/r-vs-python-for-data-science)'라는 글에서는 최근에 이루어진 R과 파이썬의 최근의 성과에 대해 알려주는데, Altair라는 새로운 라이브러리는 R의 ggplot2와 비슷하게 선언형(declarative) 시각화[^def1]를 할 수 있는 라이브러리로 주목받는 중입니다. [전체 동영상](https://blog.dominodatalab.com/video-huge-debate-r-vs-python-data-science/)에서는 R과 파이썬의 전반적 역사와 요즘 트렌드를 알려주고 있으니 함께 보시는 것을 추천합니다.

이 글에서는 지금까지 파이썬에서 많이 쓰이는 시각화 라이브러리를 살펴보고, altair로 몇 가지 그래프를 만들어 보겠습니다.

## 파이썬 지금까지의 시각화 라이브러리

### matplotlib (<https://matplotlib.org/>)

{% include ls/image.html
   src='20171203_matplotlib.png'
%}

거의 모든 파이썬 시각화 라이브러리의 조상님이죠. matlab라는 언어에서 사용되는 문법을 차용해서 만들었는데요. 이게 옛날에 만들었다 보니 데이터와 표현 방법이 섞여 있어 혼란스러우며, 색깔이 들어간 점을 찍으려면 for 루프를 돌려야 하는 등 학습 난이도가 높은 편입니다. 그런데 한글로 된 자료들은 대부분 matplotlib으로 시각화를 하는 경우가 많아서 파이썬이 시각화가 어렵다고 생각하는데 일조하지 않나 생각이 듭니다.

* 장점
    * 많은 레퍼런스 보유 (= 인터넷에 코드가 많이 올라와서 베끼기 쉬움)
    * matlab와 유사한 문법으로 matlab 언어 사용자에게 친숙함.
    * 차트에 표시된 항목들을 세세하게 커스터마이징 가능 (= 리포팅에 적합)

* 단점
    * 엄청나게 복잡한 문법
    * 비직관적인 사용법
    * 시각화를 위해 많은 코드를 작성해야 함
    * 데이터 분석 라이브러리인 pandas를 기본으로 지원하지 않음
    * 약간 못생긴 기본 스타일

### seaborn (<https://seaborn.pydata.org/>)

{% include ls/image.html
   src='20171203_seaborn.png'
%}

matplotlib를 기반으로 통계적 시각화를 편리하게 할 수 있도록 해주는 라이브러리입니다. 강력한 시각화 기능을 가지고 있고, 디자인도 예쁜 편이여서 현재 실무에서 많이 사용되고 있습니다. 쉬운 기능은 간단한 자체 기능을 사용하고, 어려운 기능은 matplotlib의 기능을 차용해서 쓰는 형태로 구성 되어있습니다.

* 장점
    * matplotlib에 비해 상대적으로 사용하기 쉬운 문법
    * pandas와 잘 연동됨
    * 나아진 디자인
    * seaborn.set()만으로도 matplotlib의 디자인이 업그레이드 됨
    * 다양한 예제 갤러리

* 단점
    * matplotlib에 종속되어 있어 리포팅 용도의 차트를 원한다면 matplotlib의 문법을 배워야 함

### Altair (<https://altair-viz.github.io/>)

* 장점
    * 간편한 문법 (= 탐색적 데이터 분석(EDA), 혼자 빨리 보기에 적합)
    * [d3.js](https://d3js.org/) / [vega](http://vega.github.io/)에 기반하고 있어 웹서비스와 연동이 쉬움
    * 마우스를 올렸을 때 값을 표시하는 등 vega의 확장을 이용하기 쉬움
    * pandas와 매우 잘 연동
    * jupyter notebook과 잘 작동함.
* 단점
    * 레퍼런스가 적음
    * 다른 두 라이브러리에 비해 개발이 활발하지 않음
    * pairplot 등 통계적 시각화 일부 미지원


## 설치 방법

아래와 같은 순서로 설치합니다.

```bash
$ pip install altair
$ pip install --upgrade notebook
$ jupyter nbextension enable --sys-prefix --py vega
```

Anaconda를 사용한다면 아래와 같이 설치합니다.

```bash
$ conda install altair --channel conda-forge
```

[^def1]: 풋

