---
title: seaborn(matplotlib)으로 주가 그래프 그리기 팁
date: 2016-10-16 14:30 +0900
categories:
- python
tags:
- python
- seaborn
- matplotlib
- pandas
layout: post
published: true
---


## 그래프 그리기 준비
{::comment}
먼저 기본 import 컨벤션으로 numpy, pandas를 불러온다.

```python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
```
{:/comment}
jupyter notebook 내에서 차트가 출력되도록 하고, 출력 형식을 벡터 그래픽인 SVG로 설정하여 확대해도 흐려지지 않게 한다.

```python
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
```

## pandas_datareader로 주가 불러오기

pandas_datareader를 이용하여 애플의 1년치 주가를 받아온다. 

```python
from pandas_datareader import data
aapl = data.YahooDailyReader('AAPL','20151001', '20160930', adjust_price=True).read()
aapl.head()
```

```
                  Open        High         Low       Close  Volume  Adj_Ratio
Date                                                                         
2015-10-01  118.489998  118.870003  117.230003  118.339996  278000        1.0
2015-10-02  119.309998  120.820000  118.580002  120.730003  557000        1.0
2015-10-05  121.790001  122.910004  121.760002  122.320000  338300        1.0
2015-10-06  120.919998  121.260002  120.370003  120.919998  350100        1.0
2015-10-07  122.540001  123.190002  122.190002  122.709999  240700        1.0
```

pandas의 기본기능으로 플로팅을 해본다. 

```python
aapl.Close.plot()
```

{% include ls/image.html
   src='20161016-apple-close-plot.svg'
   alt='기본기능으로 그려본 애플 주가 그래프'
   caption='기본기능으로 그려본 애플 주가 그래프'
%}

seaborn을 import하면 임포트한 것 만으로도 모양이 예뻐진다.

```python
import seaborn as sns
aapl.Close.plot()
```

{% include ls/image.html
   src='20161016-apple-close-plot-with-seaborn.svg'
   alt='seaborn을 import 한 후 애플 주가 그래프'
   caption='seaborn을 import 한 후 애플 주가 그래프' %}

제목과 축 설명을 달아주기 위해 아래와 같이 입력한다.

```python
ax = aapl.Close.plot(title='애플 주가')
ax.set_ylabel('주가(달러)')
```

{% include ls/image.html
   src='20161016_add-title.svg'
   alt='제목 추가'
   caption='제목을 추가했는데... ???' %}

## matplotlib 한글 사용 설정

matplotlib에서는 한글 폰트를 기본적으로 로드하지 않는다. matplotlib의 설정에서 한글이 있는 폰트를 지정하면 한글을 정상적으로 볼 수 있다.

```python
import matplotlib
import matplotlib.pyplot as plt

# 한글 폰트 사용시 마이너스 기호가 출력되지 않는 문제 수정
matplotlib.rcParams['axes.unicode_minus'] = False

# 한글 폰트 지정
matplotlib.rc('font', family=['Malgun Gothic'])

ax = aapl.Close.plot(title='애플 주가')
ax.set_ylabel('주가(달러)')
```

{% include ls/image.html
   src='20161016_add-title-with-korean-font.svg'
   alt='한글 설정 후 그래프'
   caption='한글 설정 후 그래프. 한글이 잘 나온다.' %}



