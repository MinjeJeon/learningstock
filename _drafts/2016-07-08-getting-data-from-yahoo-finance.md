---
title: 야후 파이낸스 API를 이용하여 주가정보 수집하기
date: 2016-07-08 23:09
categories:
- 정보수집
tags:
- yahoo
- finance
- python
- pandas
- 주가
layout: post
---

주식정보 중 가장 기초적인 정보라고 할 수 있는 것이 주가정보이다. 현재 국내에서는 증권사에서 제공하고 있는 Open API를 이용하여 수집할 수 있으나, 증권사에 계좌 개설이 필요하고 각각의 API에 맞는 프로그램을 작성해야 하는 문제가 있어 아주 쉽지는 않다. 야후 파이낸스([http://finance.yahoo.com](http://finance.yahoo.com))에서는 별도 계좌개설이나 프로그램 설치 없이 다운로드 할 수 있는 API를 제공하고 있고, 파이썬에서 활용할 수 있는 API가 공개되어 있어 이용하기 가장 편리한 축에 든다. 데이터가 사전 형태로 제공되기 때문에 쉽게 pandas DataFrame형태로 변환하기 편리하다.

야후에서 제공하는 데이터에는 한국 상장기업 데이터도 포함되어 있다. 한국 상장회사 데이터를 받을 때는 꼭 주식코드 뒤에 '.KS'를 붙여야 다운로드할 수 있는 점만 주의하면 어려운 점은 없다.  
데이터를 받아 보니 회사 이름, 배당 정보, EPS 등을 제공하지 않아 본격적으로 활용하기에는 무리가 있으나, 간편하게 사용하기에는 충분한 정도라고 생각된다.

## Yahoo Finance API 설치

pip를 이용해 쉽게 설치할 수 있다.

```bash
$ pip install yahoo-finance
```

## Yahoo Finance API 사용하기

pip로 설치한 후 아래와 같이 import 한다

```python
from yahoo_finance import Share
```

예시로 삼성전자 주가정보를 다운받아 보려고 한다. 주식코드 뒤에 '.KS'를 꼭 붙여주여야 한다. get_info 메소드로 기본정보를 얻을 수 있다. 야후에서 제공하는 데이터에 문제가 있어 회사 이름이 출력되지 않는다.

```python
samsung = Share('005930.KS') # 객체 초기화
samsung.get_info() #삼성전자 기본정보
```

```
Output:
{'CompanyName': None,
 'end': '2016-07-10',
 'start': '2000-01-04',
 'symbol': '005930.KS'}
```


시계열 주가정보를 다운받기 위해서는 get_historical 메소드를 사용하여 자료를 다운로드한다.  

```python
samsung.get_historical('2016-07-04','2016-07-08')
```

```
Output:
[{'Adj_Close': '1460000.00',
  'Close': '1460000.00',
  'Date': '2016-07-08',
  'High': '1475000.00',
  'Low': '1449000.00',
  'Open': '1450000.00',
  'Symbol': '005930.KS',
  'Volume': '269900'},
...
 {'Adj_Close': '1466000.00',
  'Close': '1466000.00',
  'Date': '2016-07-04',
  'High': '1474000.00',
  'Low': '1451000.00',
  'Open': '1464000.00',
  'Symbol': '005930.KS',
  'Volume': '159900'}]
```

데이터가 사전의 리스트로 제공되기 때문에 pandas DataFrame형태로 변환하기 쉽다. 먼저 pandas, DataFrame, Series를 import한다.

```python
import pandas as pd
from pandas import DataFrame, Series
```

주가정보를 DataFrame형태로 변환하여 출력한다.

```
df = DataFrame(samsung.get_historical('2016-07-04','2016-07-08'))
df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>Adj_Close</th>
      <th>Close</th>
      <th>Date</th>
      <th>High</th>
      <th>Low</th>
      <th>Open</th>
      <th>Symbol</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1460000.00</td>
      <td>1460000.00</td>
      <td>2016-07-08</td>
      <td>1475000.00</td>
      <td>1449000.00</td>
      <td>1450000.00</td>
      <td>005930.KS</td>
      <td>269900</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1450000.00</td>
      <td>1450000.00</td>
      <td>2016-07-07</td>
      <td>1450000.00</td>
      <td>1416000.00</td>
      <td>1421000.00</td>
      <td>005930.KS</td>
      <td>229900</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1421000.00</td>
      <td>1421000.00</td>
      <td>2016-07-06</td>
      <td>1452000.00</td>
      <td>1412000.00</td>
      <td>1447000.00</td>
      <td>005930.KS</td>
      <td>334900</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1469000.00</td>
      <td>1469000.00</td>
      <td>2016-07-05</td>
      <td>1475000.00</td>
      <td>1462000.00</td>
      <td>1466000.00</td>
      <td>005930.KS</td>
      <td>157400</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1466000.00</td>
      <td>1466000.00</td>
      <td>2016-07-04</td>
      <td>1474000.00</td>
      <td>1451000.00</td>
      <td>1464000.00</td>
      <td>005930.KS</td>
      <td>159900</td>
    </tr>
  </tbody>
</table>
</div>

