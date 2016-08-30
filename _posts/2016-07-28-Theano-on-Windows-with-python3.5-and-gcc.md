---
title: 윈도우에서 Theano, Python3.5, GCC 함께 사용하기
date: 2016-07-28 00:30
categories:
- 딥러닝
tags:
- theano
- windows
- troubleshooting
layout: post
published: true
---

윈도우에서 tensorflow를 사용할 수 없어 theano를 설치했는데, windows에서 사용할 때 g++를 사용할 수 없는 경우 성능하락에 대한 경고 메시지가 나온다.

근데 g++를 설치하고 theano를 임포트하면 에러가 뜨는데, libpython이 python 3.5용으로 아직 올라오지 않아서 그렇단다.

이틀 전에 github에 방법이 올라와서 소개한다. 이하 내용은 아래 링크의 번역이다.\\
<https://github.com/Theano/Theano/issues/3376#issuecomment-235034897>

1. mingw 설치\\
오른쪽 링크에서 파일 다운로드(32/64비트 맞게 선택) <http://tdm-gcc.tdragon.net/download>\\
옵션 중 컴파일러를 PATH를 추가해 주는 옵션을 꼭 선택한다.

1. 홈 디렉토리에서 .theanorc 파일 수정(없으면 새로 만들기)\\
홈 디렉토리가 어딘지 모르겠으면 탐색기 왼쪽에서 다운로드 누르고 한단계 올라가면 된다.
.theanorc 파일이 없으면 마우스 오른쪽 버튼을 눌러 새로 파일을 만들고, 이름은 .theanorc.txt 로 한다.\\
그리고 메모장에서 아래 내용을 추가한다. 아래부터는 기본값인 C:\TDM-GCC에 설치, 64비트 버전의 경우를 가정하였다.
        
        [gcc] 
        cxxflags = -shared -I"C:\TDM-GCC\include" -I"C:\TDM-GCC\x86_64-w64-mingw32\include" 

1. libpython35.a를 수동으로 만들고 설치
    * 아무 폴더나 새로 만든다.
    * python35.dll 파일을 새 폴더에 복사한다. (Anaconda 배포판의 경우 Anaconda3 폴더..)
    * 새 폴더에서 Shift+오른쪽 버튼을 클릭하고 '여기서 명령 창 열기'를 선택
    * 아래 명령을 차례로 실행

            > C:\TDM-GCC\x86_64-w64-mingw32\bin\gendef python35.dll
            > C:\TDM-GCC\x86_64-w64-mingw32\bin\dlltool --dllname python35.dll --def python35.def --output-lib libpython35.a

    * 만들어진 libpython35.a 파일을 파이썬 폴더\libs 에 복사한다.

이제 import theano를 입력하면 경고, 에러 없이 사용가능하다. 
