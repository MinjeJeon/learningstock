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
---

2015년도 말인가 정확한 기억은 없다. 공모 형태로 안정적인 수익률을 보장한다는 선박펀드, 내부수익률법으로 7%의 안정적인 수익률. 10%가 넘는 현금 배당 실적으로 안정적인 투자처라고 생각했다. 물론 내가 사니까 주식은 떨어지기 시작했다. 주당 3000원에 달하는 주가는 슬슬 떨어지기 시작하더니 지금은 반토막난 1650원대를 오르내리락 하고 있다.

현재 청산 절차를 밟고 있는 한진해운을 국유화하겠다는 문재인의 발언? 이 모태가 되어 한진해운에 배를 빌려줬던 코리아xx호 펀드의 주가가 치솟기 시작하더니, 하이골드 주가도 널뛰기를 시작하였다. 그때 주식을 봤으면 당장 팔았을텐데, 현재는 원위치로 돌아와 이러지도 저러지도 못하는 상황이 되었다.

모든 금액을 

엑셀에는 불규칙한 현금흐름의 수익률을 계산해주는 엄청난 함수인 XIRR과 XNPV 함수가 있다. 
XIRR/XNPV와 동일한 역할을 하는 함수를 먼저 만들어보겠다.

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

이제 XNPV와 XIRR을 구하는 함수를 엑셀과 동일하게 만들어본다. 공학용/재무용 계산기로 IRR 구하는 방정식을 만들었던 추억을 생각하면 좋다.

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



결론:
이런건 엑셀로 하자!