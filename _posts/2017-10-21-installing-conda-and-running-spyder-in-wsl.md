---
title: Windows Subsystem for Linux(WSL)에서 anaconda 설치 및 spyder 사용하기
date: 2017-10-21 20:13 +0900
categories:
- linux
tags:
- WSL
- anaconda
- python
- troubleshooting
layout: post
image: 20171021_Multi-distro-1280x838.png 
published: true
---

Windows 10에서도 맥이나 리눅스처럼 bash를 사용할 수 있게 되었습니다. Anniversary update에 추가된 기능인 Windows Subsystem for Linux(WSL) 덕택인데요. 64비트 Windows 10을 사용하면서 업데이트를 제때 했다면 누구나 사용 가능합니다. 기존에 mingw나 cygwin같이 리눅스 환경을 에뮬레이팅 하는 것이 아닌 리눅스 바이너리를 윈도우에서 직접 동작하게 하는 방법이라 속도 면에서도 빠르고, 우분투를 만드는 캐노니컬과의 제휴로 apt를 이용해 패키지를 다운로드 할 수 있습니다. 콘솔만 사용한다면 실제 우분투에 가까운 수준으로 지원하고 있어요. 윈도우를 사용하면서 불가피하게 리눅스 바이너리를 사용해야 하는 경우에는 유용하게 쓸 수 있을 것 같네요. 설치 방법은 [영문 링크], [한글 링크]를 참고하면 됩니다. 영어 쪽 설명이 좀 더 자세하기는 하지만 한글로도 설명은 충분하니 아직 설치하지 않으신 분이시라면 한글 링크로 들어가서 설치 방법을 참고하세요.

[영문 링크]: https://msdn.microsoft.com/en-us/commandline/wsl/install_guide
[한글 링크]: https://blogs.msdn.microsoft.com/eva/?p=7633

데이터 분석을 위한 python 배포 환경인 anaconda도 리눅스와 동일한 방식으로 설치 가능합니다. 일반 리눅스에서처럼 wget으로 파일을 받아도 되고, 윈도우에서 브라우저를 이용해서 다운로드 받은 파일도 무방합니다. 여기서는 wget으로 다운받아서 설치해 볼게요. 

```bash
# 다운로드 받을 폴더로 이동한 후에 실행. Anaconda 파일 이름은 17.10.21 기준 최신버전입니다.
$ wget https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh
$ ./Anaconda3-5.0.0.1-Linux-x86_64.sh
```

그리고 패키지를 업데이트 하려는데....

```
$ conda update --all

Fetching package metadata ...
CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.continuum.io/pkgs/main/linux-64/repodata.json.bz2>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.
SSLError(MaxRetryError('HTTPSConnectionPool(host=\'repo.continuum.io\', port=443): Max retries exceeded with url: 
/pkgs/main/linux-64/repodata.json.bz2 (Caused by SSLError("Can\'t connect to HTTPS URL because the SSL module is not available.",))',),)
```

## WSL에서 conda가 작동하지 않을 때

에러문을 보니 SSLError라고 나오네요. wget로 받을때는 문제가 없었는데.. 인터넷을 찾아보니 원래 openssl에는 문제가 없었습니다. 설치 시에 anaconda를 path에 등록하겠냐고 하면 자동으로 ananconda의 실행파일들을 먼저 참조하도록 수정하는데, openssl 또한 anaconda의 것을 사용하다 보니 문제가 발생하는 것으로 보입니다. 패치 전까지는 아래와 같은 방법으로 해결할 수 있어요.

```bash
$ which openssl
/home/사용자명/anaconda3/bin/openssl # 이 부분이 문제에요.
$ sudo apt install execstack
$ execstack -c anaconda3/lib/libcrypto.so.1.0.0
$ conda update --all # 정상 작동!
```

## 윈도우 GUI의 spyder와 linux의 커널 연결하기

WSL에서도 GUI프로그램을 돌릴 수 있긴 하지만, 정식으로 돌릴 수 있는 건 아닙니다. 그래서 WSL에서 파이썬 개발할 때는 jupyter notebook을 많이 이용하는데요. 윈도우의 spyder로도 커널을 연결하여 리눅스의 ipython 코드를 작동시킬 수 있어요.

WSL의 bash에서 ipython kernel을 실행시키면 아래와 같이 메시지가 나오는데요. 밑에 보시면 다른 클라이언트를 이 커널에 연결시키려면.. 이라고 나와있는데, 아래 json 파일의 숫자를 기억했다가 윈도우의 spyder와 연결 시켜줍니다.

```
$ ipython kernel
NOTE: When using the `ipython kernel` entry point, Ctrl-C will not work.

To exit, you will have to explicitly quit this process, by either sending
"quit" from a client, or using Ctrl-\ in UNIX-like environments.

To read more about this, see https://github.com/ipython/ipython/issues/2049


To connect another client to this kernel, use:
    --existing kernel-37.json
```

윈도우의 spyder에서 아래와 같이 메뉴를 선택한 후에..

{% include ls/image.html
   src='20171021_spyder_existing_kernel_menu.png'
   alt='spyder 커널 메뉴에서 connect existing kernel 선택' %}

Browse 버튼을 눌러 json 파일을 선택해 줍니다.

{% include ls/image.html
   src='20171021_spyder_connect_existing_kernel_window.png'
   alt='connect existing kernel 선택, browse 메뉴를 눌러 json 파일을 선택' %}

WSL에 있는 json 파일을 선택해야 하니까, %localappdata%\Lxss\home\사용자명\\.local\share\jupyter\runtime 폴더에서 json 파일을 찾아서 선택합니다. 그럼 아래와 같이 연결이 되는데.. 되긴 하는데..

{% include ls/image.html
   src='20171021_spyder_wsl.png'
   alt='spyder와 WSL의 ipython kernel이 연결된 모습'
   caption='윈도우에서 sys.platform이 linux?? 연결은 잘 되었지만..' %}

인터럽트, 재시작이 안 되네요.. variable explorer, help도 작동하지 않아서 spyder의 셀을 실행시킬 수 있다는 점 이외에는 의미 없어 보입니다. spyder의 장점은 하나도 활용 못하고, 안되는 기능만 더 많으니 그냥 jupyter notebook을 쓰는 게 좋겠네요. 잘 돌아가니까.
