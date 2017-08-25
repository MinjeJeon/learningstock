---
title: 윈도우용 python 3.6에서 hdf5 파일이 열리지 않을 때
date: 2017-08-26 00:54 +0900
categories:
- python
tags:
- windows
- python3.6
- pandas
- hdf5
- troubleshooting
layout: post
published: true
---

python 3.6이 새로 나오고 나서 신나게 업그레이드를 한 후에 데이터 파일을 열어보았다. 생전 처음 보는 에러를 뿜으며 열리지가 않는다. 아닛!! 데이터가 다 날라간건가?? 라는 생각이 들 정도로 멘붕이 왔다. 파이썬 코드라면 어떻게 소스라도 볼텐데 c extension쪽에서 뻗어버리니 손쓸 방도가 없다.

```python
import pandas as pd
from pandas import DataFrame
df = DataFrame([[1,2],[3,4]])
store = pd.HDFStore(r'C:\오리\store.h5')
store['df'] = df
store['df']
```

```
.......
  File "tables\hdf5extension.pyx", line 488, in tables.hdf5extension.File._g_new (tables\hdf5extension.c:6017)

HDF5ExtError: HDF5 error back trace

  File "C:\aroot\work\hdf5-1.8.15-patch1\src\H5F.c", line 522, in H5Fcreate
    unable to create file
  File "C:\aroot\work\hdf5-1.8.15-patch1\src\H5Fint.c", line 1001, in H5F_open
    unable to open file: time = Sat Aug 26 01:16:21 2017
, name = 'C:\오리\store.h5', tent_flags = 13
  File "C:\aroot\work\hdf5-1.8.15-patch1\src\H5FD.c", line 993, in H5FD_open
    open failed
  File "C:\aroot\work\hdf5-1.8.15-patch1\src\H5FDsec2.c", line 343, in H5FD_sec2_open
    unable to open file: name = 'C:\오리\store.h5', errno = 22, error message = 'Invalid argument', flags = 13, o_flags = 302

End of HDF5 error back trace

Unable to open/create file 'C:\오리\store.h5'
```

인터넷 검색 끝에 윈도우에서 사용하는 파일 인코딩을 [PEP 529]에서 바꾸었는데 hdf5쪽만 윈도우 python 3.6 대응이 안 된 것 같다.

[PEP 529]: https://docs.python.org/3/whatsnew/3.6.html#pep-529-change-windows-filesystem-encoding-to-utf-8

[pandas의 이슈]를 보니 다음 버전인 0.21.0이나 되어야 해결될 것 같다. 유니코드 문제이니 파일 및 폴더 이름을 영어로 바꾸거나, HDFStore를 열기 전에 아래와 같이 실행시키면 된다. 아래 방법은 sys._enablelegacywindowsfsencoding()으로 파일시스템 인코딩을 예전 방식으로 바꾸는 것이니 웬만하면 파일 이름을 바꾸면 좋겠다.

[pandas의 이슈]: https://github.com/pandas-dev/pandas/issues/15086

```python
import sys
sys._enablelegacywindowsfsencoding()

import pandas as pd
from pandas import DataFrame
df = DataFrame([[1,2],[3,4]])
store = pd.HDFStore(r'C:\오리\store.h5')
store['df'] = df
store['df']
```

```
Out[5]: 
   0  1
0  1  2
1  3  4
```

