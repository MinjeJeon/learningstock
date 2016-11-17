---
title: freetype 업그레이드로 우분투 가독성 향상시키기
date: 2016-11-17 21:00 +0900
categories:
- linux
tags:
- ubuntu
- font
layout: post
published: true
---

우분투를 사용하면서 불만이었던 점 중 하나가 한글 렌더링이 좋지 않아 윈도우에 비해 글자 가독성이 상당히 떨어지는 것이다. 글자들이 윈도우와는 다르게 흐리멍텅하게 표시되어 크기가 작은 한글은 특히 알아보기 어려웠다.

{% include ls/image.html
   src='20161116_before_freetype_text.png'
   alt='alt_text'
   caption='freetype 업그레이드 전. 작은 글씨는 흐릿하다' %}

특히 ㅣ, ㅡ 같은 모음을 표시할 때 1픽셀씩 흐리게 번지는 현상은 가독성을 떨어트려 텍스트를 읽기 어렵게 만든다.  

{% include ls/image.html
   src='20161116_after_freetype_text.png'
   alt='freetype 업그레이드 후 세로, 가로획이 칼같아졌다'
   caption='freetype 업그레이드 후 세로, 가로획이 칼같아졌다' %}

9월에 새로 나온 freetype 2.7에서는 트루타입 인터프리터가 90년대에 사용된 기술에 기초한 v35에서 DirectWrite/클리어타입과 같이 LCD모니터에서 가독성을 높이는 기술이 적용된 v40으로 변경되어 가독성을 크게 높여준다고 한다.

{% include ls/image.html
   src='20161116_freetype-27-v35-v40-different-hinting.png'
   alt='기존 v35(위)와 v40(아래) 렌더링 비교'
   caption='기존 v35(위)와 v40(아래) 렌더링 비교, <a href="https://www.freetype.org/freetype2/docs/subpixel-hinting.html">freetype</a> 사이트에서 발췌' %}


현재 우분투 공식 리포지토리에는 올라와 있지 않아 ppa를 추가하고 apt로 설치하면 된다. infinality등 폰트 렌더링 최적화 라이브러리를 사용하고 있다면 먼저 제거하고 설치한다.
설치 방법은 <http://ubuntuhandbook.org/index.php/2016/09/install-freetype-2-7-ubuntu-16-04/>을 참고하였다.

Ctrl+Alt+T를 눌러 터미널을 열고 한줄씩 입력한다.

```bash
$ sudo add-apt-repository ppa:no1wantdthisname/ppa
$ sudo apt-get update
$ sudo apt-get install libfreetype6
```

모든 과정이 완료되면 재부팅하고 향상된 렌더링을 확인한다.

{% include ls/image.html
   src='20161116_freetype_before_after.png'
   alt='기존 버전(상단)과 새로운 버전(하단)비교 그림. 하단 그림에서<br>ㅡ, ㅣ 등의 글자가 작음에도 뚜렷하게 표시된다.'
   caption='기존 버전(상단)과 새로운 버전(하단)비교 그림. 하단 그림에서<br>ㅡ, ㅣ 등의 글자가 작음에도 뚜렷하게 표시된다.' %}