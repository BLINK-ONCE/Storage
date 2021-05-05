## Backpropagation

- recursive application of the chain rule along a computiational graph to compute the gradients of all inputs/parameters/intermediates
- 모든 input값,

### 1. a simple example

![backprop. simple example1]([https://blog.kakaocdn.net/dn/vgPV4/btqDOjh9ow6/XqQnYmCTbryWMHAwFmCBO1/img.png](https://blog.kakaocdn.net/dn/vgPV4/btqDOjh9ow6/XqQnYmCTbryWMHAwFmCBO1/img.png))

함수 f(x,y,z)가 있다.

f(x,y,z) = (x+y)z.

이때 backprop은 어떻게 구할 수 있을까?

![backprop. simple example1 answer1]([https://blog.kakaocdn.net/dn/b9Vsa0/btqDO1Bfh4p/XULKLy9CtLk9SCkcDf2cxk/img.png](https://blog.kakaocdn.net/dn/b9Vsa0/btqDO1Bfh4p/XULKLy9CtLk9SCkcDf2cxk/img.png))

우리가 원하는 기울기는 x에 대한 f의 기울기, y에 대한 f의 기울기, z에 대한 f의 기울기이다.

chain-rule을 이용하여 각각의 gradient를 구해보자. chian-rule을 이용하여 각각의 변수에 대한 gradient를 구하는 방법으로는 upstream gradient에 local gradient를 곱해서 구하는 방법이 있다. 

# Reference

- [모두를 위한 cs231n](lec4-backprop and NN]([https://deepinsight.tistory.com/98?category=897056](https://deepinsight.tistory.com/98?category=897056))