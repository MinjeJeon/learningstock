---
title: imwheel로 리눅스 휠 스크롤 속도 변경하기
date: 2016-07-08 20:47
tags:
- imwheel
- troubleshooting
- ubuntu
categories:
- linux
layout: post
---

리눅스를 처음 설치하고 브라우저로 인터넷을 이용할 때 당황스러웠던게 휠 스크롤 속도가 너무 느리다는 것이었다. 더 당황스러운 건 마우스 설정에 들어가면 휠 스크롤을 조정하는 메뉴가 아예 없다는 것 ㅜㅜ

인터넷을 찾아보니 **imwheel**이라는 프로그램을 사용하면 된다고 하는데, 설정도 어렵고 공식 문서에도 설명이 부실해서 설정하는데 애를 먹었다. 세부적으로 설정이 가능하긴 하지만 그냥 윈도우에서 잘 쓰던걸 이렇게까지 해야하는지 모르겠다.

## imwheel 설치하기

우분투 기준

```bash
$ sudo apt-get install imwheel
```

## imwheel 실행하기

```bash
$ imwheel
```
이렇게 하면 휠 스크롤 속도는 올라가는데, 5버튼 마우스를 사용하면 뒤로/앞으로 버튼이 안먹는다. 설정파일을 추가로 변경해야 한다.


## imwheel을 컴퓨터를 켤 때마다 실행시키기

```bash
$ sudo gedit /etc/X11/imwheel/startup.conf
```

'IMWHEEL\_START=0' 줄을 'IMWHEEL\_START=1'로 변경하고 저장

## imwheel 설정 파일 변경

스크롤 속도, 추가 버튼을 설정하려면 설정 파일을 수정해야 한다.

```bash
$ gedit ~/.imwheelrc
```

처음 파일을 열었을 때는 아래와 같이 되어있다. # 뒤는 주석으로 설명을 추가하였다.

```
".*" #적용 프로그램(정규식 매칭), 왼쪽은 전체 프로그램에 해당한다는 뜻
None,      Up,   Button4, 3 #같이 눌리는 키(ctrl, alt 등..), 입력버튼, 입력 시 동작, 연속으로 눌리는 횟수
None,      Down, Button5, 3
```

### 스크롤 속도 변경

<pre>
".*"
None,      Up,   Button4, <b>3</b> 
None,      Down, Button5, <b>3</b>
</pre>

굵게 표시된 숫자를 수정하면 스크롤 속도를 변경할 수 있다. 높을수록 많이 스크롤된다.
    
### 엄지 버튼 사용 가능하게 하기

".*" 항목 밑에 아래 내용을 추가한다

```
None, Thumb1, Alt_L|Left
None, Thumb2, Alt_L|Right
```

### 설정 파일에 수정한 내용 적용

```bash
$ imwheel -k
```

imwheel이 자동으로 재시작되면서 수정한 설정이 반영된다. 

## 참고

imwheel의 자세한 사용방법은 아래 링크에서 확인 가능  
imwheel manpage([http://imwheel.sourceforge.net/imwheel.1.html](http://imwheel.sourceforge.net/imwheel.1.html))  
imwheelrc 파일([http://apt-browse.org/browse/debian/wheezy/main/i386/imwheel/1.0.0pre12-9/file/etc/X11/imwheel/imwheelrc](http://apt-browse.org/browse/debian/wheezy/main/i386/imwheel/1.0.0pre12-9/file/etc/X11/imwheel/imwheelrc))

