---
title: 레이아웃 테스트
categories:
- test
tags:
- test
layout: post
published: true
---

## 이미지 테스트

{% include image.html
   src='test3.jpg'
   alt='alt 텍스트'
   caption='캡션 테스트' %}

{% include image.html
   src='test1.jpg'
   alt='alt_text'
   caption='caption_text' %}

{% include youtube.html
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


