---
title: xing-plus로 이베스트증권 주가정보 다운받기
date: 2016-09-05 21:45 +0900
categories:
- 정보수집
tags:
- xing
- eBEST
- API
- python
image: 20160905_87703e64_eBEST_DevCenter.png
layout: post
published: true
---

32bit Anaconda 배포판으로 
pip를 이용하면 쉽게 다운받을 수 있다.

## 설치하기

visual studio가 설치되지 않은 컴퓨터에서는 ta-lib를 설치할 수 없어서 비공식 컴파일된 패키지 <http://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib>에서 다운로드 받아서 설치한다. 파일을 다운로드 하고, 받은 폴더에서 아래 명령을 실행한다. 

```
> pip install TA_Lib-0.4.10-cp35-cp35m-win32.whl
> conda install pywin32 pandas 
```

```
> pip install xing-plus
```

## 로그인하기

xing-plus로 로그인하기는 
