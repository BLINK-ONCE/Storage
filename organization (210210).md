# 5.5 Maximum likelihood Estimation

이전에, 우리는 공통 추정기의 몇 가지 정의를 보고 그 속성을 분석하였다. 그런데 이 추정기들은 어디서 왔을까? 일부 함수가 좋은 추정기를 만들 수 있다고 추측하고 그 편향과 분산을 분석하는 대신, 우리는 다른 모델에 대한 좋은 추정기인 특정 함수를 도출할 수 있는 몇 가지 원칙을 가지고 싶다.

이러한 가장 일반적인 원칙은 최대우도원칙이다. 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aec109d5-27c4-4fd7-a4d7-b8b956eb58e6/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aec109d5-27c4-4fd7-a4d7-b8b956eb58e6/Untitled.png)

pdata(x) 분포를 생성하는 실제 데이터와는 독립적으로 그려진 일련의 예시 X = {x1, ... , xm}을 생각해 보자.

pm모델(x;α)을 α에 의해 지수화된 동일한 공간에 대한 확률분포의 파라메트릭 계열로 하자. 즉, pmodel(x;α)은 모든 구성 x를 실제 확률 pdata(x)를 추정하는 실제 숫자에 매핑합니다.

그러면 α에 대한 최대우도 추정기는 다음과 같이 정의된다.

(5.56, 57)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5267731b-cb2e-42d9-89ca-ddba73bb5f1d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5267731b-cb2e-42d9-89ca-ddba73bb5f1d/Untitled.png)

이것은 여러 가지 이유로 인해 불편할 수 있다. 예를 드르어, 수치적 언더플로우가 발생하기 쉽다. 보다 편리하지만 동등한 최적화 문제를 얻기 위해, 우린느 우도의 로그를 취하면 argmax가 변경되지 않고 이것을 다음과 같은 합으로 편리하게 변환하는 것을 볼 수 있다.

(5.58)