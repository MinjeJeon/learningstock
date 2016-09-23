---
title: 우분투에서 창 크기 조절할 때 버벅거린다면
date: 2016-09-19 00:33 +0900
categories:
- linux
tags:
- ubuntu
- troubleshooting
layout: post
published: true
---

터미널을 열고 ccsm

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


일반 - 기본 창 크기 조절 모드에서 
{% include ls/image.html
   src='20160919_compiz-setting-2.png'
   alt='compiz-setting-1'
   caption='' %}
