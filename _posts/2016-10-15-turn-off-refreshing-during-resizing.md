---
title: 우분투에서 창 크기 조절할 때 버벅거린다면
date: 2016-10-15 13:30 +0900
categories:
- linux
tags:
- ubuntu
- troubleshooting
layout: post
published: true
---

우분투 기본 설치 상태에서 보통은 창 크기를 조절할 때 버벅거리지는 않지만, 크롬 창 크기를 조절할 때 특히 많이 버벅거린다. 크기가 조절되면 화면이 갱신되는데 이 속도가 많이 느리다.

이런 경우 터미널을 열고 ccsm을 연다

```bash
$ ccsm
```

안된다면 compizconfig-settings-manager 패키지를 설치한다.

```bash
$ sudo apt-get install compizconfig-settings-manager
```

창 관리 - 창 크기 조절을 선택한다
{% include ls/image.html
   src='20160919_compiz-setting-1.png'
   alt='compiz-setting-1'
   caption='' %}


일반 - 기본 창 크기 조절 모드에서 기본 대신 사각형 등을 선택한다.
{% include ls/image.html
   src='20160919_compiz-setting-2.png'
   alt='compiz-setting-2'
   caption='' %}

Cinnamon 3.0 등 다른 데스크탑을 환경을 설치하면 이런 설정 없어도 해결된다.
<http://www.omgubuntu.co.uk/2016/04/how-to-install-cinnamon-3-0-on-ubuntu>
