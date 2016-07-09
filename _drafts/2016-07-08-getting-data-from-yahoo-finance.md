---
title: 야후 파이낸스 API를 이용하여 주가정보 수집하기
date: 2016-07-08 23:09
categories:
- 정보수집
tags:
- yahoo
- finance
- 주가
layout: post
---

주식정보 중 가장 기초적인 정보라고 할 수 있는 것이 주가정보이다. 기초적인
현재 국내에서는 증권사에서 제공하고 있는 Open API를 이용하여 수집할 수 있으나, 증권사에 계좌 개설이 필요하고 각각의 API에 맞는 프로그램을 작성해야 하는 문제가 있어 아주 쉽지는 않음.
파이썬으로 쉽게 수집할 수 있다.
야후 파이낸스([http://finance.yahoo.com](http://finance.yahoo.com)) api를 이용하여 공개되어있다.

배당 관련된 정보에 대해서는 부족한 편이다.
주가정보를 수집

## Yahoo Finance API 설치
```bash
$ pip install yahoo-finance
```
pip를 이용해 쉽게 설치할 수 있다.

## Yahoo Finance API 사용하기
Yahoo Finance API
```python
import pandas as pd
from pandas import DataFrame, Series
```

```python
from yahoo_finance import Share
```