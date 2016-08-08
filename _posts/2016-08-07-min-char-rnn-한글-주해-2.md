---
title: min-char-rnn 한글 주해(2) - 메인 루프
date: 2016-08-07 23:00
categories:
- 딥러닝
tags:
- RNN
- 텍스트
layout: post
published: true
---

#### 이전 글

* [min-char-rnn 한글 주해(1) - 데이터 준비, 변수 초기화]({{ site.baseurl }}{% post_url 2016-08-02-min-char-rnn-한글-주해-1 %})

전체 코드 링크 - [한글 주석 추가 전체 코드](https://gist.github.com/MinjeJeon/8f50693f0a986419ab2dda35753acb1f), [Andrej Karpathy가 작성한 원본 코드](https://gist.github.com/karpathy/d4dee566867f8291f086)

\\
변수를 초기화 했으면 손실 값 및 그래디언트를 산출하는 손실 함수와 텍스트 만들어 주는 생성 함수를 구성하고, 루프를 돌리며 가중치를 학습시켜야 한다. 원래 코드상에는 함수가 먼저 나오지만, 프로그램 실행 순서대로 메인 루프 부분을 먼저 살펴보려고 한다.

## 메인 루프 이전 변수 초기화 

```python
n, p = 0, 0 #  반복 회수(n) 및 입력 데이터(p) 위치 초기화 

# Adagrad 알고리즘에 사용되는 메모리 변수 초기화
mWxh, mWhh, mWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
mbh, mby = np.zeros_like(bh), np.zeros_like(by) 
smooth_loss = -np.log(1.0/vocab_size)*seq_length # 학습이 이루어지기 전의 손실값
```

학습 과정을 진행하기 이전에 adagrad 최적화 알고리즘을 위한 메모리 변수를 준비한다. 각 가중치와 동일한 shape를 가진 행렬을 0으로 초기화한다. smooth\_loss는 최적화가 전혀 진행되지 않은 상태를 초기값으로 한다.

```python
while True:
  # 입력데이터 준비, 텍스트의 맨 앞쪽부터 seq_length만큼씩 데이터를 준비
  # 데이터를 모두 사용하면 입력 데이터의 맨 처음으로 이동
  if p+seq_length+1 >= len(data) or n == 0: 
    hprev = np.zeros((hidden_size,1)) # RNN 메모리 초기화
    p = 0 # 입력 데이터의 맨 처음으로 이동
  
  # 입력(p~p+24번째 글자), 목표(p+1~p+25번째 글자) 데이터를 준비 
  inputs = [char_to_ix[ch] for ch in data[p:p+seq_length]]
  targets = [char_to_ix[ch] for ch in data[p+1:p+seq_length+1]]
```

메인 루프의 시작 부분이다. 데이터를 읽어들일 위치를 p로 정하고, p번째 글자부터 25개의 글자를 준비한다. min-char-rnn 모델의 목적은 어떤 글자를 넣었을 때, 다음 글자를 추론해 내는 것이기 때문에, 정답 세트로 p+1번째 글자부터 25개의 글자를 준비한다.

모델에 데이터를 입력하기 위해 문자를 char_to_ix 사전을 이용하여 각 문자에 대응하는 숫자의 리스트로 변환하여 준다. 

```python
  # 학습을 100번 반복할 때마다 학습 결과를 출력
  if n % 100 == 0:
    sample_ix = sample(hprev, inputs[0], 200) #sample 함수로 
    txt = ''.join(ix_to_char[ix] for ix in sample_ix)
    print('----\n %s \n----' % (txt, ))
```

이 부분에서는 sample 함수를 이용하여 학습의 결과를 출력하는 부분이다. 여기서는 출력할 첫 글자로 해당 루프에서 학습할 첫 글자를 사용하고, 초기 hidden state는 hprev, 200글자를 출력한다. sample함수는 숫자 200개의 리스트를 리턴하는데, ix_to_char 사전으로 숫자들을 문자로 변환하여 학습의 결과를 출력해준다.

```python
  # 손실함수에서 손실값과 그래디언트를 함께 계산
  loss, dWxh, dWhh, dWhy, dbh, dby, hprev = lossFun(inputs, targets, hprev)
  smooth_loss = smooth_loss * 0.999 + loss * 0.001
  if n % 100 == 0: print('iter %d, loss: %f' % (n, smooth_loss)) # 반복횟수, 손실 출력
```

lossFun 함수에서 손실값 및 그래디언트를 계산하여 값을 가져온다. 화면상에서 손실값을 출력해 줄 때에는 smooth\_loss를 사용하는데, 현재 손실값을 1/1000으로 줄이고 기존 값에 999/1000 가중치를 줘서 loss의 변화 폭을 줄인다. 100번 반복하는 경우 smooth\_loss는 아래와 같다. 

$$
smooth\_loss_{100} = 0.999^{100} smooth\_loss_{prev} + 0.001 \left (  0.999^{99}\times L_{1} + 0.999^{98}\times L_{2} + \cdots +  0.999 \times L_{99} + L_{100} \right )
$$

100번마다 학습 결과를 출력해 주기 때문에 이전 출력과 이번 출력 사이의 학습은 약 9.5% 정도 반영된다고 보면 되겠다. 최적화 과정에서 손실값은 항상 내려가지 않고 조금씩 올라가는 경우가 있는데, 이를 보고 학습이 잘못되고 있는 것으로 오해할 수 있어 손실값을 표현할 때 현재 회차의 값보다는 과거 값과 섞어서 부드럽게 표현해 주고 있다.

## Adagrad 알고리즘으로 파라메터 업데이트

```python
  # Adagrad 방식으로 파라미터 업데이트
  for param, dparam, mem in zip([Wxh,  Whh,  Why,  bh,  by],   # 가중치
                                [dWxh, dWhh, dWhy, dbh, dby],  # 그래디언트
                                [mWxh, mWhh, mWhy, mbh, mby]): # 메모리 
    mem += dparam * dparam
    param += -learning_rate * dparam / np.sqrt(mem + 1e-8) # 실제 파라메터 업데이트

  p += seq_length # 데이터 포인터를 seq_length만큼 우측으로 이동
  n += 1 # 반복횟수 카운터
```

min-char-rnn에서는 가중치를 업데이트하기 위한 알고리즘으로 adagrad 알고리즘을 사용하고 있다. 모든 가중치에 대해 일괄적으로 learning_rate에 의해서 업데이트 시키는 방법보다 속도가 매우 빠르다는 장점을 가지고 있다.

{% include image.html
   src='20160804_dd748085_opt2.gif'
   alt='그래디언트 탐색 방법 속도 비교'
   caption='그래디언트 탐색 알고리즘을 비교한 그림. 모든 파라미터를 같은 계수로 학습시키는 SGD(빨강) 보다 다른 Adadelta, Adagrad, Rmsprop 등의 알고리즘이 훨씬 빠르게 작동한다. Image Credit : <a href="https://twitter.com/alecrad">Alec Radford</a>' %}

그래디언트에 일괄적인 학습 속도를 적용하지 않고 각 원소별로 변화폭을 결정해 준다. 그래디언트의 원소 중 큰 항목에 대해서는 이동폭을 작게 조정해주고, 작은 원소에게는 이동폭을 증폭시켜준다. 

`param += -learning_rate * dparam / np.sqrt(mem + 1e-8)`{: .language-python}에서 파라메터 업데이트를 할 때 분모가 mem 이므로 mem이 커질수록 각 원소의 변화폭이 감소한다(분모의 +1e-8은 divide by zero 방지). `mem += dparam * dparam`{: .language-python} 에 따라 메모리 변수에 dparam의 제곱만큼을 계속 더하기 때문에 그래디언트가 큰 원소의 변화 폭이 점차 감소하게 된다. 

예를 들어 mem을 초기값(0)으로, 그래디언트 $$\nabla W_{xh}$$가 아래 행렬과 같다고 가정하면...

$$
\nabla W_{xh} = \begin{pmatrix}
3 & -0.5 & -2 \\ 
1.1 & 0.03 & \textbf{0.001} \\ 
-1.1 & \textbf{-5} & -0.14
\end{pmatrix}
$$

굵게 표시된 두 값 (0.001, -5) 에 대한 mem값은 각각 (0.000001, 25) 이다. 실제 업데이트 할 때에는 각각 (0.001 / 0.00100001 = 0.99999, -5 / 5.00000001 = -0.99999) 만큼 업데이트되므로 방향을 제외한 그래디언트 원소 간의 편차가 제거된다. 그리고 mem 값의 증가에 따라 이동 속도가 점차 감소하는데, 이로 인해 learning_rate를 크게 가져갈 수 있게 되므로 학습 속도 향상이 가능한 것 같다.

복잡하면 **그냥 빠르다!!** 라고 생각하면 된다. 각 머신러닝 패키지에서 지원하는 좋은 알고리즘을 사용해보자.

## 참고

<!-- * cs231n 강좌 Cross-entropy 부분 - <http://cs231n.github.io/linear-classify/#softmax-classifier> -->
* latex 수식 편집기 - <http://mathurl.com/>