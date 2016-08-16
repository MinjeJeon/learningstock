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
이전 글에서 데이터를 준비하고, 전체적인 RNN 학습 과정을 알아보았다. 여기서는 손실값을 구하는 forward pass 및 학습을 위해 변화시킬 그래디언트를 구하는 backward pass에 대해 해설하려고 한다. RNN이라고 해서 계산이 어려운 것은 아니고 변수가 하나 더 있고, 계산을 여러 번에 걸쳐 반복 수행하는 것으로 생각하면 되겠다.

## 손실값 계산(forward pass)

```python
def lossFun(inputs, targets, hprev):
  xs, hs, ys, ps = {}, {}, {}, {}
  hs[-1] = np.copy(hprev)
  loss = 0
  # forward pass
  for t in range(len(inputs)):
    ...
```

inputs, targets는 모두 문자를 인덱싱한 숫자의 리스트이고, hprev값은 이전 학습에서의 마지막 hidden state를 가져온다. forward pass에서 h값, y값, p값을 차례대로 구하는 것은 다른 뉴럴 네트워크와 동일하지만, 여기서는 들어오는 글자 수만큼 학습이 반복되기 때문에 캐싱을 위한 변수를 사전으로 초기화하고 각각의 사전에 0부터 글자의 길이만큼 값을 넣어준다. 처음(0번째)에 t-1번째의 h값으로 사용하기 위해 hs[-1]에 hprev값을 넣어준다. 파이썬은 참조에 의한 전달을 사용하므로 값이 변경될 위험이 있을 때 copy함수를 사용하는데, 여기서는 값의 변동이 없어 `hs[-1] = hprev`{: .language-python}를 넣어줘도 무방하다. 그렇지만 copy함수를 넣어야 할 때 안 넣으면 결과가 치명적이므로 copy를 사용하여 값을 할당해 준다.

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

글자 수만큼 루프를 타면서 loss를 계산하는 과정이다.

* xs[t] - t번째의 입력 문자. 1-of-k 또는 one-hot encoding을 통해 한 개의 값만 1인 array(ex. [0, 0, ..., 1, 0, 0])를 만들어서 넣어준다.
* hs[t] - t번째의 hidden state. x[0] 부터 Wxh, Whh에 의해 변화한 수치이다.
* ys[t] - 입력으로 들어오는 문자열 시퀀스의 횟수만큼 가중치 적용과 출력을 반복한다.

여기서는 각 t 시점의

## 그래디언트 계산(backward pass)

```python
  dWxh, dWhh, dWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
  dbh, dby = np.zeros_like(bh), np.zeros_like(by)
  dhnext = np.zeros_like(hs[0])
```


첫번째 문자의 경우는 이렇고, 다음 문자의 경우는 이러하다.

## 텍스트 생성(sample)

이것으로 분석을 마치겠다. 가장 간단한 형태의 RNN이라서 100만번을 돌려봐도 만족할 만한 결과는 나오지 않았다. 가끔 대문자로 이름을 말하고, 콜론 이후 의미불명의 문자열을 뱉어내는 게 최선인 정도였다. 가속기를 이용하여 훈련 속도를 높히고, 층을 더 쌓아서 모델을 구성하면 더 좋은 결과를 뽑아낼 수 있을 것이다.