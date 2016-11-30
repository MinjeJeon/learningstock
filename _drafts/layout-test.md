---
title: 레이아웃 테스트
categories:
- test
tags:
- test
layout: post
published: true
---

## 이미지 테스트[^fn1]

{% include ls/image.html
   src='test3.jpg'
   alt='alt 텍스트'
   caption='캡션 테스트' %}

{% include ls/image.html
   src='test1.jpg'
   alt='alt_text'
   caption='caption_text' %}

{% include ls/youtube.html
   src='kE9ZSBkbQNY'
   alt='alt_text'
   caption='유튜브 캡션 테스트' %}

## 내부 페이지 링크

## MathJax

$$
smooth\_loss_{100} = 0.999^{100} smooth\_loss_{prev} + 0.001 \left (  0.999^{99}\times L_{1} + 0.999^{98}\times L_{2} + \cdots +  0.999 \times L_{99} + L_{100} \right )
$$

$$
\nabla W_{xh} = \begin{pmatrix}
3 & -0.5 & -2 \\ 
1.1 & 0.03 & \textbf{0.001} \\ 
-1.1 & \textbf{-5} & -0.14
\end{pmatrix}
$$

This is some text not written in HTML but in another language!

definition term 1
definition term 2
: This is the first line. Since the first non-space characters appears in
column 3, all other lines[^def1] have to be indented 2 spaces (or lazy syntax may
  be used after an indented line). This tells kramdown that the lines
  belong to the definition.
:    This is the another definition for the same term. It uses a
     different number of spaces for indentation which is okay but
     should generally be avoided.
   : The definition marker is indented 3 spaces which is allowed but
     should also be avoided.

[^fn1]: footnote1
[^def1]: footnote2