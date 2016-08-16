---
title: min-char-rnn 한글 주해(3) - 손실값 계산, 그래디언트 계산, 문자 출력함수
date: 2016-08-16 16:50
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
* [min-char-rnn 한글 주해(2) - 메인 루프]({{ site.baseurl }}{% post_url 2016-08-07-min-char-rnn-한글-주해-2 %})

전체 코드 링크 - [한글 주석 추가 전체 코드](https://gist.github.com/MinjeJeon/8f50693f0a986419ab2dda35753acb1f), [Andrej Karpathy가 작성한 원본 코드](https://gist.github.com/karpathy/d4dee566867f8291f086)

\\
먼저 손실값을 구하는 forward pass부터 시작한다. RNN이라고 해서 계산이 어려운 것은 아니고 변수가 하나 더 있고, 계산을 반복해서 수행하는 것으로 생각하면 되겠다.

```python
def lossFun(inputs, targets, hprev):
  xs, hs, ys, ps = {}, {}, {}, {}
  hs[-1] = np.copy(hprev)
  loss = 0
  # forward pass
  for t in range(len(inputs)):
    ...
```
inputs, targets는 모두 문자를 인덱싱한 숫자의 리스트를 입력으로 한다. RNN은 입력된 글자의 숫자만큼 로스펑션 및 그래디언트를 만드는 행위를 반복하기 때문에 아래의 루프를 타면서 손실값을 계산하게 된다.

hprev값은 지금까지 x의 입력으로 인해서 변화된 가장 마지막 hidden state를 가지고 와서 첫번째 입력 0시점에 사용될 hidden state이다.

0번째 시점에서의 

이제 0부터 inputs 리스트의 길이만큼 루프를 돌면서 손실값을 계산한다. 

t번째 각각의 xs, hs, ys, ps를 빈 사전으로 초기화한다.
* xs[t] - t번째의 입력 문자. 1-of-k 또는 one-hot encoding을 통해 한 개의 값만 1인 array를 만든다. 
* hs[t] - t번째의 hidden state. x[0] 부터 Wxh, Whh에 의해 변화한 수치이다.
* ys[t] - 

```python
  # forward pass
  for t in range(len(inputs)):
    xs[t] = np.zeros((vocab_size,1)) # encode in 1-of-k representation
    xs[t][inputs[t]] = 1
    hs[t] = np.tanh(np.dot(Wxh, xs[t]) + np.dot(Whh, hs[t-1]) + bh) # hidden state
    ys[t] = np.dot(Why, hs[t]) + by # unnormalized log probabilities for next chars
    ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t])) # probabilities for next chars
    loss += -np.log(ps[t][targets[t],0]) # softmax (cross-entropy loss)
```

loss를 계산하는 과정이다. 입력으로 들어오는 문자열 시퀀스의 횟수만큼 가중치 적용과 출력을 반복한다.

첫번째 문자의 경우는 이렇고, 다음 문자의 경우는 이러하다.

이것으로 분석을 마치겠다. 가장 간단한 형태의 RNN이라서 100만번을 돌려봐도 만족할 만한 결과는 나오지 않았다. 가끔 대문자로 이름을 말하고, 콜론 이후 의미불명의 문자열을 뱉어내는 게 최선인 정도였다. 가속기를 이용하여 훈련 속도를 높히고, 층을 더 쌓아서 모델을 구성하면 더 좋은 결과를 뽑아낼 수 있을 것이다.