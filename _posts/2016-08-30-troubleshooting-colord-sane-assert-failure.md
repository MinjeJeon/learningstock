---
title: 우분투를 시작하자마자 '시스템 프로그램 오류를 발견했습니다'가 나온다면
date: 2016-08-30 21:00
categories:
- linux
tags:
- ubuntu
- troubleshooting
layout: post
published: true
image: 20160830_33b8a1ec_colord-sane-screenshot2.png
---

새 SSD를 사고 우여곡절 끝에(엔비디아 드라이버 문제로 무한 로그인 ㅜㅜ) 우분투를 설치하고 로그인을 하면 시스템 오류가 튀어 나온다. 

{% include ls/image.html
   src='20160830_277d5c0b_colord-sane-screenshot1.png'
   alt='시스템 프로그램 오류를 발견했습니다' %}

이 오류는 컴퓨터를 켤 때마다 매번 나오고, 시차들 두고 두번 튀어나와서 사람을 짜증나게 만들어준다. 앞으로 이런 오류를 무시한다고 해도 또! 또! 나온다

```colord-sane assert failure: colord-sane: simple-watch.c:454: avahi_simple_poll_prepare: Assertion `s->state == STATE_INIT || s->state == STATE_DISPATCHED || s->state == STATE_FAILURE' failed.
```

{% include ls/image.html
   src='20160830_33b8a1ec_colord-sane-screenshot2.png'
   alt='alt_text'
   caption='colord-sane?? 뭐라는건데??' %}

오류 보고로 보면 colord-sane 관련된 오류라는데.. 알 턱이 없으니 구글에서 검색한다.
[우분투 포럼의 해당 글](https://bugs.launchpad.net/ubuntu/+source/sane-backends/+bug/1351286)을 보면 우분투 14.10 부터 있어온 유서깊은 오류로, 최신 버전인 16.04버전까지도 발생하고 있다.

우분투 포럼의 반응은...

* 나도요
* 나도요
* 15.04 도요
* 15.04에서 아직도요!!
* 15.04에서 킬때마다요
* [2011년부터 4년째 이럼, 이런 망할 프로그램을 기본 설치에서 빼주면 안됨??](https://bugs.launchpad.net/ubuntu/+source/sane-backends/+bug/1351286#yui_3_10_3_1_1472558930635_612) \\
After update today sep 27 2015 I start to have the same problem, I have this problem on 3 ubuntu version from 2011. May be somebody try to remove this useless program from default installation? please! please!, **<u> 4 years you cant fix it, may be simple remove it and stop this hard sex with colord sane</u>** ) Thx developers this program! may be this gays start to working on ms windows? - linux is not right OS for this gays )\\
(깊은 빡침)
* 최신 15.10도요!! 왕짜증 난 html밖에 모르니 좀 고쳐봐요
* 나도요
* 16.04 인데 아직도임

colord-sane은 스캐너 관련 패키지이니, 스캐너 안쓰면 그냥 지워버리면 된다.([포럼 댓글 링크](https://bugs.launchpad.net/ubuntu/+source/sane-backends/+bug/1351286#yui_3_10_3_1_1472564839898_371))

```bash
$ sudo apt-get purge sane-utils
$ sudo apt-get purge colord
$ sudo apt-get autoremove
```

재부팅 해보면 오류 해결!!

