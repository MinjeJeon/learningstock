---
title: jekyll 블로그에서 구글 맞춤검색으로 검색창 만들기
date: 2017-10-02 13:24 +0900
categories:
- blogging
tags:
- jekyll
- github
- google
layout: post
image: 20171002_gcse_cover.jpg
published: true
---

깃헙 페이지(github pages, <https://pages.github.com>)는 정적(static, 내용이 고정된) 사이트를 호스팅 할 수 있는 툴입니다. 깃헙 리포지토리에 html, css, js, 이미지 등을 올리면 인터넷에서 볼 수 있도록 무료로 호스팅을 해줍니다. 그런데 github pages에서는 jekyll이라는 사이트 생성기를 기본적으로 지원하고 있어서 블로그 용도로도 사용이 가능합니다. 글의 내용이 들어있는 [markdown](https://guides.github.com/features/mastering-markdown/) 파일만 github에 올리면 그에 맞추어 레이아웃이 포함된 html 사이트를 자동으로 생성해 주죠. 이 페이지도 실제로는 markdown 양식으로 작성되어 있습니다. 기본적인 사용법과 설명은 아래 글을 참고해 주세요.

* [Github Page로 블로그 호스팅](http://gjchoi.github.io/env/Github-page%EB%A1%9C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0/)
* [GitHub의 페이지 기능 이용하기](http://dogfeet.github.io/articles/2012/github-pages.html)

{% include ls/image.html
   src='20171002_editing_markdown.png'
   alt='markdown 편집 화면'
   caption='실제로 이 포스트를 작성할 때의 편집 화면.' %}

github pages의 장점은 아무래도 '**기술스러운** 느낌을 줄 수 있다'이지 않을까 싶네요. '[github.io](github.io)'도메인이 달려 있으면 왠지 기술력 있는 느낌을 준다고나 할까요? 문서를 작성할 때에도 WYSIWYG 에디터가 아닌 텍스트 에디터만을 이용하기 때문에 글의 내용에 집중하기 쉽다는 것도 장점입니다. 그리고 뼈대를 이루는 레이아웃 구조가 단순하기 때문에 세세한 부분까지 마음대로 고칠 수 있죠. 물론 워드프레스 같은 설치형 블로그를 운영해도 세세하게 수정이 가능하지만, 워낙 코드가 많기 때문에 하나하나 고치기에는 이해해야 하는 부분이 많아요. 그래서인지 [카카오 기술 블로그](http://tech.kakao.com/2016/07/07/tech-blog-story/)도 github pages로 이사를 가게 되었습니다.

하지만 장점이 있는 만큼 단점도 있습니다. jekyll은 '정적'인 사이트를 만드는 기능만 있다 보니 검색, 태그별 글 모음 등 동적으로 컨텐츠를 제공하는 기능에 있어서는 일반적인 블로깅 툴에 비해 기능이 상당히 떨어집니다. 하지만 geek들이 많이 사용하는 툴 답게 이러한 한계를 기술적으로 많이 극복을 해 놓은 상태입니다. 구글에서 검색해 보면 jekyll의 한계를 넘어서는 다양한 기능을 html과 js로 구현해 놓은 글을 볼 수 있습니다. [카카오 기술 블로그](http://tech.kakao.com/2016/07/07/tech-blog-story/)에서는 정적 사이트에서 구현하기 힘든 태그와 작성자별 글 목록을 보여주는 방법을 올려 놓았습니다.

설치형 블로그에서는 보통 검색 기능을 제공하고 있는데, jekyll은 정적 사이트 생성기일 뿐이어서 동적으로 결과를 보여주는 검색이라는 기능을 구현하기에는 한계가 있죠. 하지만 기술스러운 사람은 어떻게든 방법을 만들어 내더라고요. 하나의 방법은 검색에 필요한 연산을 클라이언트에 맡기는 방법입니다. 사용자에게 모든 텍스트가 들어있는 파일을 다운로드 시키고, 자바스크립트로 클라이언트의 웹 브라우저에서 텍스트를 찾게 하는 방법입니다.

* [luna.js를 이용한 jekyll 블로그 검색(영어)](https://learn.cloudcannon.com/jekyll/jekyll-search-using-lunr-js/)
* [지킬 블로그에 검색 기능 추가하기](https://imyeonn.github.io/blog/blog/30/)

많이 복잡한데, 좀 더 쉽게 할 수 있는 방법은 없을까요?

## 구글 맞춤검색으로 사이트 검색엔진 만들기

구글에서 제공하는 custom search engine(CSE) 라는 사이트 맞춤 검색 서비스가 있습니다. 내 홈페이지만의 검색 결과를 표시해 줄 수 있는 맞춤형 구글 검색 엔진을 탑재할 수 있는 기능입니다. 내 사이트의 검색 결과가 구글에 나오고 있다면, 구글 맞춤 검색으로 내 github pages 내의 검색 결과를 표시할 수 있습니다. 그리고 마치 사이트 내에서 검색이 작동하는 것처럼 검색 결과 디자인을 일체화할 수 있도록 세부적인 설정도 가능합니다. 실제로 제 블로그에도 구현해 보았는데요. 맨 윗부분의 'Search in 컴퓨터, 주식을 배우다' 에 텍스트를 넣고 검색하면 검색 결과가 표시됩니다. [바로가기](#searchtext) 

{% include ls/youtube.html
   src='Qd9z48Bo8ZA'
   alt='구글 맞춤 검색 소개영상'
   caption='구글 맞춤검색 소개영상. 톱니바퀴 > 자동 번역 > 한국어 선택시 한글 자막이 표시됩니다.' %}

### 구글에서 맞춤형 검색 엔진 만들기

먼저 구글의 구글 맞춤검색(<https://cse.google.co.kr>)사이트로 이동합니다. 검색엔진을 만들 사이트 주소를 입력하고 만들기 버튼을 클릭하면 맞춤형 검색 엔진 만들기가 완료됩니다.

{% include ls/image.html
   src='20171002_create_gcse_01.png' %}

왼쪽 메뉴에서 '디자인'을 클릭하면 구글 맞춤검색이 표시되는 방법을 지정할 수 있습니다. 저는 지금 운영중인 jekyll 블로그와 어울리는 디자인을 직접 만들어 보려고 '검색결과만'을 선택하였습니다. 별도의 디자인 구성 없이 코드 삽입만으로 편리하게 쓰려면 '오버레이' 선택을 추천 드립니다.

{% include ls/image.html
   src='20171002_create_gcse_02.png' %}

선택 후 '저장 및 코드 생성'을 클릭하면 아래와 같이 코드가 나옵니다. 이 코드는 나중에 설정 메뉴에서 다시 받을 수 있습니다.

```javascript
<script>
  (function() {
    var cx = '구글 맞춤검색 ID';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
  })();
</script>
<gcse:search></gcse:search>
```

### 정적 페이지 구성하기

이제 검색 엔진을 만들었으니, 검색창과 검색 결과 html을 만들어 보겠습니다. 먼저 검색창을 표시할 search.html을 만들어 보겠습니다. 검색결과 제출 및 결과 처리를 위해 jquery를 활용합니다. 검색어가 들어오면 result.html을 호출하면서 q 파라미터에 검색어를 넣어서 이동합니다.

```html
<html>
  <head>
    <!-- jquery 불러오기 -->
    <script
    src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha256-k2WSCIexGzOj3Euiig+TlR8gA0EmPjuc79OEeY5L45g="
    crossorigin="anonymous"></script>
  </head>
  <body>
    <!-- 검색 상자 -->
    <form id="searchform" class="searchbox" action="#">
      <input id="searchtext" name="searchtext" type="text" placeholder="Search...">
    </form>
    <!-- 검색어 submit 이벤트 처리 -->
    <script>
      $(document).ready(function(){
        $("#searchform").on("submit", function(e){
          e.preventDefault();
          var url = encodeURIComponent($("#searchtext").val());
          location.href = "./result.html?q=" + url;
        });
      });
    </script>
  </body>
</html>
```

같은 디렉토리에 검색결과를 표시할 result.html 파일을 만듭니다. `<title>` 태그에 창 제목이 들어있고, `<h1>` 태그에 제목이 들어있는데요. jekyll같이 정적으로만 사이트를 제공하는 툴에서는 서버에서 태그 안의 내용을 변경할 수 없습니다. 앞에서 넘겨준 파라미터를 이용해 javascript를 이용한 꼼수로 내용을 변경해 보겠습니다.

```html
<html>
  <head>
    <!-- jquery 불러오기 -->
    <script
    src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha256-k2WSCIexGzOj3Euiig+TlR8gA0EmPjuc79OEeY5L45g="
    crossorigin="anonymous"></script>
    <title>검색 결과</title>
  </head>
  <body>
    <!-- 검색 결과 제목 -->
    <h1 id="page_title">검색 결과</h1>
    <script>
      function getUrlVars() // 쿼리 스트링을 파싱하는 함수
      {
        var vars = [], hash;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for(var i = 0; i < hashes.length; i++)
        {
          hash = hashes[i].split('=');
          vars.push(hash[0]);
          vars[hash[0]] = hash[1];
        }
        return vars;
      }
      $(document).ready(function(){ // 쿼리 스트링에서 'q'파라미터를 읽어 창 제목과 표시 제목을 바꿈
        var txt_title = "'" + decodeURIComponent(getUrlVars()['q']) + "' - 검색 결과"
        $("#page_title").text(txt_title);
        document.title = txt_title;
      });
      (function() {
        var cx = '구글 CSE 아이디';
        var gcse = document.createElement('script');
        gcse.type = 'text/javascript';
        gcse.async = true;
        gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(gcse, s);
      })();
    </script>
    <gcse:searchresults-only></gcse:searchresults-only>
  </body>
</html>
```

두 파일을 같은 디렉토리에 넣고 검색을 수행해 보았습니다. 아래 두 그림 중 위의 그림은 search.html을 열었을 때 화면이고, 아래 그림은 'jekyll'을 검색했을 때 나오는 검색 결과입니다.

{% include ls/image.html
   src='20171002_create_gcse_result.png' %}
