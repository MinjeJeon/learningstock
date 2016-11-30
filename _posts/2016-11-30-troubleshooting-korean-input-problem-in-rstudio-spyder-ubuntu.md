---
title: 우분투에서 spyder, rstudio 한글 입력 문제 해결
date: 2016-11-29 16:30 +0900
categories:
- linux
tags:
- ubuntu
- spyder
- python
- rstudio
layout: post
published: true
---

## spyder에서 한글 입력이 안될때[^spyder1]

ibus를 사용한다

```bash
$ im-config -n ibus
```

재부팅하고 ibus 설정 \\
참고: <http://blog.daum.net/bagjunggyu/191>

## rstudio에서 한글 입력이 안될때(1)[^rstudio1]

[일본 블로그(いくやの斬鉄日記)](http://blog.goo.ne.jp/ikunya/e/8508d21055503d0560efc245aa787831)에서 패치한 fcitx를 사용한다.

임시 디렉토리로 이동해서 파일을 다운받고 설치한다.

```bash
$ wget http://ikuya.info/tmp/fcitx-qt5-rstudio.tar.gz
$ tar xf fcitx-qt5-rstudio.tar.gz
$ cd fcitx-qt5-rstudio
$ sudo apt install ./fcitx-frontend-qt5-rstudio_1.0.5-1_amd64.deb ./libfcitx-qt5-1-rstudio_1.0.5-1_amd64.deb
```

## rstudio에서 한글 입력이 안될때(2)[^rstudio2]

rstudio-server를 설치한다 \\
참고: <https://www.rstudio.com/products/rstudio/download-server/>

```bash
$ sudo apt-get install r-base gdebi-core
$ wget https://download2.rstudio.org/rstudio-server-1.0.44-amd64.deb
$ sudo gdebi rstudio-server-1.0.44-amd64.deb
```
(현재 최신 버전인 64bit rstudio-server 1.0.44 기준)

설치 후 웹브라우저에서 <http://127.0.0.1:8787>로 접속

그냥 윈도우 쓰자!


[^spyder1]: 16.04, 16.10에서 해봄 
[^rstudio1]: 16.04에서 해봄
[^rstudio2]: 16.04, 16.10에서 해봄

