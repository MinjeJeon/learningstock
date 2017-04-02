---
title: 선박펀드 주가 예측하기 (하이골드3호)
date: 2017-03-24 20:05 +0900
categories:
- 가치평가
tags:
- python
- IRR
- NPV
layout: post
published: true
image: 20170328_higold3_chart.PNG
---

2015년도 말인가 정확한 기억은 없다. 공모 형태로 안정적인 수익률을 보장한다는 선박펀드, 내부수익률법으로 7%의 안정적인 수익률. 10%가 넘는 현금 배당 실적으로 안정적인 투자처라고 생각했다. 물론 내가 사니까 주식은 떨어지기 시작했다. 주당 3000원에 달하는 주가는 슬슬 떨어지기 시작하더니 지금은 반토막난 1650원대를 오르내리락 하고 있다.

현재 청산 절차를 밟고 있는 한진해운을 국유화하겠다는 한 대권주자의 발언과 함께 한진해운에 배를 빌려줬던 코리아xx호 펀드의 주가가 치솟기 시작하더니, 하이골드 주가도 널뛰기를 시작하였다. 그때 주식을 봤으면 당장 팔았을텐데, 현재는 원위치로 돌아와 이러지도 저러지도 못하는 상황이 되었다.

그나마 지금은 유동성이라도 생겨서 다행이지, 예전에는 진짜 10주도 거래 안됐었다. 한진해운님 고맙습니다 ㅜㅜ


## 현재 경영진은 하이골드 3호를 어떻게 평가하고 있는가?

우리에게 매달 배당금을 지급하고 있는 하이골드 3호의 경영진은 

{% include ls/image.html
   src='20170401_higold3_disclosure.png'
   alt='하이골드 3호 예상투자수익률 공시'
   caption='예상투자수익률을 -3.63%, 과연 적절한 것인가?' %}

가정 - 현재의 선박을 매각, 모든 배당 수익률과 투자원금을 내부수익률(IRR) 방식으로 계산한다고 한다.

지금까지의 현금흐름을 바탕으로 현재 예상되는 선가가 어느 정도인지, 지금의 주가와 대비해서는 어느정도 차이가 나는지 알아보려고 한다. 지금보다 주가가 고평가 되어 있다 하면 지금 당장 파는게 나을 것이다. 경영진의 판단은 언제나 자신의 펀드에 대해 고평가를 할 것이기 때문이다.

4\. 기타 투자판단과 관련된 중요사항에서는 예상 투자수익률이 목표수익률(7%)를 초과하는 경우 매각이 즉시 가능하다고 하는데, 어느정도 되어야 하는지 알려주겠다!!


모든 금액을 가지고 

엑셀에는 불규칙한 현금흐름의 현재가치 및 수익률을 계산해주는 엄청난 함수인 XIRR과 XNPV 함수가 있다. 파이썬에는 만들어 줄 법도 한데 없어 보여서 XIRR/XNPV와 동일한 역할을 하는 함수를 먼저 만들어 본다.

그전에 기본 import 함수를 준비하고, xnpv, xirr이 잘 만들어졌는지 테스트할 데이터를 준비한다.

```python
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from scipy import optimize

#테스트를 위한 예제 데이터 생성. NPV는 0, IRR은 5%
npv_test_case = {'20130101':-300,
                 '20140101': 100*(1.05),
                 '20150101': 100*(1.05**2),
                 '20160101': 100*(1.05**3)}

# Series 형태로 만들고, index는 날짜 형태로
test_case_series = Series(npv_test_case)
test_case_series.index = pd.to_datetime(test_case_series.index)

print(npv_test_case)
```
```
2013-01-01   -300.0000
2014-01-01    105.0000
2015-01-01    110.2500
2016-01-01    115.7625
dtype: float64
```

이제 XNPV와 XIRR을 구하는 함수를 엑셀과 동일하게 만들어본다. 공학용/재무용 계산기로 IRR을 구해봤던 추억을 생각하면 좋다.

```python
# cfs = 날짜 인덱스 / 숫자 값을 가진 Series
# https://github.com/peliot/XIRR-and-XNPV/blob/master/financial.py 의 식을 변형
def pd_xnpv(cfs, rate):
    time_delta = cfs.index - cfs.index.min()
    years = time_delta.days / 365 #엑셀의 XNPV와 동일(1년=365일)
    npv_series = cfs/((1+rate) ** years)
    return npv_series.sum()

def pd_xirr(cfs, guess=0.01):
    func = lambda rate: pd_xnpv(cfs, rate)
    return optimize.newton(func, guess)
```

앞에서 만들었던 test\_case\_series로 테스트 해보자

```python
print("할인율이 5%%인 경우 테스트 케이스의 NPV는 %.1f" % pd_xnpv(ser, 0.05))
print("따라서 내부수익률은 %.1f%%입니다." % (pd_xirr(ser) * 100))
```
```
할인율이 5%인 경우 테스트 케이스의 NPV는 0.0
따라서 내부수익률은 5.0%입니다.
```

잘 나왔으니 다음 단계로 진행

하이골드 3호의 현재까지의 현금흐름 시계열을 만든다. 월별 분배금을 연말로 몰았으니 NPV, IRR을 약간 과소평가하게 된다. 보수적인 추정이니 괜찮지 않을까 싶다.

```python
higold3_rawdata = {'20120302':-81749224580,
                   '20121231':  5523203046,
                   '20131231':  5636925260,
                   '20141231':  5636924988,
                   '20151231':  5652411406,
                   '20161231':  5185366035}
shares_higold3 = 16149790 # 하이골드 3호의 주식수

# xnpv, xirr함수를 사용하기 위한 Series 만들기. 위의 테스트 케이스 생성과 동일한 방법
def raw_to_series(dictionary):
    result = Series(dictionary)
    result.index = pd.to_datetime(result.index)
    return result

higold3 = raw_to_series(higold3_rawdata)
print(higold3.map('{:,.0f}'.format)) # 3자리 콤마
```
```
2012-03-02    -81,749,224,580
2012-12-31      5,523,203,046
2013-12-31      5,636,925,260
2014-12-31      5,636,924,988
2015-12-31      5,652,411,406
2016-12-31      5,185,366,035
2017-01-31        353,967,867
2017-02-28        320,783,500
2017-03-31        298,660,488
2017-04-28        353,967,867
dtype: object
```

## IRR을 알고 있다고 가정할 때 현재의 주가를 추정

2017년 4월 1일을 기준으로 할 때

지금 즉시 현금흐름이 발생한다고 가정하면

higold3_0401 = higold3[:'20170331']

임의의 함수를 만들어서 값을 추정해낸다.



결론:
이런건 엑셀로 하자!