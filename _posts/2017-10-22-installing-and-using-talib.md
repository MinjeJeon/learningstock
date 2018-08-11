---
title: 주가의 기술적 분석을 위한 ta-lib 설치하기
date: 2018-04-07 16:46 +0900
categories:
- 기술적 분석
tags:
- python
- ta-lib
layout: post
image: 
published: true
---


주가 차트를 기술적으로 분석하기 위한 지표들과 공식에 대한 설명은 인터넷에 많이 나와있지만, 직접 만드는 법에 대해서는 나와있는 글이 많지 않습니다. 공식을 실제 코드로 구현해 보는 것도 좋지만, 그러기에는 낭비하는 시간이 너무 많잖아요? 공식들을 빠르게 계산하는 알고리즘은 이미 나와 있으니, 가져와서 사용만 해 봅시다.

## ta-lib 설치하기

{% include ls/image.html
   src='20180407_talib_homepage.png'
   alt='ta-lib 홈페이지'
   caption='ta-lib 홈페이지(<a href="https://www.ta-lib.org/">https://www.ta-lib.org/</a>)' %}

원래 ta-lib 는 c로 작성되어 있지만, 파이썬에서 사용할 수 있도록 wrapper가 만들어져 있습니다. anaconda로는 python 3용 라이브러리가 아직 나와있지 않아서 pip로 설치가 가능합니다.

```bash
$ pip install ta-lib
```

리눅스 사용자는 별 에러 없이 설치가 될 테지만, 윈도우를 사용하는 경우 비주얼 스튜디오나 minGW 등의 컴파일러가 설치되어 있지 않다면 아래와 같이 오류를 뿜어냅니다.

{% include ls/image.html
   src='20180407_talib_install_failed.png'
   alt='pip에서 ta-lib 설치 실패 화면'
   caption='pip에서 ta-lib 설치 실패 화면(윈도우)' %}

### 방법 1. 비주얼 스튜디오 설치

비주얼 스튜디오(<https://www.visualstudio.com/ko/downloads/>)를 설치합니다. 용량이 크고 설치가 오래 걸려서 ta-lib만 사용하려면 추천하지는 않습니다.

### 방법 2. Unofficial Windows Binary 다운로드

캘리포니아 대학교 어바인 캠퍼스에서 컴파일러 없이도 파이썬 라이브러리를 설치할 수 있도록 미리 컴파일된 파이썬 패키지를 올려 놓았습니다. <https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib>에서 버전에 맞는 파일을 다운로드해서 아래와 같이 설치합니다.

```bash
# python 3.6/64비트 버전 사용시
$ pip install TA_Lib-0.4.10-cp36-cp36m-win_amd64.whl
```

## ta-lib 사용해 보기

ta-lib를 설치했으면 간단하게 한번 사용해 봅시다. 신라젠(215600) 의 일간 주가 데이터를 가지고 이동평균을 계산해 보겠습니다.

### 데이터 가져오기

pandas_datareader를 이용하여 데이터를 불러옵니다. 

```python

import talib.abstract as ta
from pandas_datareader import data

sillajen = data.DataReader('215600.KQ','yahoo', '2017-01-01', '2018-01-31')\
    .dropna(how='all')\
    .rename(columns=lambda col:col.lower()) # 컬럼 이름을 소문자로 변경
```

ta-lib의 abstract API를 이용하면 Series나 numpy array 대신 OHLC(시가, 고가, 저가, 종가) 데이터가 들어있는 DataFrame 객체를 그냥 넣어도 계산해 줍니다.

```python
# ta-lib로 5기간 종가 이동평균 계산
talib_ma5 = ta.MA(sillajen, timeperiod=5)

# pandas 기능을 이용하여 5기간 이동평균 계산
pandas_ma5 = sillajen.close.rolling(window=5).mean() 

talib_ma5.equals(pandas_ma5)
# True / 결과는 같음  
```

그리고 pandas의 기능만 이용했을 때보다 7배 빨랐습니다. 많은 데이터를 가지고 기술적 지표를 계산한다면 ta-lib를 꼭 사용해아겠네요.

```python
%timeit ta.MA(sillajen, timeperiod=5)
# 39.7 µs ± 2.72 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit sillajen.close.rolling(window=5).mean()
# 280 µs ± 19 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

