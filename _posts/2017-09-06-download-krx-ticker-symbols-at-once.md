---
title: 파이썬 코드 한줄로 종목코드 한번에 다운받기
date: 2017-09-07 23:27 +0900
categories:
- 정보수집
tags:
- python
- KRX
- KOSPI
- KOSDAQ
- KONEX
layout: post
published: true
---

[야후 파이낸스 API를 이용하여 주가정보 수집하기]에서는 종목코드(주식코드)를 하나씩 입력해야 주가정보를 다운로드 할 수 있습니다. 코스피나, 코스닥 전체의 정보를 받고 싶으면 시장에 속해 있는 기업들의 종목코드 리스트를 알아야겠죠?

[야후 파이낸스 API를 이용하여 주가정보 수집하기]: {{ site.baseurl }}{% post_url 2016-07-08-getting-data-from-yahoo-finance %}

<http://financialfreedom.kr/834-2/>에 종목코드를 한번에 받을 수 있는 쉬운 방법이 올라와 있어서 파이썬으로 리스트를 바로 받을 수 있게 만들어 봤어요. 파이썬을 안 쓰고 엑셀로 받으시려면 링크의 글을 참고하세요.

## pandas 한줄로 종목코드 다운받기

pandas의 read\_html 기능을 이용하여 인터넷에 있는 테이블을 한줄로 불러옵니다. pandas에서 파일을 읽어들이는 함수들은 인터넷 주소를 줘도 알아서 잘 받아와요.

```python
import pandas as pd

df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]

df.head()
```

인터넷 브라우저에서 엑셀 파일 다운로드 버튼을 누를 때에는 엑셀 파일이 다운로드 되는데, 다운로드 된 파일의 실제 내용은 html 테이블이기 때문에 read\_excel 대신 read\_html 함수로 불러옵니다.

```
Out:
     회사명  종목코드                                         업종  \
0       BYC      1460                              봉제의복 제조업
1    CJ CGV     79160  영화, 비디오물, 방송프로그램 제작 및 배급업
2  CJ씨푸드     11150                             기타 식품 제조업
3   DSR제강     69730                              1차 철강 제조업
4    KB금융    105560                                  기타 금융업

                                                          주요제품  \
0  메리야스,란제리 제조,도매/건축공사/부동산 임대,분양,공급......
1                               영화상영,영화관 운영
2     수산물(어묵,맛살)가공품 도매,원양수산업,수출입
3  와이어로프,각종 경강선,철선제품,PC강선,아연도 강연선 제조......
4                                                  -

       상장일 결산월                  대표자명                  홈페이지  \
0  1975-06-02   12월                  유 중 화      http://www.byc.co.kr
1  2004-12-24   12월                     서 정      http://www.cgv.co.kr
2  1988-11-26   12월  유병철, 강신호(각자대표)  http://www.cjseafood.net
3  2003-01-28   12월                    홍하종    http://www.dsrcorp.com
4  2008-10-10   12월                    윤종규       http://www.kbfg.com

         지역
0  서울특별시
1  서울특별시
2      경기도
3    전라남도
4  서울특별시
```

종목코드 부분이 6자리 숫자로 나오지 않기 때문에 앞자리를 0으로 채워줍니다.

```python
df.종목코드 = df.종목코드.map('{:06d}'.format)
df.종목코드.head()
```

```
Out:
0    001460
1    079160
2    011150
3    069730
4    105560
Name: 종목코드, dtype: object
```

위에 잘 보면... 시장구분이 빠져 있어요. 엑셀 양식에 시장구분이 빠져 있어서 그런데, 시장을 구분하려면 다운받을 URL의 파라미터를 조정하면 됩니다. 하지만 일일이 하려면 귀찮잖아요? 그래서 코드를 만들어 놨어요. 아래 코드를 실행시키세요. 위 내용의 종합판입니다.

```python
import urllib.parse
import pandas as pd

MARKET_CODE_DICT = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt',
    'konex': 'konexMkt'
}

DOWNLOAD_URL = 'kind.krx.co.kr/corpgeneral/corpList.do'

def download_stock_codes(market=None, delisted=False):
    params = {'method': 'download'}

    if market.lower() in MARKET_CODE_DICT:
        params['marketType'] = MARKET_CODE_DICT[market]

    if not delisted:
        params['searchType'] = 13

    params_string = urllib.parse.urlencode(params)
    request_url = urllib.parse.urlunsplit(['http', DOWNLOAD_URL, '', params_string, ''])

    df = pd.read_html(request_url, header=0)[0]
    df.종목코드 = df.종목코드.map('{:06d}'.format)

    return df
```

이제 코스닥 시장의 종목코드를 한꺼번에 받아볼까요?

```python
kosdaq_stocks = download_stock_codes('kosdaq')
kosdaq_stocks.head()
```

```
Out:
           회사명 종목코드                       업종               주요제품  \
0          CJ E&M   130960            텔레비전 방송업       방송게임영화음악
1    CJ프레시웨이   051500   음·식료품 및 담배 도매업   식자재유통, 단체급식
2  GMR 머티리얼즈   032860  해체, 선별 및 원료 재생업               철스크랩
3   IBKS제5호스팩   254120         금융 지원 서비스업           기업인수합병
4          KD건설   044180                건물 건설업  몰드베이스(Mold Base)

       상장일 결산월 대표자명                     홈페이지        지역
0  2010-10-15   12월   김성수         http://www.cjenm.com  서울특별시
1  2001-07-26   12월   문종석    http://www.cjfreshway.com      경기도
2  1997-07-04   12월   김동은  http://www.gmrmaterials.com    충청남도
3  2016-12-02   12월   김형준                          NaN  서울특별시
4  2000-11-16   12월   구정회      http://dymoldtech.co.kr      경기도
```

[야후 파이낸스 API를 이용하여 주가정보 수집하기]에서 나온 방법대로 위에 나와있는 5개 종목의 최근 수정주가를 출력해보자.

```python
from pandas_datareader import data

results = {}
for code in kosdaq_stocks.종목코드.head():
    results[code] = data.DataReader(code + '.KQ', 'yahoo', '2017-01-01', None)

df = pd.concat(results, axis=1)
df.loc[:, pd.IndexSlice[:, 'Adj Close']].tail()
```

```
Out:
              032860    044180    051500    130960    254120
           Adj Close Adj Close Adj Close Adj Close Adj Close
Date
2017-09-01     635.0     213.0   41550.0   75600.0    2070.0
2017-09-04     624.0     207.0   40400.0   75000.0    2070.0
2017-09-05     625.0     207.0   40750.0   75100.0    2040.0
2017-09-06     619.0     211.0   38250.0   76900.0    2055.0
2017-09-07     620.0     211.0   39000.0   77000.0    2060.0
```