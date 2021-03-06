---
title: min-char-rnn 한글 주해(3) - 손실값 계산, 그래디언트 계산, 문자 출력함수
date: 2016-08-28 11:40
categories:
- 딥러닝
tags:
- RNN
- 텍스트
layout: post
published: true
image: 20160818_7f5d6a69_rnn-backward-1.png
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
  # forward pass(손실값 계산)
  for t in range(len(inputs)):
    ...
```

함수의 입력으로 사용되는 inputs, targets는 모두 문자를 인덱싱한 숫자의 리스트이고, hprev는 이전 학습에서의 마지막 hidden state값이다. forward pass에서 h값, y값, p값을 차례대로 구하는 것은 다른 뉴럴 네트워크와 동일하지만, 여기서는 들어오는 글자 수만큼 학습이 반복되기 때문에 캐싱을 위한 변수를 사전으로 초기화하고 각각의 사전에 0부터 글자의 길이만큼 값을 넣어준다. 

처음(0번째)에 t-1번째의 h값으로 사용하기 위해 `hs[-1]`에 `hprev`값을 넣어준다. 파이썬은 참조에 의한 전달을 사용하므로 값이 변경될 위험이 있을 때 copy함수를 사용하는데, 여기서는 값의 변동이 없어 `hs[-1] = hprev`{: .language-python}를 넣어줘도 무방하다. 그렇지만 copy함수를 넣어야 할 때 안 넣으면 결과가 치명적이므로 copy를 사용하여 값을 할당해 주는 것이 안전하다.

```python
  # forward pass(손실값 계산)
  for t in range(len(inputs)):
    xs[t] = np.zeros((vocab_size,1)) # 1-of-k(one-hot) 형태로 변환. 모든 값이 0인 array 준비
    xs[t][inputs[t]] = 1 # 해당하는 글자에만 값을 1로 설정 - [0, ..., 0, 1, 0, ..., 0]
    hs[t] = np.tanh(np.dot(Wxh, xs[t]) + np.dot(Whh, hs[t-1]) + bh) # hidden state 업데이트
    ys[t] = np.dot(Why, hs[t]) + by # 다음 글자가 어떤 글자가 나올지에 가능성을 표시한 array(정규화되지 않음)
    ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t])) # softmax로 각 글자의 등장 가능성을 확률로 표시
    loss += -np.log(ps[t][targets[t],0]) # cross-entropy를 이용하여 정답과 비교하여 손실값 판정
```

글자 수만큼 루프를 타면서 loss를 계산하는 과정이다.

* `xs[t]` - t번째의 입력 문자. 1-of-k 또는 one-hot encoding을 통해 한 개의 값만 1인 array(ex. [0, ..., 0, 1, 0, ..., 0])를 만들어서 넣어준다.
* `hs[t]` - t번째의 hidden state. 직전의 hidden state(`hs[t-1]`), 입력값(`xs[t]`), bias를 더하고, tanh 함수에 더한 값을 넣어 다음 단계로 보낸다.
* `ys[t]` - 계산의 결과로 다음 글자가 어떤 글자가 나타날 확률이 높은지 나타내는 array이다. 이 값이 높을수록 나타날 확률이 높아지지만, 로그 확률이기 때문에 음수도 있어 직관적으로 이해하기는 어려운 숫자이다.
* `ps[t]` - softmax 함수를 이용하여 각 문자가 나타날 확률을 합이 1인 확률분포로 만들어준다.
* `loss` - forward pass의 결과로 계산된 손실값이며, 최종적으로는 각 시점에서 계산된 손실값의 총합을 나타낸다. $$ \left ( loss = loss_{1} + loss_{2} + loss_{3} + \ldots + loss_{25} \right )$$

{% include ls/image.html
   src='20160817_21bc366d_rnn-forward-1.png'
   alt='RNN에서 각 시점에서 문자가 나타날 확률을 계산하는 과정'
   caption='RNN에서 각 시점에서 문자가 나타날 확률을 계산하는 과정' %}

루프를 반복하면서 각각의 글자가 나타날 확률을 만들어내는데, 마지막 글자에 이르면 상당히 깊은 네트워크가 만들어지게 된다. 

## 그래디언트 계산(backward pass)

앞에서 손실값을 계산할 때 입력 글자 수 만큼 반복하였기 때문에 전체 손실을 수식이나 그래프로 표현하게 되면 엄청나게 길어지게 된다. 다행히 다변수 함수에 대한 연쇄법칙(참고 - [위키백과](https://ko.wikipedia.org/wiki/%EC%97%B0%EC%87%84_%EB%B2%95%EC%B9%99#.EB.8B.A4.EB.B3.80.EC.88.98_.ED.95.A8.EC.88.98.EC.97.90_.EB.8C.80.ED.95.9C_.EC.97.B0.EC.87.84.EB.B2.95.EC.B9.99), [네이버 블로그](http://blog.naver.com/PostView.nhn?blogId=mindo1103&logNo=90103548178))에 의해 RNN의 각 반복마다 루프를 거꾸로 돌면서 그래디언트를 계산해 단순히 값을 더해주기만 하면 된다. 

{% include ls/image.html
   src='20160818_7f5d6a69_rnn-backward-1.png'
   alt='t=1 시점에서의 그래디언트 역전파'
   caption='t=1 시점에서의 그래디언트 역전파 다이어그램. 전체를 표현하려면 훨씬 커진다.' %}

```python
  dWxh, dWhh, dWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
  dbh, dby = np.zeros_like(bh), np.zeros_like(by)
  dhnext = np.zeros_like(hs[0])
