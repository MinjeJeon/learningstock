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

주식정보 중 가장 기초적인 정보라고 할 수 있는 것이 주가정보이다. 현재 국내에서는 증권사에서 제공하고 있는 Open API를 이용하여 수집할 수 있으나, 증권사에 계좌 개설이 필요하고 각각의 API에 맞는 프로그램을 작성해야 하는 문제가 있어 아주 쉽지는 않다. 야후 파이낸스([http://finance.yahoo.com](http://finance.yahoo.com))에서는 별도 계좌개설이나 프로그램 설치 없이 다운로드 할 수 있는 API를 제공하고 있고, 파이썬에서 활용할 수 있는 API가 공개되어 있어 이용하기 가장 편리한 축에 든다.

야후에서 제공하는 데이터에는 한국 상장주식 데이터도 포함되어 있다. 데이터를 받을 때는 꼭 주식코드 뒤에 '.KS'를 붙여야 다운로드할 수 있다.
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