```

그래디언트 계산을 위한 변수를 초기화한다. 각각의 그래디언트는 각 가중치 변수와 같은 형태를 가진 array이므로, np.zeros_like함수를 이용하여 0으로 초기화한다.

```python
  for t in reversed(range(len(inputs))): #위의 과정을 반대로 진행(t=24부터 시작)
    dy = np.copy(ps[t])
    dy[targets[t]] -= 1 # y의 그래디언트 계산 - softmax 함수의 그래디언트 계산
    dby += dy
    dWhy += np.dot(dy, hs[t].T)
    dh = np.dot(Why.T, dy) + dhnext # loss에서 사용된 h와 h를 업데이트한 계산의 그래디언트 값을 더함
    dhraw = (1 - hs[t] * hs[t]) * dh # tanh 역전파
    dbh += dhraw
    dWxh += np.dot(dhraw, xs[t].T)
    dWhh += np.dot(dhraw, hs[t-1].T)
    dhnext = np.dot(Whh.T, dhraw)
```

dy.. 로 시작되는 줄이 위 그림에서 $$ y_{1} \rightarrow p_{1} $$ 으로 역전파되는 과정이다. softmax의 그래디언트를 산출하는데, 금방 와닿지는 않지만 아래 수식으로 된다고 한다. [원문 참고자료](http://cs231n.github.io/neural-networks-case-study/#grad)

$$ \frac{\partial L_i }{ \partial f_k } = p_k - \mathbb{1}(y_i = k) $$

dy에서 $$+$$게이트를 타기 때문에 때문에 양쪽에 같은 값이 전파된다. 여기서 $$b_y$$의 그래디언트 값이 결정되고, $$\times$$게이트에서는 양쪽의 값을 바꾸어 곱하여 $$W_{hy}$$의 그래디언트가 나온다.
특이하게 dh를 구할 때 dhnext란 값을 더해주는데, 손실값에 반영되지 않는 hidden state의 업데이트 계산$$(h_t \rightarrow h_{t+1})$$에 대해서도 역전파를 해주어야 한다고 [답변을 하였다.](https://gist.github.com/karpathy/d4dee566867f8291f086#gistcomment-1694245)

dhraw값은 tanh게이트를 통과한 그래디언트 값이고, 이후는 일반적인 연쇄 법칙대로 진행된다. 


```python
  for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
    np.clip(dparam, -5, 5, out=dparam) # 그래디언트 발산 방지
  return loss, dWxh, dWhh, dWhy, dbh, dby, hs[len(inputs)-1]
```

이후 그래디언트의 각 원소에서 절대값이 5가 넘어가는 값은 그래디언트의 발산 방지를 위해 np.clip 함수를 이용하여 최대 절대값을 5로 만들어 주고 결과를 반환한다.

## 텍스트 생성(sample)

```python
def sample(h, seed_ix, n):
  x = np.zeros((vocab_size, 1))
  x[seed_ix] = 1
  ixes = []
  for t in range(n):
    # forward pass 수행
    h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h) + bh)
    y = np.dot(Why, h) + by
    p = np.exp(y) / np.sum(np.exp(y))

    # 샘플링. 임의성을 부여하기 위해 argmax대신 array p에서 주어진 확률에 의해 하나의 문자를 선택
    ix = np.random.choice(range(vocab_size), p=p.ravel())

    # 다음 글자 추론을 위해 샘플링 된 글자를 다음 입력으로 사용 
    x = np.zeros((vocab_size, 1))
    x[ix] = 1
    
    # 결과값 리스트에 추가
    ixes.append(ix)
  return ixes
```

모델에서 지정된 글자 수(n) 만큼의 글자(숫자의 리스트)를 출력하는 함수이다. 입력으로 hidden state h, 첫번째로 사용할 글자 seed_ix를 받는다. 여기서 첫번째 글자는 이번 학습에 사용되는 글자 중 첫번째 글자와 동일하다([이전 글 참고]({{ site.baseurl }}{% post_url 2016-08-07-min-char-rnn-한글-주해-2 %}#section-2)).

초기값을 기반으로 글자를 하나씩 뽑아내는데 무조건 가장 나타날 확률이 높은 문자를 뽑는 게 아니라, np.sample 함수로 확률을 이용하여 추출한다. 이로 인해 생성되는 글자는 어느 정도 임의성을 부여받게 된다.

\\
지금까지 살펴본 RNN은 가장 간단한 형태의 RNN이라서 100만번을 돌려봐도 만족할 만한 결과는 나오지 않았다. 가끔 대문자로 이름을 말하고, 콜론 이후 의미불명의 문자열을 뱉어내는 게 최선인 정도였다. GPU를 이용하여 훈련 속도를 높히고, 층을 더 쌓아서 모델을 구성하면 더 좋은 결과를 뽑아낼 수 있을 것이다.